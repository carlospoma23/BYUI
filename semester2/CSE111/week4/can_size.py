import math
import ast

def main():

    st_can_size_1={'Name':'#1 Picnic','Radius':6.83,'Height':10.16,'Cost':0.28}
    st_can_size_2={'Name':'#1 Tall','Radius':7.78,'Height':11.91,'Cost':0.43}
    st_can_size_3={'Name':'#2','Radius':8.73,'Height':11.59,'Cost':0.45}
    st_can_size_4={'Name':'#2.5','Radius':10.32,'Height':11.91,'Cost':0.61}
    st_can_size_5={'Name':'#3 Cylinder','Radius':10.79,'Height':17.78,'Cost':0.86}
    st_can_size_6={'Name':'#5','Radius':13.02,'Height':14.29,'Cost':0.83}
    st_can_size_7={'Name':'#6Z','Radius':5.40,'Height':8.89,'Cost':0.22}
    st_can_size_8={'Name':'8Z Short','Radius':6.83,'Height':7.62,'Cost':0.26}
    st_can_size_9={'Name':'#10','Radius':15.72,'Height':17.78,'Cost':1.53}
    st_can_size_10={'Name':'#211','Radius':6.83,'Height':12.38,'Cost':0.34}
    st_can_size_11={'Name':'#300','Radius':7.62,'Height':11.27,'Cost':0.38}
    st_can_size_12={'Name':'#303','Radius':8.10,'Height':11.11,'Cost':0.42}
     
    list_st_can_size=[st_can_size_1,st_can_size_2,st_can_size_3,st_can_size_4,st_can_size_5,st_can_size_6,st_can_size_7,st_can_size_8,st_can_size_9,st_can_size_10,st_can_size_11,st_can_size_12]

    #showing the results - - Output
   
    max_store_eff=-1
    max_cost_eff=-1
    print()
    print("Name Steel Can ", "Storage Efficiency ", " Cost Efficiency")
    print()
    for i in list_st_can_size:
       
        store_eff=compute_storage_efficiency(i)
        cost_eff=compute_cost_efficiency(i)
        print(f"{i['Name']:15}        {store_eff:.2f}            ${cost_eff:.2f}")

        if store_eff>max_store_eff:
            best_store=i['Name']
            max_store_eff=store_eff
        
        if cost_eff > max_cost_eff:
            best_cost = i['Name']
            max_cost_eff = cost_eff
    
    print()
    print("************************************************")
    print('Best can size in storage efficiency:',best_store)
    print('Best can size in cost efficiency::',best_cost)
    
    
def compute_volume(dic):

    r=float(dic['Radius'])
    h=float(dic['Height'])
    vol=math.pi*r*r*h
    return vol

def compute_surface_area(dic):
    r=float(dic['Radius'])
    h=float(dic['Height'])
    area=(2*math.pi*r)*(r+h)
    return area


def compute_storage_efficiency(dic):
    v=compute_volume(dic)
    a=compute_surface_area(dic)
    str_eff=v/a
    return str_eff

def compute_cost_efficiency(dic):
    v=compute_volume(dic)
    cost_efficiency=v/(float(dic['Cost']))

    return cost_efficiency

main()