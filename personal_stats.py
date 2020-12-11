import re
import datetime

header = """      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score"""
new_header = """      --------Part 1--------   --------Part 2--------  --------Delta--------
Day       Time   Rank  Score       Time   Rank  Score       Delta rank  Delta time"""


stats = """
 11   02:20:42   8833      0   02:46:37   7158      0
 10   03:09:23  16635      0   07:32:15  15346      0
  9   02:35:35  14408      0   02:46:41  13079      0
  8   03:05:11  16551      0   03:25:06  13837      0
  7   05:57:16  18664      0   06:07:51  15021      0
  6   09:37:37  36350      0   09:44:54  33848      0
  5   03:16:34  14519      0   03:21:16  13611      0
  4   02:17:37  14475      0   02:58:30  11542      0
  3   03:06:56  17982      0   03:18:47  16885      0
  2   02:53:45  15724      0   03:08:50  15256      0
  1   15:30:58  57284      0   15:41:05  53086      0
"""


print(new_header)
stat_line_re = re.compile(
    r"^\s+(?P<day>\d+)\s+(?P<time1>[0-9:]+)\s+(?P<rank1>\d+)\s+(?P<score1>\d+)\s+(?P<time2>[0-9:]+)\s+(?P<rank2>\d+)\s+(?P<score2>\d+)$"
)
time_format = "%H:%M:%S"
for line in stats.split("\n"):
    if line:
        m = stat_line_re.match(line)
        d = m.groupdict()
        time1 = datetime.datetime.strptime(d["time1"], time_format)
        time2 = datetime.datetime.strptime(d["time2"], time_format)
        rank1 = int(d["rank1"])
        rank2 = int(d["rank2"])
        delta_rank = rank1 - rank2
        delta_time = time2 - time1
        print("{}       {:5d}        {}".format(line, delta_rank, delta_time))
