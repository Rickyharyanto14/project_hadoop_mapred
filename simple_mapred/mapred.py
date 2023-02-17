from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.runner import MRJobRunner
import re

# Untuk mengambil pattern word dari input file
WORD_RE = re.compile(r"[\w']+")


class MRJobWordCount(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            )
        ]
    def mapper(self, _, line):
        #mengatur output agar berbentuk list
        for benda in WORD_RE.findall(line):
            yield (benda.lower(), 1)

    def reducer(self, benda, counts):
        yield (benda, sum(counts))


if __name__ == '__main__':
    data_source = "C:\\Users\\ASUS\\.vscode\\project_mapper_reducer\\data\\benda.txt"
    mr_job = MRJobWordCount(args=[data_source])
    with mr_job.make_runner() as runner:
        runner.run()
        output = list(mr_job.parse_output(runner.cat_output()))
        output.sort(key=lambda x: x[1], reverse=True)
        #print(output)
        with open("output.txt", "w") as f:
            for key, value in output:
                f.write(f"{key} {value}\n")
                print(key, value)