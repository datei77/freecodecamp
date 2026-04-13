import pandas as pd

def calculate_demographic_data(print_data=True):
  
    df = pd.read_csv('adult.data.csv')
    race_cnt = df['race'].value_counts()
    avg_age_m= round(df[df['sex'] == 'Male']['age'].mean(), 1)
    tot_ppl = len(df)
    bachelors_cnt = (df['education'] == 'Bachelors').sum()
    perc_bachelors = round((bachelors_cnt / tot_ppl) * 100, 1)
    adv_degree = ['Bachelors', 'Masters', 'Doctorate']
    hi_edu = df[df['education'].isin(adv_degree)]
    lo_edu = df[~df['education'].isin(adv_degree)]
    hi_edu_rich = hi_edu[hi_edu['salary'] == '>50K']
  
    if len(hi_edu) > 0:
        hi_education_rich = round((len(hi_edu_rich) / len(hi_edu)) * 100, 1)
    else:
        hi_education_rich = 0.0

    lo_edu_rich = lo_edu[lo_edu['salary'] == '>50K']
  
    if len(lo_edu) > 0:
        lo_education_rich = round((len(lo_edu_rich) / len(lo_edu)) * 100, 1)
    else:
        lo_education_rich = 0.0

    min_hrs = int(df['hours-per-week'].min())
    min_work = df[df['hours-per-week'] == min_hrs]
  
    if len(min_work) > 0:
        rich_min_work = min_work[min_work['salary'] == '>50K']
        rich_percentage_min_work = round((len(rich_min_work) / len(min_work)) * 100, 1)
    else:
        rich_percentage_min_work = 0.0

    country_cnt = df['native-country'].value_counts()
    country_rich_cnt = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_perc = (country_rich_cnt / country_cnt).fillna(0) * 100

    if not country_rich_perc.empty:
        hi_earn_country = country_rich_perc.idxmax()
        hi_earn_country_perc = round(country_rich_perc.max(), 1)
    else:
        hi_earn_country = None
        hi_earn_country_perc = 0.0

   india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]

    if not india_rich.empty:
        top_in_occ = india_rich['occupation'].value_counts().idxmax()
    else:
        top_in_occ = None

   if print_data:
        print("Number of each race:\n", race_cnt, "\n")
        print("Average age of men:", avg_age_men, "\n")
        print("Percentage with Bachelors degrees:", perc_bachelors, "%\n")
        print("Percentage with higher education that earn >50K:", hi_education_rich, "%\n")
        print("Percentage without higher education that earn >50K:", lo_education_rich, "%\n")
        print("Min work time (hours/week):", min_hrs, "\n")
        print("Percentage of rich among those who work fewest hours:", rich_percentage_min_work, "%\n")
        print("Country with highest percentage of rich:", hi_earn_country, "\n")
        print("Highest percentage of rich people in country:", hi_earn_country_perc, "%\n")
        print("Top occupation in India for those who earn >50K:", top_in_occ, "\n")

    results = 
    {
        'race_cnt': race_cnt,
        'avg_age_men': avg_age_men,
        'perc_bachelors': perc_bachelors,
        'hi_education_rich': hi_education_rich,
        'lo_education_rich': lo_education_rich,
        'min_hrs': min_hrs,
        'rich_percentage_min_work': rich_percentage_min_work,
        'hi_earn_country': hi_earn_country,
        'hi_earn_country_perc': hi_earn_country_perc,
        'top_in_occ': top_in_occ
    }
    return results

if __name__ == '__main__':
    calculate_demographic_data(print_data=True)
