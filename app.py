from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import logging
import sys
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('C:/Users/Surya/Desktop/Harschil/KNR deployed model/KNR.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Hole_Depth_feet=float(request.form['Hole Depth (feet)'])
        Bit_Depth_feet=float(request.form['Bit Depth (feet)'])
        Rate_Of_Penetration_ft_per_hr=float(request.form['Rate Of Penetration (ft_per_hr)'])
        Weight_on_Bit_klbs=float(request.form['Weight on Bit (klbs)'])
        Differential_Pressure_psi=float(request.form['Differential Pressure (psi)'])
        Rotary_RPM_RPM=float(request.form['Rotary RPM (RPM)'])
        Standpipe_Pressure_psi=float(request.form['Standpipe Pressure (psi)'])
        Hook_Load_klbs=float(request.form['Hook Load (klbs)'])
        Flow_flow_percent=float(request.form['Flow (flow_percent)'])
        Pason_Lag_Depth_feet=float(request.form['Pason Lag Depth (feet)'])
        Third_Party_Gas_percent=float(request.form['Third Party Gas (percent)'])
        WITS_Lag_Depth_feet=float(request.form['WITS Lag Depth (feet)'])
        Total_Mud_Volume_barrels=float(request.form['Total Mud Volume (barrels)'])
        Block_Height_feet=float(request.form['Block Height (feet)'])
        Gamma_api=float(request.form['Gamma (api)'])
        Gamma_Depth_feet=float(request.form['Gamma Depth (feet)'])
        Pump_1_strokes_per_min_SPM=float(request.form['Pump 1 strokes/min (SPM)'])
        On_Bottom_Hours_hrs=float(request.form['On Bottom Hours (hrs)'])
        Over_Pull_klbs=float(request.form['Over Pull (klbs)'])
        Pump_2_strokes_per_min_SPM=float(request.form['Pump 2 strokes/min (SPM)'])
        Tool_Face_degrees=float(request.form['Tool Face (degrees)'])
        Gravity_Toolface_degrees=float(request.form['Gravity Toolface (degrees)'])
        Magnetic_Toolface_degrees=float(request.form['Magnetic Toolface (degrees)'])
        AMAP_Info_1_unitless=float(request.form['AMAP Info 1 (unitless)'])
        AMAP_Mode_unitless=float(request.form['AMAP Mode (unitless)'])
        Azimuth_degrees=float(request.form['Azimuth (degrees)'])
        Bit_RPM_RPM=float(request.form['Bit RPM (RPM)'])
        Convertible_Torque_kft_lb=float(request.form['Convertible Torque (kft_lb)'])


        prediction=model.predict([[Hole_Depth_feet, Bit_Depth_feet, Rate_Of_Penetration_ft_per_hr, Weight_on_Bit_klbs, Differential_Pressure_psi, Rotary_RPM_RPM, Standpipe_Pressure_psi, Hook_Load_klbs, Flow_flow_percent, Pason_Lag_Depth_feet, Third_Party_Gas_percent, WITS_Lag_Depth_feet, Total_Mud_Volume_barrels, Block_Height_feet, Gamma_api, Gamma_Depth_feet, Pump_1_strokes_per_min_SPM, On_Bottom_Hours_hrs, Over_Pull_klbs, Pump_2_strokes_per_min_SPM, Tool_Face_degrees, Gravity_Toolface_degrees, Magnetic_Toolface_degrees, AMAP_Info_1_unitless, AMAP_Mode_unitless, Azimuth_degrees, Bit_RPM_RPM, Convertible_Torque_kft_lb]])
        output=(prediction)

        return render_template('index.html',prediction_text="The predicted Total Pump Output (gal_per_min) is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

