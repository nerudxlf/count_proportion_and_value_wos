import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from mpldatacursor import datacursor


def count(data: DataFrame, field: str) -> DataFrame:
    research_area_list: list = data["Research Area"].to_list()
    field_list: list = data[field].to_list()

    proportion_dict: dict = {}
    value_dict: dict = {}

    for i in range(len(research_area_list)):
        research_area_split = research_area_list[i].split("; ")
        for area in research_area_split:
            if not (proportion_dict.get(area) is None):
                proportion_dict[area] += field_list[i]
                value_dict[area] += 1
            else:
                proportion_dict[area] = field_list[i]
                value_dict[area] = 1
    result_df: DataFrame = pd.DataFrame({"Research Area": proportion_dict.keys(), "Sum": proportion_dict.values(),
                                         "Values": value_dict.values()})
    result_df[field] = result_df["Sum"] / result_df["Values"]
    return result_df


def plot_info(data: DataFrame) -> None:
    x = data["Values"].to_list()
    y = data["Category Normalized Citation Impact"].to_list()
    name = data["Research Area"].to_list()
    plt.plot()
    ax = plt.gca()
    for i in range(len(data)):
        ax.scatter(x[i], y[i], label=name[i])
    datacursor(formatter='{label}'.format)
    plt.plot([0, max(x)], [1, 1])
    plt.plot([100, 100], [0, max(y)])
    plt.show()


def main():
    data_df_wos: DataFrame = pd.read_excel("data/WoS Research Areas 2010-2020.xlsx")
    data_df_wos_ar: DataFrame = pd.read_excel("data/WoS Research Areas 2010-2020 AR.xlsx")
    result_df_wos: DataFrame = count(data_df_wos, "Category Normalized Citation Impact")
    result_df_wos_ar: DataFrame = count(data_df_wos_ar, "Category Normalized Citation Impact")
    plot_info(result_df_wos_ar)
    result_df_wos.to_excel("WoS Research Areas 2010-2020 result.xlsx", index=False)
    result_df_wos_ar.to_excel("WoS Research Areas 2010-2020 AR result.xlsx", index=False)
