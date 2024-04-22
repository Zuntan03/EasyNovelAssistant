import threading
import time


class Job:
    def __init__(self, func, **kwargs):
        self.func = func
        self.args = kwargs
        self.started = False
        self.finished = False
        self.result = None
        self.callback = None

    def cancel(self):
        if not self.started:
            self.finished = True

    def canceled(self):
        return (not self.started) and self.finished

    def successful(self):
        return self.started and self.finished


class JobQueue:
    sleep_time = 0.05

    def __init__(self):
        self._queue = []
        self._current = None
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def _run(self):
        while True:
            job = self._current
            if (job is not None) and (not job.finished):
                assert job.started
                job.result = job.func(**job.args)
                job.finished = True
                if job.callback is not None:
                    job.callback(job)
            time.sleep(JobQueue.sleep_time)

    def update(self) -> Job:
        for i in range((len(self._queue) - 1), -1, -1):
            if self._queue[i].finished:
                self._queue.pop(i)

        end_job = None
        if (self._current is None) or self._current.finished:
            start_job = None
            if len(self._queue) > 0:
                start_job = self._queue.pop(0)
                start_job.started = True
            end_job = self._current
            self._current = start_job
        return end_job

    def push(self, job_func, **kwargs) -> Job:
        job = Job(job_func, **kwargs)
        self._queue.append(job)
        return job

    def empty(self):
        return (len(self._queue) == 0) and ((self._current is None) or self._current.finished)

    def cancel(self, job):
        job.cancel()
        if job.finished and (job in self._queue):
            self._queue.remove(job)

    def cancel_all(self):
        for i in range((len(self._queue) - 1), -1, -1):
            self._queue[i].cancel()
            if self._queue[i].finished:
                self._queue.pop(i)
