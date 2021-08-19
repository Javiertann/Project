# Importing of required modules
import pandas as pd
import matplotlib.pyplot as pt
import numpy as np

class stats:

    topCountryName = ""

    def __init__(self):
        self.countries = pd.read_excel(r"Project_File.xlsx")

    def getTopCountry(self):
        countries = pd.read_excel(r"Project_File.xlsx")
        countries = countries.iloc[:, lambda countries: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        countries = countries.replace("na", 0)
        asia = countries.set_index("Unnamed: 0")
        asia = asia.loc["2008 Jan":"2017 Nov"]
        sums = asia.sum(axis=0)
        sums = sums.sort_values(ascending=False)
        top1 = sums.index[0]
        Sum1 = sums[top1]
        print(Sum1)

        return asia["Indonesia"].sum()

    def top3(self):
        countries = self.countries
        countries = countries.iloc[:,lambda countries:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        countries = countries.replace("na", 0)
        asia = countries.set_index("Unnamed: 0")
        asia = asia.loc["2008 Jan":"2017 Nov"]

        sums = asia.sum(axis=0)
        sums = sums.sort_values(ascending = False)
        print()
        print()
        print(sums, "\n")
        top1 = sums.index[0]
        top2 = sums.index[1]
        top3 = sums.index[2]
        print("The top 3 countries with the most visitors in Asia are: ", top1, ",", top2, ",", top3, "\n")

        amount1 = sums[top1]
        amount2 = sums[top2]
        amount3 = sums[top3]
        print("The amount of visitors from the top 3 countries are", amount1, ",", amount2, ",", amount3, "respectively.", "\n")

        means = asia.mean(axis = 0)
        means = means.sort_values(ascending = False)
        print(means)
        mean1 = round(means[0], 2)
        mean2 = round(means[1], 2)
        mean3 = round(means[2], 2)
        print("The mean amount of visitors from the top 3 countries are", round(mean1), ",", round(mean2), ",", round(mean3), "respectively. (Rounded to nearest whole number)", "\n")

        medians = asia.median(axis = 0)
        medians = medians.sort_values(ascending = False)
        print(medians)
        median1 = medians[0]
        median2 = medians[1]
        median3 = medians[2]
        print("The median amount of visitors from the top 3 countries are", round(median1), ", ", round(median2), ", ", round(median3), "respectively. (Rounded to nearest whole number)")

    def bottom3(self):
        countries = self.countries
        countries = countries.iloc[:,lambda countries:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        countries = countries.replace("na", 0)
        asia = countries.set_index("Unnamed: 0")
        asia = asia.loc["2008 Jan":"2017 Nov"]
        sums = asia.sum(axis = 0)
        sums = sums.sort_values(ascending = True)
        print()
        print()
        print()
        print(sums, "\n")
        top1 = sums.index[0]
        top2 = sums.index[1]
        top3 = sums.index[2]
        print("The top 3 countries with the least visitors in Europe are: ", top1, ",", top2, ",", top3, "\n")

        amount1 = sums[top1]
        amount2 = sums[top2]
        amount3 = sums[top3]
        print("The amount of visitors from the bottom 3 countries are", amount1, ",", amount2, ",", amount3, "respectively.", "\n")

        means = asia.mean(axis = 0)
        means = means.sort_values(ascending = True)
        print(means)
        mean1 = round(means[0], 2)
        mean2 = round(means[1], 2)
        mean3 = round(means[2], 2)
        print("The mean amount of visitors from the bottom 3 countries are", round(mean1), ",", round(mean2), ",", round(mean3), "respectively. (Rounded to nearest whole number)", "\n")

        medians = asia.median(axis = 0)
        medians = medians.sort_values(ascending = True)
        print(medians)
        median1 = medians[0]
        median2 = medians[1]
        median3 = medians[2]
        print("The median amount of visitors from the bottom 3 countries are", round(median1), ", ", round(median2), ", ", round(median3), "respectively. (Rounded to nearest whole number)", "\n")

    def plotGraphs(self):
        countries = self.countries
        countries = countries.iloc[:,lambda countries:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
        countries = countries.replace("na", 0)
        asia = countries.set_index("Unnamed: 0")
        asia = asia.loc["2008 Jan":"2017 Nov"]
        date_sum = asia.sum(axis = 1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        for j in range(0,12):
            for i in np.arange(j,118,12):
                months[j] += date_sum.iat[i]
        pt.plot(month_names,months)
        pt.title("Visitors from all countries each month in each year")
        pt.show()

        date_sum = asia.mean(axis = 1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        for j in range(0,12):
            for i in np.arange(j,118,12):
                months[j] += date_sum.iat[i]
        pt.plot(month_names,months)
        pt.title("Mean visitors from all countries each month in each year")
        pt.show()

        date_sum = asia.median(axis = 1)
        months = np.zeros((12,), dtype=int).tolist()
        month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        for j in range(0,12):
            for i in np.arange(j,118,12):
                months[j] += date_sum.iat[i]
        pt.plot(month_names,months)
        pt.title("Median visitors from all countries each month in each year")
        pt.show()

Stats = stats()
Stats.top3()
Stats.bottom3()
Stats.plotGraphs()

