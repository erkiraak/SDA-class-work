import json, pandas, csv, io

with open('number_data.txt') as f:
    json_data = json.load(f)

def get_avg(*args):
    allowed_data_types = (int, float)
    num_args = [arg for arg in args if isinstance(arg, allowed_data_types)]
    return sum(num_args) / len(num_args)


right_side_avg = get_avg(*json_data["right_side"])
left_side_avg = get_avg(*json_data["left_side"])
avg = get_avg(*json_data["left_side"], *json_data["right_side"])

# print(right_side_avg)
# print(left_side_avg)
# print(avg)

csv_data = """album, year, US_peak_chart_post
The White Stripes, 1999, -
De Stijl, 2000, -
White Blood Cells, 2001, 61
Elephant, 2003, 6
Get Behind Me Satan, 2005, 3
Icky Thump, 2007, 2
Under Great White Northern Lights, 2010, 11
Live in Mississippi, 2011, -
Live at the Gold Dollar, 2012, -
Nine Miles from the White City, 2013, -"""


lines = csv_data.splitlines()
reader = csv.reader(lines, delimiter=',', skipinitialspace=True)
with open("data.csv", "w") as csv_data_file:
    writer = csv.writer(csv_data_file)
    for row in reader:
        writer.writerow(row)
df = pandas.read_csv("data.csv")
df["US_peak_chart_post"] = pandas.to_numeric(df["US_peak_chart_post"], errors="ignore", downcast="integer")
df.to_json("data.json", "records")

df2 = pandas.read_csv(io.StringIO(csv_data), sep=",", skipinitialspace=True)
df2.apply(pandas.to_numeric, errors="ignore")
print(df)
df2.to_json("data2.json", "records")

with open("data.json") as data:
    print(json.load(data))

