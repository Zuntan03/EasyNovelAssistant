import time

from job_queue import JobQueue


class Generator:
    GEN_AREA_DEFAULT_TEXT = """hoge"""

    def __init__(self, ctx):
        self.ctx = ctx

        self.gen_queue = JobQueue()
        self.check_queue = JobQueue()

        self.enabled = False
        self.generate_job = None
        self.check_job = None

        self.pre_check_time = time.perf_counter()
        self.gen_area_text = ""

        self.gen_queue.push(self.initial_launch)

    def initial_launch(self):
        model_name = self.ctx.kobold_cpp.get_model()
        if model_name is None:
            self.ctx.kobold_cpp.launch_server()
        else:
            self.enabled = True
            self.ctx.form.update_title()

    def update(self):
        if self.enabled:
            if self.generate_job is None:
                input_text = self.ctx.input_area.get_text()
                if input_text != "":
                    self.generate_job = self.gen_queue.push(self._generate, input_text=input_text)
            elif self.generate_job.successful():
                result = self.generate_job.result
                if result is None:
                    if self.ctx.kobold_cpp.abort() is None:
                        self.enabled = False
                        self.ctx.form.update_title()
                else:
                    self.ctx.output_area.append_output(result)
                self.generate_job = None
            elif self.generate_job.canceled():
                self.generate_job = None

            if self.check_job is None:
                now_time = time.perf_counter()
                if now_time - self.pre_check_time > self.ctx["check_interval"]:
                    self.check_job = self.check_queue.push(self._check)
                    self.pre_check_time = now_time
            elif self.check_job.successful():
                result = self.check_job.result
                if (result is not None) and (result != self.gen_area_text):
                    if result.startswith(self.gen_area_text):
                        self.ctx.form.gen_area.append_text(result[len(self.gen_area_text) :])
                    else:
                        self.ctx.form.gen_area.set_text(result)
                    self.gen_area_text = result
                self.check_job = None
            elif self.check_job.canceled():
                self.check_job = None
        else:
            if self.generate_job is not None:
                self.ctx.kobold_cpp.abort()
                self.gen_queue.cancel(self.generate_job)
                self.generate_job = None

            if self.check_job is not None:
                self.check_queue.cancel(self.check_job)
                self.check_job = None

        self.check_queue.update()
        self.gen_queue.update()

    def _generate(self, input_text):
        return self.ctx.kobold_cpp.generate(input_text)

    def _check(self):
        return self.ctx.kobold_cpp.check()

    def abort(self):
        self.check_queue.push(self.ctx.kobold_cpp.abort)
