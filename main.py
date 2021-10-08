import pandas as pd
from pandas import DataFrame


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


def main():
    data_df_wos: DataFrame = pd.read_excel("data/WoS Research Areas 2010-2020.xlsx")
    data_df_wos_ar: DataFrame = pd.read_excel("data/WoS Research Areas 2010-2020 AR.xlsx")
    result_df_wos: DataFrame = count(data_df_wos, "Category Normalized Citation Impact")
    result_df_wos_ar: DataFrame = count(data_df_wos_ar, "Category Normalized Citation Impact")
    result_df_wos.to_excel("WoS Research Areas 2010-2020 result.xlsx", index=False)
    result_df_wos_ar.to_excel("WoS Research Areas 2010-2020 AR result.xlsx", index=False)
