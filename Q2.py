
import pandas as pd
import matplotlib.pyplot as plt
import json
with open('nobelprizes.json','r') as nb:
    nodic=json.load(nb)



def report(nobelprizeDict):
    
    #
    import pandas as pd
    import matplotlib.pyplot as plt
    year=[]
    category=[]
    awarded=[]
    for i in range(len(nobelprizeDict)):
        year.append(nobelprizeDict[i]['year'])
        category.append(nobelprizeDict[i]['category'])

    for i in nobelprizeDict:
        if 'laureates' in i:
            awarded.append(True)
        else:
            awarded.append(False)
    df=pd.DataFrame({'year':year,'category':category,'awarded_or_not':awarded})
    return df



def get_laureates_and_motivation(nobelprizeDict, year, category):
    
    #
    for i in range(len(nobelprizeDict)):
        if nobelprizeDict[i]['year'] == year:
            if nobelprizeDict[i]['category'] == category:
                if 'laureates' in nobelprizeDict[i]:
                    q2_list=nobelprizeDict[i]['laureates']
                    id_list=[]
                    laureate_list=[]
                    moti_list=[]
                    for n in range(len(q2_list)):
                        id_list.append(q2_list[n]['id'])
                        if 'surname' in q2_list[n]:
                            laureate_list.append((q2_list[n]['firstname']) + ' ' + (q2_list[n]['surname']))
                        else:
                            laureate_list.append(q2_list[n]['firstname'])
                        moti_list.append(q2_list[n]['motivation'].replace('\"',''))
                    if len(nobelprizeDict[i]) == 3:
                        # float('nan'), to creat an NaN.
                        # came from:'https://m.py.cn/faq/python/12124/html'
                        df=pd.DataFrame({'category':category,'year':year,'id':id_list,'laureate':laureate_list,'motivation':moti_list,'overall_motivation':float('nan')})
                    else:
                        df=pd.DataFrame({'category':category,'year':year,'id':id_list,'laureate':laureate_list,'motivation':moti_list,'overall_motivation':nobelprizeDict[i]['overallMotivation']})
                    return df





def plot_freqs(nobelprizeDict):
    
    # open whitelist.txt first.
    with open('whitelist.txt','r') as cw:
        count_words=[each_words.strip() for each_words in cw]


    # define a function to gather motivations from a certain categories.
    def get_motivation(category):
        motivation_list=[]
        for i in nobelprizeDict:
            if i['category'] == category:
                if 'laureates' in i:
                   q2_list=i['laureates']
                   for n in range(len(q2_list)):
                       motivation_list.append(q2_list[n]['motivation'])
                for i in range(len(motivation_list)):
                    motivation_list[i]=motivation_list[i].replace('"','')
            else:
                continue
        return motivation_list
    # call this function six times so I will have six lists full of motivations from different catagories.
    # Copy 'motivation_list' to a new list because 'motivation_list' will re-define when calling the function again.
    motivation_list1=get_motivation('chemistry')
    motivation_chemistry=[]
    for i in motivation_list1:
        motivation_chemistry.extend(i.split(' '))         # separate every motivations,turn this list into a list with many many words, each element is one word.

    motivation_list2=get_motivation('economics')
    motivation_economics=[]
    for i in motivation_list2:
        motivation_economics.extend(i.split(' '))

    motivation_list3=get_motivation('literature')
    motivation_literature=[]
    for i in motivation_list3:
        motivation_literature.extend(i.split(' '))

    motivation_list4=get_motivation('peace')
    motivation_peace=[]
    for i in motivation_list4:
        motivation_peace.extend(i.split(' '))

    motivation_list5=get_motivation('physics')
    motivation_physics=[]
    for i in motivation_list5:
        motivation_physics.extend(i.split(' '))

    motivation_list6=get_motivation('medicine')
    motivation_medicine=[]
    for i in motivation_list6:
        motivation_medicine.extend(i.split(' '))

    # define another function to compare each categories' motivations with the given whitelist.txt,which had already been transfered to 'count_words'
    # 'count_list' will record every words' frequencyies using numbers only.
    def compare_words(motivation_category):
        count_list=[]
        for each_words in count_words:
                x=0
                for n in range(len(motivation_category)):
                     if each_words == motivation_category[n]:
                         x += 1
                count_list.append(x)
        return count_list
    # Call this function six times,get six lists with only numbers in them. Copy them into different catagories' counting list.
    chemistry_count=compare_words(motivation_chemistry)
    economics_count=compare_words(motivation_economics)
    literature_count=compare_words(motivation_literature)
    peace_count=compare_words(motivation_peace)
    physics_count=compare_words(motivation_physics)
    medicine_count=compare_words(motivation_medicine)


    # Combine words and their frequency into a pandas dataframe, then sort them reversely and slice 1st,10th,20th,30th,40th and 50th words and their frequencies.
    df_chemistry=pd.DataFrame({'words':count_words,'frequency':chemistry_count}).sort_values(by='frequency',ascending=False)
    df_chemistry=pd.concat([df_chemistry.iloc[:1,:],df_chemistry.iloc[9:50:10,:]])

    df_economics=pd.DataFrame({'words':count_words,'frequency':economics_count}).sort_values(by='frequency',ascending=False)
    df_economics=pd.concat([df_economics.iloc[:1,:],df_economics.iloc[9:50:10,:]])

    df_literature=pd.DataFrame({'words':count_words,'frequency':literature_count}).sort_values(by='frequency',ascending=False)
    df_literature=pd.concat([df_literature.iloc[:1,:],df_literature.iloc[9:50:10,:]])

    df_peace=pd.DataFrame({'words':count_words,'frequency':peace_count}).sort_values(by='frequency',ascending=False)
    df_peace=pd.concat([df_peace.iloc[:1,:],df_peace.iloc[9:50:10,:]])

    df_physics=pd.DataFrame({'words':count_words,'frequency':physics_count}).sort_values(by='frequency',ascending=False)
    df_physics=pd.concat([df_physics.iloc[:1,:],df_physics.iloc[9:50:10,:]])

    df_medicine=pd.DataFrame({'words':count_words,'frequency':medicine_count}).sort_values(by='frequency',ascending=False)
    df_medicine=pd.concat([df_medicine.iloc[:1,:],df_medicine.iloc[9:50:10,:]])



    # Creat a subplot which has six plots.
    sub=plt.figure(figsize=(15,12))
    sub.suptitle('words frequency',fontsize=13)
    sub.add_subplot(321)
    plt1,=plt.plot(df_chemistry['words'],df_chemistry['frequency'],'.y')
    # Show exact frequency number in the plot
    # taken from: 'https://blog.csdn.net/u012063773/article/details/79357139'
    # I made some modifications so it would work here nicely.
    for a,b in zip(df_chemistry['words'],df_chemistry['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    # end of referenced code
    plt.title('chemistry',fontsize=10,color='y')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])
    sub.add_subplot(322)
    plt2,=plt.plot(df_economics['words'],df_economics['frequency'],'xm')
    for a,b in zip(df_economics['words'],df_economics['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    plt.title('economics',fontsize=10,color='m')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])
    sub.add_subplot(323)
    plt3,=plt.plot(df_literature['words'],df_literature['frequency'],'*r')
    for a,b in zip(df_literature['words'],df_literature['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    plt.title('literature',fontsize=10,color='r')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])
    sub.add_subplot(324)
    plt4,=plt.plot(df_peace['words'],df_peace['frequency'],'.k')
    for a,b in zip(df_peace['words'],df_peace['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    plt.title('peace',fontsize=10,color='k')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])
    sub.add_subplot(325)
    plt5,=plt.plot(df_physics['words'],df_physics['frequency'],'xb')
    for a,b in zip(df_physics['words'],df_physics['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    plt.title('physics',fontsize=10,color='b')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])
    sub.add_subplot(326)
    plt6,=plt.plot(df_medicine['words'],df_medicine['frequency'],'*c')
    for a,b in zip(df_medicine['words'],df_medicine['frequency']):
        plt.text(a,b+0.7,'%.0f' %b, ha='center', va='bottom',fontsize=12)
    plt.title('medicine',fontsize=10,color='c')
    plt.xticks(rotation= -45)
    plt.ylim([0,145])

    sub.legend( handles = [plt1,plt2,plt3,plt4,plt5,plt6], labels = ['chemistry','economics','literature','peace','physics','medicine'],loc='East', fontsize=13)
    plt.subplots_adjust(hspace=0.58)
    plt.show()


print(report(nodic))
print(get_laureates_and_motivation(nodic,'2010','chemistry'))
print(get_laureates_and_motivation(nodic,'1967','medicine'))
print(get_laureates_and_motivation(nodic,'1973','literature'))
print(get_laureates_and_motivation(nodic,'1937','physics'))
print(plot_freqs(nodic))
