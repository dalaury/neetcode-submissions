class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        record_sum = 0
        for operation in operations:
            if operation == "C":
                if len(record) > 0:
                    last = record.pop()
                    record_sum = record_sum - last
            elif operation == "D":
                res = record[-1] * 2
                record.append(res)
                record_sum = record_sum + res
            elif operation == "+":
                res = record[-1] + record[-2]
                record.append(res)
                record_sum = record_sum + res
            else:
                num = int(operation)
                record.append(num)
                record_sum = record_sum + num

        return record_sum