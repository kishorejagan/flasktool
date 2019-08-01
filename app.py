import flask


from sqlalchemy import create_engine

import json
import os
import pandas as pd

# Defining input variables with input values from nigel file
BaseSupport = 3635.64
TeacherCompAmount = 3681.09
TeacherCompPercent = 1.25
Amount200DayCalender = 3817.42
Percent200DayCalender = 5
TeacherCompAnd200DayCalender = 3865.14
FullDayKindergarten10 = 0
GroupABasePSD = 1
GroupAGradeLevelPSD = 0
GroupAPSD = 0.45
GroupAFinalGroupAWeightsPSD = 1.45
GroupABaseK_8 = 1
GroupAGradeLevelK_8 = 0
GroupAK_8 = 0.158
GroupAFinalGroupAWeightsK_8 = 1.158
GroupABase9_12 = 1
GroupAGradeLevel9_12 = 0.163
GroupA9_12 = 0.105
GroupAFinalGroupAWeights9_12 = 1.268
GroupABaseJTED = 1
GroupAGradeLevelJTED = 0.339
GroupAJTED = 0
GroupAFinalGroupAWeightsJTED = 1.339
WtSmallIso1to99K_8 = 1.559
WtSmallIso100to499K_8 = 1.358
WtSmallIso500to599K_8 = 1.158
WtSmallIso600AndOverK_8 = 0
WtSmall1to99K_8 = 1.399
WtSmall100to499K_8 = 1.278
WtSmall500to599K_8 = 1.158
WtSmall600AndOverK_8 = 0
WtSmallIso1to999_12 = 1.669
WtSmallIso100to4999_12 = 1.468
WtSmallIso500to5999_12 = 1.268
WtSmallIso600AndOver9_12 = 0
WtSmall1to999_12 = 1.559
WtSmall100to4999_12 = 1.398
WtSmall500to5999_12 = 1.268
WtSmall600AndOver9_12 = 0
IncWtSmallIso1to99K_8 = 0
IncWtSmallIso100to499K_8 = 0.0005
IncWtSmallIso500to599K_8 = 0.002
IncWtSmallIso600AndOverK_8 = 0
IncWtSmall1to99K_8 = 0
IncWtSmall100to499K_8 = 0.0003
IncWtSmall500to599K_8 = 0.0012
IncWtSmall600AndOverK_8 = 0
IncWtSmallIso1to999_12 = 0
IncWtSmallIso100to4999_12 = 0.0005
IncWtSmallIso500to5999_12 = 0.002
IncWtSmallIso600AndOver9_12 = 0
IncWtSmall1to999_12 = 0
IncWtSmall100to4999_12 = 0.0004
IncWtSmall500to5999_12 = 0.0013
IncWtSmall600AndOver9_12 = 0
GroupB1 = 0.003
GroupB2 = 0.040
GroupB3 = 0.060
GroupB4 = 0.115
GroupB5 = 3.158
GroupB6 = 3.595
GroupB7 = 4.421
GroupB8 = 4.771
GroupB9 = 4.806
GroupB10 = 4.822
GroupB11 = 5.833
GroupB12 = 6.024
GroupB13 = 6.773
GroupB14 = 7.947
PolicyOption1 = 0
TEI10 = 1
FullTimeAOI = 0.95
HalfTimeAOI = 0.85
Transportation123TSL = 1
TransportationPerPupilOptionTRCL = 0
DistSuppLvlAllPSD = 450.76
DistSuppLvl1to99K_8 = 544.58
DistSuppLvl100to599K_8 = 389.25
DistSuppLvl600AndOverK_8 = 450.76
DistSuppLvl1to999_12 = 601.24
DistSuppLvl100to5999_12 = 405.59
DistSuppLvl600AndOver9_12 = 492.94
CharSuppLvlAllK_8 = 1752.1
CharSuppLvlAll9_12 = 2042.04
DistHSTxtBkAllPSD = 0
DistHSTxtBk1to99K_8 = 0
DistHSTxtBk100to599K_8 = 0
DistHSTxtBk600AndOverK_8 = 0
DistHSTxtBk1to999_12 = 69.68
DistHSTxtBk100to5999_12 = 69.68
DistHSTxtBk600AndOver9_12 = 69.68
CharHSTxtBkAllK_8 = 0
CharHSTxtBkAll9_12 = 0
Reduction10 = 1
AdditionalAssistant_eqformula = 2
DistrictReduction = 352442700
ActualDistrictReduction = -381355874.7
CharterReduction = 18656000
AvgDistrictPPReduction = 382.77165
AvgActualDistReduction = -414.1729064
AvgCharterPPReduction = 109.6679608
AdditonalAssistantReduction = 1
QTRK_8 = 2.0793
QTR9_12 = 2.0793
QTRUnified = 4.1586
QTRJTED = 0.05


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, float):
            return float(obj)
        return super(CustomJsonEncoder, self).default(obj)


app = flask.Flask(__name__)
app.secret_key = 'asfmasgma'
app._static_folder = os.path.abspath("C:/Users/jjoth/PycharmProjects/untitled1/templates/static/")
# ESHTABLISHING CONNECTION
engine = create_engine(
    'mysql+pymysql://DCEdExUser1:DCEdExUser1@dcedex.cgnkf5ysjn5z.us-west-1.rds.amazonaws.com/DCSchoolFinance')


@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    ll = 0
    usercheck = engine.execute('Select * from userLogin')
    for i in usercheck:
        if flask.request.form['password'] == i[1] and flask.request.form['username'] == i[0]:
            ll += 1
            flask.session['username'] = flask.request.form['username']
            flask.session['password'] = flask.request.form['password']
            return wftf()
    if ll == 0:
        error = 'Invalid Credentials. Please try again.'
        return flask.render_template("login.html", error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask.session['username'] = None
    flask.session['password'] = None

    return flask.render_template('login.html')


# CALCULATION OF VALUES
@app.route('/wftf', methods=['GET', 'POST'])
def wftf():
    # ASSIGNING VARIABLES FOR CALCULATION
    # DEFINING VARIABLES FOR FURTHER CALCULATION
    sumprekadm={}
    sumelemadm={}
    sumhsadm={}
    Final_9_12SmWgt=[]
    Final_K_8SmWgt=[]
    AuditBaseLevelAdjustment=[]
    ddd = 0
    FinalFormulaAdditionalAssistance=[]
    FinalAAAllocation=[]
    EID=[]
    Ename=[]
    D=[]
    BSL=[]
    TEI=[]
    LEABaseLevel=[]
    WeightedElemCounts=[]
    WeightedHSCounts=[]
    GroupBWeightedAddonCounts=[]
    ElemBaseWeight=[]
    HSBaseWeight=[]
    GroupBBSL=[]
    WeightedPreKCounts=[]
    GB1_EDMIDSLD=[]
    GB2_K3Reading=[]
    GB3_K3=[]
    GB4_ELL=[]
    GB5_OI_R=[]
    GB6_PS_D=[]
    GB7_MOID=[]
    GB8_HI=[]
    GB9_VI=[]
    GB10_ED_P=[]
    GB11_MDSC=[]
    GB12_MD_R=[]
    GB13_OI_SC=[]
    GB14_MD_SSI=[]
    AC1=[]
    AH=[]
    AI=[]
    Weighted_GB1_EDMIDSLD=[]
    Weighted_GB2_K3Reading=[]
    Weighted_GB3_K3=[]
    Weighted_=[]
    Weighted_GB5_OI_R=[]
    Weighted_GB6_PS_D=[]
    Weighted_GB7_MOID=[]
    Weighted_GB8_HI=[]
    Weighted_GB9_VI=[]
    Weighted_GB10_ED_P=[]
    Weighted_GB11_MDSC=[]
    Weighted_GB12_MD_R=[]
    Weighted_GB13_OI_SC=[]
    Weighted_GB14_MD_SSI=[]
    PreKWeightedPupilsuser_specifiedSWWreduction=[]
    K_8WeightedPupilsuser_specifiedSWWreduction=[]
    nine_12WeightedPupilsuser_specifiedSWWreduction=[]
    PercPreK_8ofTotal=[]
    PercHSofTotal=[]
    AB2=[]
    AC2=[]
    ElemAssessedValuation=[]
    ElemTotalStateFormula=[]
    HSTotalStateFormula=[]
    HSAssessedValuation=[]
    ElemQTRYield=[]
    HSQTRYield=[]
    HSLL=[]
    ElemLL=[]
    TotalLocalLevy=[]
    ElemStateAid=[]
    HSStateAid=[]
    TotalStateAid=[]
    ElemNoStateAidDistrict = []
    HSNoStateAidDistrict = []
    NoStateAidDistrict = []
    TotalQTRYield = []
    UncapturedQTR = []
    TotalStateFundingEqualised = []
    SSWELEMINCREMENTALWEIGHTPP = []
    SSWHSINCREMENTALWEIGHTPP = []
    fDK = 0
    PREKADM=[]
    PrekBSL=[]
    HSADM=[]
    ELEMADM=[]
    ELEMBSL=[]
    HSBSL=[]
    sixtyseven= 67
    CharterElemAA= {}
    CharterHSAA = {}
    CharterElemADM=[]
    CharterHSADM=[]
    LEApercentofCharterElemADM = []
    LEApercentofCharterHSADM = []
    K_8PercentofTotalcharterAA = []
    TotalCharterElemReduction = []
    TotalCharterHSReduction = []
    CharterElemAAReduction = []
    CharterHSAAReduction = []
    TotalNetCharterAA = []
    DistrictHSTextbooksAA = []
    DistrictHSAA = []
    DistrictElemAA = []
    DistrictPreKAA = []
    TotalFormulaDistrictAA = []
    DistrictPreKElemReduction = []
    DistrictHSReduction = []
    TotalDistrictAAReduction = []
    TotalNetDistrictAA = []
    NetworkElemADM = []
    NetworkHSADM = []
    sumofnetworkelemadm = {}
    sumofnetworkhsadm = {}
    FinalFormulaAAwithReduction = []
    AdditionalAssistance = []
    HSRange = []
    ELEMRange = []
    TotalStateEqualisationFunding = []
    OppurtunityWeight = []
    TRCL = []
    TSL = []
    RCL = []
    DSL = []
    TeacherComp = []
    twohundereddaycalendar = []
    techercompand200daycalender = []
    SumofPreKWeightedPupilsuser_specifiedSWWreduction = {}
    Sumofk_8WeightedPupilsuser_specifiedSWWreduction = {}
    Sumof9_12WeightedPupilsuser_specifiedSWWreduction = {}
    sumCharterElemADM={}
    sumCharterHSADM={}
    BSLWithoutAdjustment=[]
    SumofBSL={}
    # STORE THE NETWORK NAMES
    parentorg = engine.execute('select distinct (ParentOrganization) from ChartersWithNetwork')
    for row2 in parentorg:
        d2 = row2[0]
        if d2 != '':
            sumofnetworkelemadm[d2]=0
            sumofnetworkhsadm[d2]=0
    count = 0
    # CALCULATION OF ADM VALUES
    preresult = engine.execute('select truck.*,lorry.PsdCapOutlayRevLimitAmt,lorry.ElemCapOutlayRevLimitAmt,lorry.HsPrlmCapOutlayRevLimitAmt,lorry.HsBooksCapOutlayRevLimitAmt,lorry.PSElTransAdj,lorry.HSTransAdj from (select kvs.*, CSH.parentOrganization, CSH.NetworkForFundingPurposes, CSH.ESSmallIsolated, CSH.HSSmallIsolated from (select ftfmaintype.*,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (Select ftfmain.*,EntityName,Entityshort.County,Entityshort.Type from (select EntityID,sum(PsdCount) as sumOfPsdCount,sum(ElemCount) as sumOfElemCount,sum(DSCSElemCnt) as sumOfDSCSElemCount,sum(HsCount) as sumOfHsCount, sum(DSCSHsCnt) as sumOfDSCSHsCount, FiscalYear,TEI,BaseAmount as MaxOfBaseAmount,BaseAdjsAmount as MaxofBaseAdjsAmount, sum(MDSSICnt) as sumOfMDSSICnt, sum(DSCSMDSSICnt)as sumOfDSCSMDSSICnt, sum(DSCSVICnt)as sumOfDSCSVICnt, sum(DSCSOISCCnt) as sumOfDSCSOISCCnt, sum(DSCSPSDCnt)as sumOfDSCSPSDCnt, sum(DSCSMDSCCnt)as sumOfDSCSMDSCCnt, sum(DSCSHICnt)as sumOfDSCSHICnt, sum(DSCSMOMRCnt)as sumOfDSCSMOMRCnt, sum(DSCSEDPPrivateCnt)as sumOfDSCSEDPPrivateCnt, sum(DSCSMDResCnt)as sumOfDSCSMDResCnt, sum(DSCSOIResCnt)as sumOfDSCSOIResCnt, sum(DSCSEDMIMRCnt)as sumOfDSCSEDMIMRCnt, sum(DSCSLEPCnt)as sumOfDSCSLEPCnt, sum(DSCSK3Cnt)as SumOfDSCSK3Cnt, sum(PSDCnt)as sumOfPSDCnt, sum(VICnt)as sumOfVICnt, sum(OISCCnt)as sumOfOISCCnt, sum(MDSCCnt)as sumOfMDSCCnt, sum(HICnt)as sumOfHICnt, sum(MOMRCnt)as sumOfMOMRCnt, sum(EDPPrivateCnt)as sumOfEDPPrivateCnt, sum(MDResCnt)as sumOfMDResCnt, sum(OIResCnt)as sumOfOIResCnt, sum(EDMIMRCnt)as sumOfEDMIMRCnt, sum(LEPCnt)as sumOfLEPCnt, sum(K3Cnt)as sumOfK3Cnt, FTFStatus from ((select t.EntityID,t.FiscalYear,t.PsdCount,t.ElemCount,t.DSCSElemCnt,t.HsCount,t.DSCSHsCnt,t.DSCSK3Cnt,t.TEI,t.PaymentMonth,t.FTFStatus,t.BaseAmount,t.BaseAdjsAmount,t.MDSSICnt,t.DSCSMDSSICnt, t.DSCSVICnt,t.DSCSOISCCnt,t.DSCSPSDCnt,t.DSCSMDSCCnt,t.DSCSHICnt,t.DSCSMOMRCnt,t.DSCSEDPPrivateCnt,t.DSCSMDResCnt,t.DSCSOIResCnt,t.DSCSEDMIMRCnt,t.DSCSLEPCnt,t.PSDCnt,t.VICnt,t.OISCCnt, t.MDSCCnt,t.HICnt,t.MOMRCnt,t.EDPPrivateCnt,t.MDResCnt,t.OIResCnt,t.EDMIMRCnt,t.LEPCnt,t.K3Cnt from SaAporBaseSupportLevelCalcs1 t inner join (select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporBaseSupportLevelCalcs1 group by EntityID) tm on t.EntityID=tm.EntityID and t.PaymentMonth=tm.MaxPaymentMonth) union all select EntityID,FiscalYear,PsdCount,ElemCount,DSCSElemCnt,HsCount,DSCSHsCnt,DSCSK3Cnt,TEI,PaymentMonth,FTFStatus,BaseAmount,BaseAdjsAmount, MDSSICnt,DSCSMDSSICnt, DSCSVICnt,DSCSOISCCnt,DSCSPSDCnt,DSCSMDSCCnt,DSCSHICnt,DSCSMOMRCnt,DSCSEDPPrivateCnt,DSCSMDResCnt,DSCSOIResCnt,DSCSEDMIMRCnt,DSCSLEPCnt,PSDCnt,VICnt,OISCCnt, MDSCCnt,HICnt,MOMRCnt,EDPPrivateCnt,MDResCnt,OIResCnt,EDMIMRCnt,LEPCnt,K3Cnt from SaCharBaseSupportLevelCalcs1 where PaymentMonth=13)uni where FiscalYear=2017 group by EntityID,FTFStatus )ftfmain left join (select EntityID,EntityName,County,Entity.Type from Entity)Entityshort on ftfmain.EntityID=Entityshort.EntityID )ftfmaintype left join (select TRCLTSL.EntityID,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (select TRCL.EntityID,TRCL,TSL from ((select j.EntityID,j.TRCL from SaAporTransRevCtlLimit j inner join ( select EntityID,max(PaymentMonth)as MaxPaymentMonth from SaAporTransRevCtlLimit group by EntityID) jm on j.EntityID=jm.EntityID and j.PaymentMonth=jm.MaxPaymentMonth and FiscalYear=2017))TRCL left join ((select k.EntityID,k.TSL from SaAporTransSupptLvl k inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporTransSupptLvl group by EntityID)km where k.EntityID=km.EntityID and k.PaymentMonth=km.MaxPaymentMonth and k.FiscalYear=2017))TSL on TRCL.EntityID=TSL.EntityID)TRCLTSL left join ((Select l.EntityID,l.TotalPSElAssessValAmt,l.TotalHSAssessValAmt from SaAporQualLevy l inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporQualLevy group by EntityID)lm where l.EntityID=lm.EntityID and l.PaymentMonth=lm.MaxPaymentMonth and l.FiscalYear=2017))PSEl on TRCLTSL.EntityID=PSEl.EntityID )Bike on ftfmaintype.EntityID=Bike.EntityID) kvs left join (select CWN.EntityID, CWN.EntityName, CWN.parentOrganization, CWN.NetworkForFundingPurposes, ESSmallIsolated, HSSmallIsolated from (select EntityID, ChartersWithNetwork.OrganizationName as EntityName, ParentOrganization, ifnull(Charters4Funding.NetworkForFundingPurposes,0) as NetworkForFundingPurposes  from ChartersWithNetwork left join Charters4Funding on ChartersWithNetwork.ParentOrganization = Charters4Funding.OrganizationName) CWN left join SmallIsolatedList on CWN.EntityID = SmallIsolatedList.EntityID)CSH on kvs.EntityID = CSH.EntityID)truck left join(select car1.EntityID,PsdCapOutlayRevLimitAmt,ElemCapOutlayRevLimitAmt,HsPrlmCapOutlayRevLimitAmt,HsBooksCapOutlayRevLimitAmt,PSElTransAdj,HSTransAdj from ((select g.EntityID,g.PsdCapOutlayRevLimitAmt,g.ElemCapOutlayRevLimitAmt,g.HsPrlmCapOutlayRevLimitAmt,g.HsBooksCapOutlayRevLimitAmt from SaAporCapitalOutlayCalcs g inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporCapitalOutlayCalcs group by EntityID ) gm where g.EntityID=gm.EntityID and g.PaymentMonth=gm.MaxPaymentMonth and g.FiscalYear=2017) )bike1 left join ((select d.EntityID,d.PSElTransAdj,d.HSTransAdj from SaAporSoftCapAlloc d inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporSoftCapAlloc group by EntityID)dm where d.EntityID=dm.EntityID and d.PaymentMonth=dm.MaxPaymentMonth and d.FiscalYear=2017) )car1 on car1.EntityID=bike1.EntityID)lorry on lorry.EntityID=truck.EntityID')
    for prerow in preresult:
        pred = dict(prerow.items())
        d3 = pred['EntityID']
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[d3] = 0
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d3] = 0
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d3] = 0
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS
        if (pred['Type'] == 'Charter Holder-Charter Board'):
            pred['Type'] = "Charter"
        elif (pred['Type'] == 'Charter Holder - University'):
            pred['Type'] = "Charter"
        elif (pred['Type'] == 'School District - Vocational/Technical'):
            pred['Type'] = "JTED"
        else:
            pred['Type'] = "District"
        # calculation of PREKADM

        if pred['sumOfPsdCount'] == None:
            pred['sumOfPsdCount'] = 0

        PREKADM.append(float(pred['sumOfPsdCount']))

        # CALCULATION OF ELEM ADM

        if pred['sumOfElemCount'] == None:
            pred['sumOfElemCount'] = 0
        if pred['sumOfDSCSElemCount'] == None:
            pred['sumOfDSCSElemCount'] = 0
        ELEMADM.append(float(pred['sumOfElemCount']) + float(pred['sumOfDSCSElemCount']))
        # CALCULATION OF HSADM VALUE
        if pred['sumOfHsCount'] == None:
            pred['sumOfHsCount'] = 0
        if pred['sumOfDSCSHsCount'] == None:
            pred['sumOfDSCSHsCount'] = 0
        HSADM.append(float(pred['sumOfHsCount']) + float(pred['sumOfDSCSHsCount']))
        if pred['NetworkForFundingPurposes'] == 1:

            sumofnetworkelemadm[pred['ParentOrganization']] += ELEMADM[count]
            sumofnetworkhsadm[pred['ParentOrganization']] += HSADM[count]

        if pred['EntityID'] not in sumprekadm.keys():
            sumprekadm[pred['EntityID']]=float(PREKADM[count])
        else:
            sumprekadm[pred['EntityID']] += float(PREKADM[count])
        if pred['EntityID'] not in sumelemadm.keys():
            sumelemadm[pred['EntityID']] = float(ELEMADM[count])
        else:
            sumelemadm[pred['EntityID']]+=float(ELEMADM[count])
        if pred['EntityID'] not in sumhsadm.keys():
            sumhsadm[pred['EntityID']] = float(HSADM[count])
        else:
            sumhsadm[pred['EntityID']] += float(HSADM[count])
        # CALCULATION OF CHARTERELEMENTARY AA AND ADM VALUES
        if pred['Type'] == "Charter":
            if pred['EntityID'] not in sumCharterElemADM.keys():
                sumCharterElemADM[pred['EntityID']]=float(ELEMADM[count])
            else:
                sumCharterElemADM[pred['EntityID']]+=float(ELEMADM[count])

            if pred['EntityID'] not in sumCharterHSADM.keys():
                sumCharterHSADM[pred['EntityID']]=float(HSADM[count])
            else:
                sumCharterHSADM[pred['EntityID']]+=float(HSADM[count])
        else:
            sumCharterElemADM[pred['EntityID']] =0
            sumCharterHSADM[pred['EntityID']]=0
        SumofBSL[pred['EntityID']]=0
        count += 1
    #CARRYING ON NEXT STEPS OF CALCULATION
    result = engine.execute('select truck.*,lorry.PsdCapOutlayRevLimitAmt,lorry.ElemCapOutlayRevLimitAmt,lorry.HsPrlmCapOutlayRevLimitAmt,lorry.HsBooksCapOutlayRevLimitAmt,lorry.PSElTransAdj,lorry.HSTransAdj from (select kvs.*, CSH.parentOrganization, CSH.NetworkForFundingPurposes, CSH.ESSmallIsolated, CSH.HSSmallIsolated from (select ftfmaintype.*,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (Select ftfmain.*,EntityName,Entityshort.County,Entityshort.Type from (select EntityID,sum(PsdCount) as sumOfPsdCount,sum(ElemCount) as sumOfElemCount,sum(DSCSElemCnt) as sumOfDSCSElemCount,sum(HsCount) as sumOfHsCount, sum(DSCSHsCnt) as sumOfDSCSHsCount, FiscalYear,TEI,BaseAmount as MaxOfBaseAmount,BaseAdjsAmount as MaxofBaseAdjsAmount, sum(MDSSICnt) as sumOfMDSSICnt, sum(DSCSMDSSICnt)as sumOfDSCSMDSSICnt, sum(DSCSVICnt)as sumOfDSCSVICnt, sum(DSCSOISCCnt) as sumOfDSCSOISCCnt, sum(DSCSPSDCnt)as sumOfDSCSPSDCnt, sum(DSCSMDSCCnt)as sumOfDSCSMDSCCnt, sum(DSCSHICnt)as sumOfDSCSHICnt, sum(DSCSMOMRCnt)as sumOfDSCSMOMRCnt, sum(DSCSEDPPrivateCnt)as sumOfDSCSEDPPrivateCnt, sum(DSCSMDResCnt)as sumOfDSCSMDResCnt, sum(DSCSOIResCnt)as sumOfDSCSOIResCnt, sum(DSCSEDMIMRCnt)as sumOfDSCSEDMIMRCnt, sum(DSCSLEPCnt)as sumOfDSCSLEPCnt, sum(DSCSK3Cnt)as SumOfDSCSK3Cnt, sum(PSDCnt)as sumOfPSDCnt, sum(VICnt)as sumOfVICnt, sum(OISCCnt)as sumOfOISCCnt, sum(MDSCCnt)as sumOfMDSCCnt, sum(HICnt)as sumOfHICnt, sum(MOMRCnt)as sumOfMOMRCnt, sum(EDPPrivateCnt)as sumOfEDPPrivateCnt, sum(MDResCnt)as sumOfMDResCnt, sum(OIResCnt)as sumOfOIResCnt, sum(EDMIMRCnt)as sumOfEDMIMRCnt, sum(LEPCnt)as sumOfLEPCnt, sum(K3Cnt)as sumOfK3Cnt, FTFStatus from ((select t.EntityID,t.FiscalYear,t.PsdCount,t.ElemCount,t.DSCSElemCnt,t.HsCount,t.DSCSHsCnt,t.DSCSK3Cnt,t.TEI,t.PaymentMonth,t.FTFStatus,t.BaseAmount,t.BaseAdjsAmount,t.MDSSICnt,t.DSCSMDSSICnt, t.DSCSVICnt,t.DSCSOISCCnt,t.DSCSPSDCnt,t.DSCSMDSCCnt,t.DSCSHICnt,t.DSCSMOMRCnt,t.DSCSEDPPrivateCnt,t.DSCSMDResCnt,t.DSCSOIResCnt,t.DSCSEDMIMRCnt,t.DSCSLEPCnt,t.PSDCnt,t.VICnt,t.OISCCnt, t.MDSCCnt,t.HICnt,t.MOMRCnt,t.EDPPrivateCnt,t.MDResCnt,t.OIResCnt,t.EDMIMRCnt,t.LEPCnt,t.K3Cnt from SaAporBaseSupportLevelCalcs1 t inner join (select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporBaseSupportLevelCalcs1 group by EntityID) tm on t.EntityID=tm.EntityID and t.PaymentMonth=tm.MaxPaymentMonth) union all select EntityID,FiscalYear,PsdCount,ElemCount,DSCSElemCnt,HsCount,DSCSHsCnt,DSCSK3Cnt,TEI,PaymentMonth,FTFStatus,BaseAmount,BaseAdjsAmount, MDSSICnt,DSCSMDSSICnt, DSCSVICnt,DSCSOISCCnt,DSCSPSDCnt,DSCSMDSCCnt,DSCSHICnt,DSCSMOMRCnt,DSCSEDPPrivateCnt,DSCSMDResCnt,DSCSOIResCnt,DSCSEDMIMRCnt,DSCSLEPCnt,PSDCnt,VICnt,OISCCnt, MDSCCnt,HICnt,MOMRCnt,EDPPrivateCnt,MDResCnt,OIResCnt,EDMIMRCnt,LEPCnt,K3Cnt from SaCharBaseSupportLevelCalcs1 where PaymentMonth=13)uni where FiscalYear=2017 group by EntityID,FTFStatus )ftfmain left join (select EntityID,EntityName,County,Entity.Type from Entity)Entityshort on ftfmain.EntityID=Entityshort.EntityID )ftfmaintype left join (select TRCLTSL.EntityID,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (select TRCL.EntityID,TRCL,TSL from ((select j.EntityID,j.TRCL from SaAporTransRevCtlLimit j inner join ( select EntityID,max(PaymentMonth)as MaxPaymentMonth from SaAporTransRevCtlLimit group by EntityID) jm on j.EntityID=jm.EntityID and j.PaymentMonth=jm.MaxPaymentMonth and FiscalYear=2017))TRCL left join ((select k.EntityID,k.TSL from SaAporTransSupptLvl k inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporTransSupptLvl group by EntityID)km where k.EntityID=km.EntityID and k.PaymentMonth=km.MaxPaymentMonth and k.FiscalYear=2017))TSL on TRCL.EntityID=TSL.EntityID)TRCLTSL left join ((Select l.EntityID,l.TotalPSElAssessValAmt,l.TotalHSAssessValAmt from SaAporQualLevy l inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporQualLevy group by EntityID)lm where l.EntityID=lm.EntityID and l.PaymentMonth=lm.MaxPaymentMonth and l.FiscalYear=2017))PSEl on TRCLTSL.EntityID=PSEl.EntityID )Bike on ftfmaintype.EntityID=Bike.EntityID) kvs left join (select CWN.EntityID, CWN.EntityName, CWN.parentOrganization, CWN.NetworkForFundingPurposes, ESSmallIsolated, HSSmallIsolated from (select EntityID, ChartersWithNetwork.OrganizationName as EntityName, ParentOrganization, ifnull(Charters4Funding.NetworkForFundingPurposes,0) as NetworkForFundingPurposes  from ChartersWithNetwork left join Charters4Funding on ChartersWithNetwork.ParentOrganization = Charters4Funding.OrganizationName) CWN left join SmallIsolatedList on CWN.EntityID = SmallIsolatedList.EntityID)CSH on kvs.EntityID = CSH.EntityID)truck left join(select car1.EntityID,PsdCapOutlayRevLimitAmt,ElemCapOutlayRevLimitAmt,HsPrlmCapOutlayRevLimitAmt,HsBooksCapOutlayRevLimitAmt,PSElTransAdj,HSTransAdj from ((select g.EntityID,g.PsdCapOutlayRevLimitAmt,g.ElemCapOutlayRevLimitAmt,g.HsPrlmCapOutlayRevLimitAmt,g.HsBooksCapOutlayRevLimitAmt from SaAporCapitalOutlayCalcs g inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporCapitalOutlayCalcs group by EntityID ) gm where g.EntityID=gm.EntityID and g.PaymentMonth=gm.MaxPaymentMonth and g.FiscalYear=2017) )bike1 left join ((select d.EntityID,d.PSElTransAdj,d.HSTransAdj from SaAporSoftCapAlloc d inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporSoftCapAlloc group by EntityID)dm where d.EntityID=dm.EntityID and d.PaymentMonth=dm.MaxPaymentMonth and d.FiscalYear=2017) )car1 on car1.EntityID=bike1.EntityID)lorry on lorry.EntityID=truck.EntityID')
    #PERFORMING BSL CALCULATION
    for row in result:
        # Creating a dictionary of the values retrieved from the query
        d = dict(row.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS
        if (d['Type'] == 'Charter Holder-Charter Board'):
            d['Type'] = "Charter"
        elif (d['Type'] == 'Charter Holder - University'):
            d['Type'] = "Charter"
        elif (d['Type'] == 'School District - Vocational/Technical'):
            d['Type'] = "JTED"
        else:
            d['Type'] = "District"
        if d['Type'] == "Charter":
            CharterElemAA[d['EntityID']] = (float(CharSuppLvlAllK_8) * float(sumCharterElemADM[d['EntityID']]))
            CharterHSAA[d['EntityID']] = (float(CharSuppLvlAll9_12) * float(sumCharterHSADM[d['EntityID']]))
        else:
            CharterElemAA[d['EntityID']]=0
            CharterHSAA[d['EntityID']] =0

    #CALCULATION OF ELEMENTARY RANGE AND NETWORK RANGES FOR WEIGHT CALCULATION
        if d['NetworkForFundingPurposes'] == 1:
            NetworkElemADM.append(sumofnetworkelemadm[d['ParentOrganization']])
            NetworkHSADM.append(sumofnetworkhsadm[d['ParentOrganization']])
            if NetworkHSADM[ddd] >= float(1) and NetworkHSADM[ddd] < float(100):
                HSRange.append("1to99")
            elif NetworkHSADM[ddd] >= float(100) and NetworkHSADM[ddd] < float(500):
                HSRange.append("100to499")
            elif NetworkHSADM[ddd] >= (float(500)) and NetworkHSADM[ddd] < (float(600)):
                HSRange.append("500to599")
            elif (NetworkHSADM[ddd] >= float(600)):
                HSRange.append(">600")
            else:
                HSRange.append(None)
            if NetworkElemADM[ddd] >= float(1) and NetworkElemADM[ddd] < float(100):
                ELEMRange.append("1to99")
            elif NetworkElemADM[ddd] >= float(100) and NetworkElemADM[ddd] < float(500):
                ELEMRange.append("100to499")
            elif NetworkElemADM[ddd] >= (float(500)) and NetworkElemADM[ddd] < (float(600)):
                ELEMRange.append("500to599")
            elif (NetworkElemADM[ddd] >= float(600)):
                ELEMRange.append(">600")
            else:
                ELEMRange.append(None)
        else:
            NetworkElemADM.append(0)
            NetworkHSADM.append(0)
            if sumhsadm[d['EntityID']] >= float(1) and sumhsadm[d['EntityID']] < float(100):
                HSRange.append("1to99")
            elif sumhsadm[d['EntityID']] >= float(100) and sumhsadm[d['EntityID']] < float(500):
                HSRange.append("100to499")
            elif sumhsadm[d['EntityID']] >= (float(500)) and sumhsadm[d['EntityID']] < (float(600)):
                HSRange.append("500to599")
            elif (sumhsadm[d['EntityID']] >= float(600)):
                HSRange.append(">600")
            else:
                HSRange.append(None)
            if sumelemadm[d['EntityID']] >= float(1) and sumelemadm[d['EntityID']] < float(100):
                ELEMRange.append("1to99")
            elif sumelemadm[d['EntityID']] >= float(100) and sumelemadm[d['EntityID']] < float(500):
                ELEMRange.append("100to499")
            elif sumelemadm[d['EntityID']] >= (float(500)) and sumelemadm[d['EntityID']] < (float(600)):
                ELEMRange.append("500to599")
            elif (sumelemadm[d['EntityID']] >= float(600)):
                ELEMRange.append(">600")
            else:
                ELEMRange.append(None)
        #CALCULATION OF SSWHSINCREMENTALWEIGHTPP
        if (d['Type'] == "JTED"):
            SSWHSINCREMENTALWEIGHTPP.append(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[ddd] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso1to999_12)
                elif HSRange[ddd] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso100to4999_12)
                elif HSRange[ddd] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
            else:
                if HSRange[ddd] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall1to999_12)
                elif HSRange[ddd] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall100to4999_12)
                elif HSRange[ddd] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
        #CALCULATION OF FinalHSBASEWEIGHT
        if (d['Type'] == "JTED"):
            HSBaseWeight.append(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[ddd] == "1to99":
                    HSBaseWeight.append(WtSmallIso1to999_12)
                elif HSRange[ddd] == "100to499":
                    HSBaseWeight.append(WtSmallIso100to4999_12)
                elif HSRange[ddd] == "500to599":
                    HSBaseWeight.append(WtSmallIso500to5999_12)
                else:
                    HSBaseWeight.append(0)
            else:
                if HSRange[ddd] == "1to99":
                    HSBaseWeight.append(WtSmall1to999_12)
                elif HSRange[ddd] == "100to499":
                    HSBaseWeight.append(WtSmall100to4999_12)
                elif HSRange[ddd] == "500to599":
                    HSBaseWeight.append(WtSmall500to5999_12)
                else:
                    HSBaseWeight.append(0)
        #CALCUATION OF Final9-12WEIGHT
        if d['Type'] == "JTED":
            Final_9_12SmWgt.append(GroupAFinalGroupAWeightsJTED)
        else:
            if HSRange[ddd] == ">600":
                Final_9_12SmWgt.append(GroupAFinalGroupAWeights9_12)
            elif HSRange[ddd] == "1to99":
                Final_9_12SmWgt.append(HSBaseWeight[ddd])
            elif HSRange[ddd] == "100to499":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt.append(float(HSBaseWeight[ddd]) + (float(SSWHSINCREMENTALWEIGHTPP[ddd]) * (float(float(500) - float(NetworkHSADM[ddd])))))
                else:
                    Final_9_12SmWgt.append(float(HSBaseWeight[ddd]) + (float(SSWHSINCREMENTALWEIGHTPP[ddd]) * (float(float(500) - float(HSADM[ddd])))))
            elif HSRange[ddd] == "500to599":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt.append(float(HSBaseWeight[ddd]) + (float(SSWHSINCREMENTALWEIGHTPP[ddd]) * (float(float(600) - float(NetworkHSADM[ddd])))))
                else:
                    Final_9_12SmWgt.append(float(HSBaseWeight[ddd]) + (float(SSWHSINCREMENTALWEIGHTPP[ddd]) * (float(float(600) - float(HSADM[ddd])))))
            else:
                Final_9_12SmWgt.append(GroupAFinalGroupAWeights9_12)
        # CALCULATION OF SSWELEMINCREMENTALWEIGHTPP
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[ddd] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso1to99K_8)
            elif ELEMRange[ddd] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso100to499K_8)
            elif ELEMRange[ddd] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        else:
            if ELEMRange[ddd] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall1to99K_8)
            elif ELEMRange[ddd] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall100to499K_8)
            elif ELEMRange[ddd] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        # CALCULATION OF FINALELEMBASEWEIGHT
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[ddd] == "1to99":
                ElemBaseWeight.append(WtSmallIso1to99K_8)
            elif ELEMRange[ddd] == "100to499":
                ElemBaseWeight.append(WtSmallIso100to499K_8)
            elif ELEMRange[ddd] == "500to599":
                ElemBaseWeight.append(WtSmallIso500to599K_8)
            else:
                ElemBaseWeight.append(0)
        else:
            if ELEMRange[ddd] == "1to99":
                ElemBaseWeight.append(WtSmall1to99K_8)
            elif ELEMRange[ddd] == "100to499":
                ElemBaseWeight.append(WtSmall100to499K_8)
            elif ELEMRange[ddd] == "500to599":
                ElemBaseWeight.append(WtSmall500to599K_8)
            else:
                ElemBaseWeight.append(0)
        # CALCUATION OF K-8WEIGHT
        if ELEMRange[ddd] == ">600":
            Final_K_8SmWgt.append(GroupAFinalGroupAWeightsK_8)
        elif ELEMRange[ddd] == "1to99":
            Final_K_8SmWgt.append(ElemBaseWeight[ddd])
        elif ELEMRange[ddd] == "100to499":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt.append(float(ElemBaseWeight[ddd]) + (float(SSWELEMINCREMENTALWEIGHTPP[ddd]) * (float(500 - NetworkElemADM[ddd]))))
            else:
                Final_K_8SmWgt.append(float(ElemBaseWeight[ddd]) + (float(SSWELEMINCREMENTALWEIGHTPP[ddd]) * (float(500 - ELEMADM[ddd]))))
        elif ELEMRange[ddd] == "500to599":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt.append(float(ElemBaseWeight[ddd]) + (float(SSWELEMINCREMENTALWEIGHTPP[ddd]) * (float(600 - NetworkElemADM[ddd]))))
            else:
                Final_K_8SmWgt.append(float(ElemBaseWeight[ddd]) + (float(SSWELEMINCREMENTALWEIGHTPP[ddd]) * (float(600 - ELEMADM[ddd]))))
        else:
            Final_K_8SmWgt.append(GroupAFinalGroupAWeightsK_8)
        # CALCULATION OF VARIABLES FOR GROUP B WEIGHTS
        if d['sumOfDSCSEDMIMRCnt'] == None:
            d['sumOfDSCSEDMIMRCnt'] = 0
        if d['sumOfEDMIMRCnt'] == None:
            d['sumOfEDMIMRCnt'] = 0
        GB1_EDMIDSLD.append(float(d['sumOfEDMIMRCnt']) + float(d['sumOfDSCSEDMIMRCnt']))
        if d['sumOfK3Cnt'] == None:
            d['sumOfK3Cnt'] = 0
        if d['SumOfDSCSK3Cnt'] == None:
            d['SumOfDSCSK3Cnt'] = 0
        GB2_K3Reading.append(float(d['sumOfK3Cnt']) + float(d['SumOfDSCSK3Cnt']))
        GB3_K3.append(float(d['sumOfK3Cnt']) + float(d['SumOfDSCSK3Cnt']))
        if d['sumOfLEPCnt'] == None:
            d['sumOfLEPCnt'] = 0
        if d['sumOfDSCSLEPCnt'] == None:
            d['sumOfDSCSLEPCnt'] = 0
        GB4_ELL.append(float(d['sumOfLEPCnt']) + float(d['sumOfDSCSLEPCnt']))
        if d['sumOfOIResCnt'] == None:
            d['sumOfOIResCnt'] = 0
        if d['sumOfDSCSOIResCnt'] == None:
            d['sumOfDSCSOIResCnt'] = 0
        GB5_OI_R.append(float(d['sumOfOIResCnt']) + float(d['sumOfDSCSOIResCnt']))
        if d['sumOfPSDCnt'] == None:
            d['sumOfPSDCnt'] = 0
        if d['sumOfDSCSPSDCnt'] == None:
            d['sumOfDSCSPSDCnt'] = 0
        GB6_PS_D.append(float(d['sumOfPSDCnt']) + float(d['sumOfDSCSPSDCnt']))
        if d['sumOfMOMRCnt'] == None:
            d['sumOfMOMRCnt'] = 0
        if d['sumOfDSCSMOMRCnt'] == None:
            d['sumOfDSCSMOMRCnt'] = 0
        GB7_MOID.append(float(d['sumOfMOMRCnt']) + float(d['sumOfDSCSMOMRCnt']))
        if d['sumOfHICnt'] == None:
            d['sumOfHICnt'] = 0
        if d['sumOfDSCSHICnt'] == None:
            d['sumOfDSCSHICnt'] = 0
        GB8_HI.append(float(d['sumOfHICnt']) + float(d['sumOfDSCSHICnt']))
        if d['sumOfVICnt'] == None:
            d['sumOfVICnt'] = 0
        if d['sumOfDSCSVICnt'] == None:
            d['sumOfDSCSVICnt'] = 0
        GB9_VI.append(float(d['sumOfVICnt']) + float(d['sumOfDSCSVICnt']))
        if d['sumOfEDPPrivateCnt'] == None:
            d['sumOfEDPPrivateCnt'] = 0
        if d['sumOfDSCSEDPPrivateCnt'] == None:
            d['sumOfDSCSEDPPrivateCnt'] = 0
        GB10_ED_P.append(float(d['sumOfEDPPrivateCnt']) + float(d['sumOfDSCSEDPPrivateCnt']))
        if d['sumOfMDSCCnt'] == None:
            d['sumOfMDSCCnt'] = 0
        if d['sumOfDSCSMDSCCnt'] == None:
            d['sumOfDSCSMDSCCnt'] = 0
        GB11_MDSC.append(float(d['sumOfMDSCCnt']) + float(d['sumOfDSCSMDSCCnt']))
        if d['sumOfMDResCnt'] == None:
            d['sumOfMDResCnt'] = 0
        if d['sumOfDSCSMDResCnt'] == None:
            d['sumOfDSCSMDResCnt'] = 0
        GB12_MD_R.append(float(d['sumOfMDResCnt']) + float(d['sumOfDSCSMDResCnt']))
        if d['sumOfOISCCnt'] == None:
            d['sumOfOISCCnt'] = 0
        if d['sumOfDSCSOISCCnt'] == None:
            d['sumOfDSCSOISCCnt'] = 0
        GB13_OI_SC.append(float(d['sumOfOISCCnt']) + float(d['sumOfDSCSOISCCnt']))
        if d['sumOfMDSSICnt'] == None:
            d['sumOfMDSSICnt'] = 0
        if d['sumOfDSCSMDSSICnt'] == None:
            d['sumOfDSCSMDSSICnt'] = 0
        GB14_MD_SSI.append(float(d['sumOfMDSSICnt']) + float(d['sumOfDSCSMDSSICnt']))
        if d["TEI"] == None:
            d["TEI"] = 0
        # CALCULATION OF TEI
        TEI.append(float(max(TEI10, d["TEI"])))
        # calculation of BASEAMOUNT
        if float(d["MaxOfBaseAmount"]) == 3635.64:
            TeacherComp.append(1)
        else:
            TeacherComp.append(0)
        if float(d["MaxOfBaseAmount"]) == 3681.09:
            techercompand200daycalender.append(1)
        else:
            techercompand200daycalender.append(0)
        # if TeacherComp[ddd]==1:
        #    LEABaseLevel.append(float(d["MaxOfBaseAmount"])+(float(d["MaxOfBaseAmount"])*TeacherCompPercent))
        # elif techercompand200daycalender[ddd]==1:

        #   LEABaseLevel.append(float(d["MaxOfBaseAmount"]) + (float(d["MaxOfBaseAmount"]) * Percent200DayCalender))
        # else:
        LEABaseLevel.append(float(d["MaxOfBaseAmount"]))
        # calculation of O
        WeightedElemCounts.append(float(ELEMADM[ddd]) * round(float(Final_K_8SmWgt[ddd]),3))
        # calculation of P
        WeightedHSCounts.append(float(HSADM[ddd]) * round(float(Final_9_12SmWgt[ddd]),3))
        # CALCULATION of WEIGHTED PREKCOUNT
        WeightedPreKCounts.append(float(PREKADM[ddd] * float(GroupAFinalGroupAWeightsPSD)))
        # CALCULATION OF PREKBSL
        if d['FTFStatus'] == '1':
            PrekBSL.append((float(TEI[ddd])) * (float(LEABaseLevel[ddd])) * round(float(WeightedPreKCounts[ddd]),3) * float(FullTimeAOI))
        elif d['FTFStatus'] == '0':
            PrekBSL.append((float(TEI[ddd])) * (float(LEABaseLevel[ddd])) * round(float(WeightedPreKCounts[ddd]),3) * float(HalfTimeAOI))
        else:
            PrekBSL.append((float(TEI[ddd])) * (float(LEABaseLevel[ddd])) * round(float(WeightedPreKCounts[ddd]),3))
        # CALCULATION OF ELEMBSL AND HSBSL
        if (d["FTFStatus"] == '0'):
            ELEMBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedElemCounts[ddd]),3) * float(HalfTimeAOI))
            HSBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedHSCounts[ddd]),3) * float(HalfTimeAOI))
        elif (d["FTFStatus"] == '1'):
            ELEMBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedElemCounts[ddd]),3) * float(FullTimeAOI))
            HSBSL.append(
                (float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedHSCounts[ddd]),3) * float(FullTimeAOI))
        else:
            ELEMBSL.append(
                ((LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedElemCounts[ddd]),3))
            HSBSL.append(
                (float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(WeightedHSCounts[ddd]),3))
        # CALCULATION OF VARIABLES FOR Q(GROUP B WEIGHTED ADD ON COUNTS) FROM STUDENT COUNTS FY2016_CLEAN
        Weighted_GB1_EDMIDSLD.append(float(GB1_EDMIDSLD[ddd]) * float(GroupB1))
        Weighted_GB2_K3Reading.append(float(GB2_K3Reading[ddd]) * float(GroupB2))
        Weighted_GB3_K3.append(float(GB3_K3[ddd]) * float(GroupB3))
        Weighted_.append(float(GB4_ELL[ddd]) * float(GroupB4))
        Weighted_GB5_OI_R.append(float(GB5_OI_R[ddd]) * float(GroupB5))
        Weighted_GB6_PS_D.append(float(GB6_PS_D[ddd]) * float(GroupB6))
        Weighted_GB7_MOID.append(float(GB7_MOID[ddd]) * float(GroupB7))
        Weighted_GB8_HI.append(float(GB8_HI[ddd]) * float(GroupB8))
        Weighted_GB9_VI.append(float(GB9_VI[ddd]) * float(GroupB9))
        Weighted_GB10_ED_P.append(float(GB10_ED_P[ddd]) * float(GroupB10))
        Weighted_GB11_MDSC.append(float(GB11_MDSC[ddd]) * float(GroupB11))
        Weighted_GB12_MD_R.append(float(GB12_MD_R[ddd]) * float(GroupB12))
        Weighted_GB13_OI_SC.append(float(GB13_OI_SC[ddd]) * float(GroupB13))
        Weighted_GB14_MD_SSI.append(float(GB14_MD_SSI[ddd]) * float(GroupB14))
        # CALCULATION OF GROUP B WEIGHTED ADD ON COUNTS
        GroupBWeightedAddonCounts.append(
            round(Weighted_GB1_EDMIDSLD[ddd],3) + round(Weighted_GB2_K3Reading[ddd],3) + round(Weighted_GB3_K3[ddd],3) + round(Weighted_[ddd],3) +
            round(Weighted_GB5_OI_R[ddd],3) + round(Weighted_GB6_PS_D[ddd],3) + round(Weighted_GB7_MOID[ddd],3) + round(Weighted_GB8_HI[ddd],3) +
            round(Weighted_GB9_VI[ddd],3) + round(Weighted_GB10_ED_P[ddd],3) + round(Weighted_GB11_MDSC[ddd],3) + round(Weighted_GB12_MD_R[ddd],3) +
            round(Weighted_GB13_OI_SC[ddd],3) + round(Weighted_GB14_MD_SSI[ddd],3))
        # CALCULATION OF GROUP B BSL
        if (d["FTFStatus"] == '0'):
            GroupBBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(GroupBWeightedAddonCounts[ddd]),3) * (float(HalfTimeAOI)))

        elif (d["FTFStatus"] == '1'):
            GroupBBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) * round(float(GroupBWeightedAddonCounts[ddd]),3) *(float(FullTimeAOI)))
        else:
            GroupBBSL.append((float(LEABaseLevel[ddd])) * (float(TEI[ddd])) *round(float(GroupBWeightedAddonCounts[ddd]),3))
        # CALCULATION OF AuditBaseLevelAdjustment
        if (d["FTFStatus"] != "NULL"):
            AuditBaseLevelAdjustment.append(float(0))
        else:
            AuditBaseLevelAdjustment.append(float(d["MaxofBaseAdjsAmount"]))
        # CALCULATION OF LOSS FROM SSW OF K-8 FUNDING AND LOSS FROM SSW OF 9-12 FUNDING
        AB2.append(float(LEABaseLevel[ddd]) * float(Final_K_8SmWgt[ddd]) * float(ELEMADM[ddd]))
        AH.append(0)
        # AH.append(float(AB2[ddd])-float(AB2[ddd]*float(sixtyseven/100)))
        AC2.append(float(LEABaseLevel[ddd]) * float(Final_9_12SmWgt[ddd]) * float(HSADM[ddd]))
        AI.append(0)
        # AI.append(float(AC2[ddd]) - float(AC2[ddd] * float(sixtyseven / 100)))
        # CALCULATION OF BSL VALUE
        BSLWithoutAdjustment.append((float(PrekBSL[ddd]) + float(ELEMBSL[ddd]) + round(float(HSBSL[ddd]), 3) + round(float(GroupBBSL[ddd]), 3)  ))
        BSL.append((float(PrekBSL[ddd]) + float(ELEMBSL[ddd]) + round(float(HSBSL[ddd]),3) + round(float(GroupBBSL[ddd]),3) + float(AuditBaseLevelAdjustment[ddd])))
        SumofBSL[d['EntityID']]+=BSL[ddd]
        # STORING ENTITY ID
        EID.append(d['EntityID'])
        # STORING ENTITY NAME
        Ename.append(d['EntityName'])
        # CALCULATION OF TOTOAL NET CHARTER AA
        if d['EntityID'] not in sumCharterElemADM.keys():
            LEApercentofCharterElemADM.append(0)
        elif (sumCharterElemADM[d['EntityID']] == 0 or sumCharterElemADM[d['EntityID']] ==None) :
            LEApercentofCharterElemADM.append(0)
        else:
            LEApercentofCharterElemADM.append(float(sumCharterElemADM[d['EntityID']] / sum(sumCharterElemADM)))
        if d['EntityID'] not in sumCharterHSADM.keys():
            LEApercentofCharterHSADM.append(0)
        elif sumCharterHSADM[d['EntityID']] == 0 or sumCharterHSADM[d['EntityID']] ==None:
            LEApercentofCharterHSADM.append(0)
        else:
            LEApercentofCharterHSADM.append(float(sumCharterHSADM[d['EntityID']] / sum(sumCharterHSADM)))

        if (sum(CharterElemAA) + sum(CharterHSAA)) == 0:
            K_8PercentofTotalcharterAA.append(0)
        else:
            K_8PercentofTotalcharterAA.append(float(sum(CharterElemAA) / (sum(CharterElemAA) + sum(CharterHSAA))))
        TotalCharterElemReduction.append(float(CharterReduction) * float(K_8PercentofTotalcharterAA[ddd]))
        TotalCharterHSReduction.append(float(CharterReduction) * float((1 - float(K_8PercentofTotalcharterAA[ddd]))))
        CharterElemAAReduction.append(float(LEApercentofCharterElemADM[ddd]) * float(TotalCharterElemReduction[ddd]))
        CharterHSAAReduction.append(float(LEApercentofCharterHSADM[ddd]) * float(TotalCharterHSReduction[ddd]))
        TotalNetCharterAA.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]) - (float(CharterElemAAReduction[ddd] + CharterHSAAReduction[ddd])))
        # CALCULATION OF FINAL FORUMULAADDITIONALASSISTANCE
        if d['Type'] == "Charter":
            DistrictHSTextbooksAA.append(0)
            DistrictHSAA.append(0)
            DistrictElemAA.append(0)
            DistrictPreKAA.append(0)
            DistrictPreKElemReduction.append(float(0))
            DistrictHSReduction.append(float(0))
            TotalDistrictAAReduction.append(float(0))
            TotalFormulaDistrictAA.append(float(0))
            TotalNetDistrictAA.append(float(0))
            FinalFormulaAAwithReduction.append(float(TotalNetCharterAA[ddd]))
            FinalFormulaAdditionalAssistance.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]))
        else:
            if AdditionalAssistant_eqformula == 2:

                DistrictHSTextbooksAA.append(0)
                DistrictPreKAA.append(float(DistSuppLvlAllPSD * sumprekadm[d['EntityID']]))
                if HSRange[ddd] == "1to99":
                    DistrictHSAA.append(float(DistSuppLvl1to999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[ddd] == "100to499" or HSRange[ddd] == "100to499":
                    DistrictHSAA.append(float(DistSuppLvl100to5999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[ddd] == ">600":
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                else:
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                if ELEMRange[ddd] == "1to99":
                    DistrictElemAA.append(float(DistSuppLvl1to99K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[ddd] == "100to499" or ELEMRange[ddd] == "500to599":
                    DistrictElemAA.append(float(DistSuppLvl100to599K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[ddd] == ">600":
                    DistrictElemAA.append(float(DistSuppLvl600AndOverK_8 * sumelemadm[d['EntityID']]))
                else:
                    DistrictElemAA.append(float(DistSuppLvl600AndOverK_8 * sumelemadm[d['EntityID']]))


            else:
                if d['HsBooksCapOutlayRevLimitAmt'] == None:
                    d['HsBooksCapOutlayRevLimitAmt'] = 0
                if d['HsPrlmCapOutlayRevLimitAmt'] == None:
                    d['HsPrlmCapOutlayRevLimitAmt'] = 0
                if d['ElemCapOutlayRevLimitAmt'] == None:
                    d['ElemCapOutlayRevLimitAmt'] = 0
                if d['PsdCapOutlayRevLimitAmt'] == None:
                    d['PsdCapOutlayRevLimitAmt'] = 0

                DistrictHSTextbooksAA.append(float(d['HsBooksCapOutlayRevLimitAmt']))
                DistrictHSAA.append(float(d['HsPrlmCapOutlayRevLimitAmt']))
                DistrictElemAA.append(float(d['ElemCapOutlayRevLimitAmt']))
                DistrictPreKAA.append(float(d['PsdCapOutlayRevLimitAmt']))
            if d['PSElTransAdj'] == None:
                d['PSElTransAdj'] = 0
            if d['HSTransAdj'] == None:
                d['HSTransAdj'] = 0
            DistrictPreKElemReduction.append(float(d['PSElTransAdj']))
            DistrictHSReduction.append(float(d['HSTransAdj']))
            TotalDistrictAAReduction.append(float(DistrictPreKElemReduction[ddd] + DistrictHSReduction[ddd]))
            TotalFormulaDistrictAA.append(float(DistrictHSTextbooksAA[ddd] + DistrictHSAA[ddd] + DistrictElemAA[ddd] + DistrictPreKAA[ddd]))
            TotalNetDistrictAA.append(float(TotalFormulaDistrictAA[ddd] + TotalDistrictAAReduction[ddd]))

            FinalFormulaAAwithReduction.append(TotalNetDistrictAA[ddd])
            FinalFormulaAdditionalAssistance.append(TotalFormulaDistrictAA[ddd])
        # CALCULATION OF FINALAAALLOCATION
        if AdditonalAssistantReduction == 1:
            FinalAAAllocation.append(FinalFormulaAAwithReduction[ddd])
        else:
            FinalAAAllocation.append(FinalFormulaAdditionalAssistance[ddd])

        AdditionalAssistance.append(FinalAAAllocation[ddd])


        OppurtunityWeight.append(float(0))
        if d['TRCL'] == None:
            d['TRCL'] = 0
        if d['TSL'] == None:
            d['TSL'] = 0
        TRCL.append(float(d['TRCL']))
        TSL.append(float(d['TSL']))

        # CALCULATION OF  WEIGHTED PUPILS USER SPECIFIED SSW REDUCTION
        PreKWeightedPupilsuser_specifiedSWWreduction.append(
            float(float(PREKADM[ddd] * float(GroupAFinalGroupAWeightsPSD)) - 0))
        K_8WeightedPupilsuser_specifiedSWWreduction.append((float(ELEMADM[ddd]) * float(Final_K_8SmWgt[ddd])) - 0)
        nine_12WeightedPupilsuser_specifiedSWWreduction.append((float(HSADM[ddd]) * float(Final_9_12SmWgt[ddd])) - 0)
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += PreKWeightedPupilsuser_specifiedSWWreduction[ddd]
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += K_8WeightedPupilsuser_specifiedSWWreduction[ddd]
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += nine_12WeightedPupilsuser_specifiedSWWreduction[ddd]
        ddd += 1
    dd4 = 0
    result3 = engine.execute('select truck.*,lorry.PsdCapOutlayRevLimitAmt,lorry.ElemCapOutlayRevLimitAmt,lorry.HsPrlmCapOutlayRevLimitAmt,lorry.HsBooksCapOutlayRevLimitAmt,lorry.PSElTransAdj,lorry.HSTransAdj from (select kvs.*, CSH.parentOrganization, CSH.NetworkForFundingPurposes, CSH.ESSmallIsolated, CSH.HSSmallIsolated from (select ftfmaintype.*,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (Select ftfmain.*,EntityName,Entityshort.County,Entityshort.Type from (select EntityID,sum(PsdCount) as sumOfPsdCount,sum(ElemCount) as sumOfElemCount,sum(DSCSElemCnt) as sumOfDSCSElemCount,sum(HsCount) as sumOfHsCount, sum(DSCSHsCnt) as sumOfDSCSHsCount, FiscalYear,TEI,BaseAmount as MaxOfBaseAmount,BaseAdjsAmount as MaxofBaseAdjsAmount, sum(MDSSICnt) as sumOfMDSSICnt, sum(DSCSMDSSICnt)as sumOfDSCSMDSSICnt, sum(DSCSVICnt)as sumOfDSCSVICnt, sum(DSCSOISCCnt) as sumOfDSCSOISCCnt, sum(DSCSPSDCnt)as sumOfDSCSPSDCnt, sum(DSCSMDSCCnt)as sumOfDSCSMDSCCnt, sum(DSCSHICnt)as sumOfDSCSHICnt, sum(DSCSMOMRCnt)as sumOfDSCSMOMRCnt, sum(DSCSEDPPrivateCnt)as sumOfDSCSEDPPrivateCnt, sum(DSCSMDResCnt)as sumOfDSCSMDResCnt, sum(DSCSOIResCnt)as sumOfDSCSOIResCnt, sum(DSCSEDMIMRCnt)as sumOfDSCSEDMIMRCnt, sum(DSCSLEPCnt)as sumOfDSCSLEPCnt, sum(DSCSK3Cnt)as SumOfDSCSK3Cnt, sum(PSDCnt)as sumOfPSDCnt, sum(VICnt)as sumOfVICnt, sum(OISCCnt)as sumOfOISCCnt, sum(MDSCCnt)as sumOfMDSCCnt, sum(HICnt)as sumOfHICnt, sum(MOMRCnt)as sumOfMOMRCnt, sum(EDPPrivateCnt)as sumOfEDPPrivateCnt, sum(MDResCnt)as sumOfMDResCnt, sum(OIResCnt)as sumOfOIResCnt, sum(EDMIMRCnt)as sumOfEDMIMRCnt, sum(LEPCnt)as sumOfLEPCnt, sum(K3Cnt)as sumOfK3Cnt, FTFStatus from ((select t.EntityID,t.FiscalYear,t.PsdCount,t.ElemCount,t.DSCSElemCnt,t.HsCount,t.DSCSHsCnt,t.DSCSK3Cnt,t.TEI,t.PaymentMonth,t.FTFStatus,t.BaseAmount,t.BaseAdjsAmount,t.MDSSICnt,t.DSCSMDSSICnt, t.DSCSVICnt,t.DSCSOISCCnt,t.DSCSPSDCnt,t.DSCSMDSCCnt,t.DSCSHICnt,t.DSCSMOMRCnt,t.DSCSEDPPrivateCnt,t.DSCSMDResCnt,t.DSCSOIResCnt,t.DSCSEDMIMRCnt,t.DSCSLEPCnt,t.PSDCnt,t.VICnt,t.OISCCnt, t.MDSCCnt,t.HICnt,t.MOMRCnt,t.EDPPrivateCnt,t.MDResCnt,t.OIResCnt,t.EDMIMRCnt,t.LEPCnt,t.K3Cnt from SaAporBaseSupportLevelCalcs1 t inner join (select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporBaseSupportLevelCalcs1 group by EntityID) tm on t.EntityID=tm.EntityID and t.PaymentMonth=tm.MaxPaymentMonth) union all select EntityID,FiscalYear,PsdCount,ElemCount,DSCSElemCnt,HsCount,DSCSHsCnt,DSCSK3Cnt,TEI,PaymentMonth,FTFStatus,BaseAmount,BaseAdjsAmount, MDSSICnt,DSCSMDSSICnt, DSCSVICnt,DSCSOISCCnt,DSCSPSDCnt,DSCSMDSCCnt,DSCSHICnt,DSCSMOMRCnt,DSCSEDPPrivateCnt,DSCSMDResCnt,DSCSOIResCnt,DSCSEDMIMRCnt,DSCSLEPCnt,PSDCnt,VICnt,OISCCnt, MDSCCnt,HICnt,MOMRCnt,EDPPrivateCnt,MDResCnt,OIResCnt,EDMIMRCnt,LEPCnt,K3Cnt from SaCharBaseSupportLevelCalcs1 where PaymentMonth=13)uni where FiscalYear=2017 group by EntityID,FTFStatus )ftfmain left join (select EntityID,EntityName,County,Entity.Type from Entity)Entityshort on ftfmain.EntityID=Entityshort.EntityID )ftfmaintype left join (select TRCLTSL.EntityID,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (select TRCL.EntityID,TRCL,TSL from ((select j.EntityID,j.TRCL from SaAporTransRevCtlLimit j inner join ( select EntityID,max(PaymentMonth)as MaxPaymentMonth from SaAporTransRevCtlLimit group by EntityID) jm on j.EntityID=jm.EntityID and j.PaymentMonth=jm.MaxPaymentMonth and FiscalYear=2017))TRCL left join ((select k.EntityID,k.TSL from SaAporTransSupptLvl k inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporTransSupptLvl group by EntityID)km where k.EntityID=km.EntityID and k.PaymentMonth=km.MaxPaymentMonth and k.FiscalYear=2017))TSL on TRCL.EntityID=TSL.EntityID)TRCLTSL left join ((Select l.EntityID,l.TotalPSElAssessValAmt,l.TotalHSAssessValAmt from SaAporQualLevy l inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporQualLevy group by EntityID)lm where l.EntityID=lm.EntityID and l.PaymentMonth=lm.MaxPaymentMonth and l.FiscalYear=2017))PSEl on TRCLTSL.EntityID=PSEl.EntityID )Bike on ftfmaintype.EntityID=Bike.EntityID) kvs left join (select CWN.EntityID, CWN.EntityName, CWN.parentOrganization, CWN.NetworkForFundingPurposes, ESSmallIsolated, HSSmallIsolated from (select EntityID, ChartersWithNetwork.OrganizationName as EntityName, ParentOrganization, ifnull(Charters4Funding.NetworkForFundingPurposes,0) as NetworkForFundingPurposes  from ChartersWithNetwork left join Charters4Funding on ChartersWithNetwork.ParentOrganization = Charters4Funding.OrganizationName) CWN left join SmallIsolatedList on CWN.EntityID = SmallIsolatedList.EntityID)CSH on kvs.EntityID = CSH.EntityID)truck left join(select car1.EntityID,PsdCapOutlayRevLimitAmt,ElemCapOutlayRevLimitAmt,HsPrlmCapOutlayRevLimitAmt,HsBooksCapOutlayRevLimitAmt,PSElTransAdj,HSTransAdj from ((select g.EntityID,g.PsdCapOutlayRevLimitAmt,g.ElemCapOutlayRevLimitAmt,g.HsPrlmCapOutlayRevLimitAmt,g.HsBooksCapOutlayRevLimitAmt from SaAporCapitalOutlayCalcs g inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporCapitalOutlayCalcs group by EntityID ) gm where g.EntityID=gm.EntityID and g.PaymentMonth=gm.MaxPaymentMonth and g.FiscalYear=2017) )bike1 left join ((select d.EntityID,d.PSElTransAdj,d.HSTransAdj from SaAporSoftCapAlloc d inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporSoftCapAlloc group by EntityID)dm where d.EntityID=dm.EntityID and d.PaymentMonth=dm.MaxPaymentMonth and d.FiscalYear=2017) )car1 on car1.EntityID=bike1.EntityID)lorry on lorry.EntityID=truck.EntityID')
    for row in result3:
        d11 = {}
        # Creating a dictionary of the values retrieved from the query
        d4 = dict(row.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS
        if (d4['Type'] == 'Charter Holder-Charter Board'):
            d4['Type'] = "Charter"
        elif (d4['Type'] == 'Charter Holder - University'):
            d4['Type'] = "Charter"
        elif (d4['Type'] == 'School District - Vocational/Technical'):
            d4['Type'] = "JTED"
        else:
            d4['Type'] = "District"
        # CALCULATION OF PERCENTAGE OF PREK_8 OF TOTAL AND HS OF TOTAL
        temp5 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[d4['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d4['EntityID']]
        temp6 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[d4['EntityID']] + \
                Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d4['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d4['EntityID']]
        temp7 = Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d4['EntityID']]
        if temp6 == 0:
            PercPreK_8ofTotal.append(float(0))
            PercHSofTotal.append(float(0))
        else:
            PercPreK_8ofTotal.append(float(temp5) / float(temp6))
            PercHSofTotal.append(float(temp7) / float(temp6))
        RCL.append(float(SumofBSL[d4['EntityID']]) + AdditionalAssistance[dd4] + OppurtunityWeight[dd4] + TRCL[dd4])
        DSL.append(float(SumofBSL[d4['EntityID']] + AdditionalAssistance[dd4] + OppurtunityWeight[dd4] + TSL[dd4]))
        TotalStateEqualisationFunding.append(min(RCL[dd4], DSL[dd4]))
        # CALCULATION OF ELEMENTARY AND HSTOTALSTATE FORMULA

        ElemTotalStateFormula.append(float(TotalStateEqualisationFunding[dd4]) * float(PercPreK_8ofTotal[dd4]))
        HSTotalStateFormula.append(float(TotalStateEqualisationFunding[dd4]) * float(PercHSofTotal[dd4]))
        # CALCULATION OF lOCAL LEVY
        if d4['TotalHSAssessValAmt'] == None:
            d4['TotalHSAssessValAmt'] = 0
        HSAssessedValuation.append(float(d4['TotalHSAssessValAmt']))
        if HSADM[dd4] == 0:
            HSQTRYield.append(0)
        elif d4['Type'] == "JTED":
            HSQTRYield.append(float(HSAssessedValuation[dd4]) * float(0.01) * float(QTRJTED))
        else:
            HSQTRYield.append(float(HSAssessedValuation[dd4]) * float(0.01) * float(QTR9_12))
        HSLL.append(min(HSTotalStateFormula[dd4], HSQTRYield[dd4]))
        if d4['TotalPSElAssessValAmt'] == None:
            d4['TotalPSElAssessValAmt'] = 0
        ElemAssessedValuation.append(float(d4['TotalPSElAssessValAmt']))
        if ELEMADM[dd4] == 0:
            ElemQTRYield.append(0)
        else:
            ElemQTRYield.append(float(ElemAssessedValuation[dd4]) * float(QTRK_8) * float(0.01))
        ElemLL.append(min(ElemTotalStateFormula[dd4], ElemQTRYield[dd4]))
        TotalLocalLevy.append(ElemLL[dd4] + HSLL[dd4])
        # CALCUALTION OF TOTAL STATE AID
        if ElemTotalStateFormula[dd4] > ElemQTRYield[dd4]:
            ElemStateAid.append(float(ElemTotalStateFormula[dd4] - ElemQTRYield[dd4]))
        else:
            ElemStateAid.append(0)
        if HSTotalStateFormula[dd4] > HSQTRYield[dd4]:
            HSStateAid.append(float(HSTotalStateFormula[dd4] - HSQTRYield[dd4]))
        else:
            HSStateAid.append(0)
        TotalStateAid.append(ElemStateAid[dd4] + HSStateAid[dd4])
        # CALCULATION OF NO STATE AID
        if ((float(PREKADM[dd4]) + float(ELEMADM[dd4])) > 0) and (float(ElemStateAid[dd4]) == 0):
            ElemNoStateAidDistrict.append(float(1))
        else:
            ElemNoStateAidDistrict.append(float(0))
        if (HSADM[dd4] > 0) and (HSStateAid[dd4] == 0):
            HSNoStateAidDistrict.append(float(1))
        else:
            HSNoStateAidDistrict.append(float(0))
        if ((float(ElemNoStateAidDistrict[dd4]) + float(HSNoStateAidDistrict[dd4])) > 0) and (float(TotalStateAid[dd4]) == 0):
            NoStateAidDistrict.append(float(1))
        else:
            NoStateAidDistrict.append(float(0))
        TotalQTRYield.append(float(ElemQTRYield[dd4] + HSQTRYield[dd4]))
        UncapturedQTR.append(float(TotalQTRYield[dd4] - TotalLocalLevy[dd4]))
        TotalStateFundingEqualised.append(float(ElemTotalStateFormula[dd4] + HSTotalStateFormula[dd4]))

        if d4['ESSmallIsolated'] == None:
            d4['ESSmallIsolated'] = 0
        if d4['HSSmallIsolated']==None:
            d4['HSSmallIsolated']=0
        d11['ElemAssessedValuation']=str(round(ElemAssessedValuation[dd4],4))
        d11['ElemQTRYield'] =str(round(ElemQTRYield[dd4], 4))
        d11['ElemTotalStateFormula']=str(round(ElemTotalStateFormula[dd4], 4))
        d11['DistrictPreKElemReduction']=str(round(DistrictPreKElemReduction[dd4], 4))
        d11['DistrictHSReduction'] = str(round(DistrictHSReduction[dd4], 4))
        d11['TotalDistrictAAReduction'] = str(round(TotalDistrictAAReduction[dd4], 4))
        d11['NetworkForFundingPurposes']=str(d4['NetworkForFundingPurposes'])
        d11['EntityID'] = EID[dd4]
        d11['prekadm'] = str(round(PREKADM[dd4], 4))
        d11['NoStateAidDistrict'] = str(round(NoStateAidDistrict[dd4], 4))
        d11['EntityName'] = Ename[dd4]
        d11['County'] = d4['County']
        d11['AOI'] = str(d4['FTFStatus'])
        d11['TEI'] = str(round(TEI[dd4], 5))
        d11['DistrictHSAA'] = str(round(DistrictHSAA[dd4], 5))
        d11['DistrictElemAA'] = str(round(DistrictElemAA[dd4], 5))
        d11['DistrictPreKAA'] = str(round(DistrictPreKAA[dd4], 5))
        d11['hsadm'] = str(round(HSADM[dd4], 4))
        d11['elemadm'] = str(round(ELEMADM[dd4], 4))
        d11['prekbsl'] = str(round(PrekBSL[dd4], 4))
        d11['elembsl'] = str(round(ELEMBSL[dd4], 4))
        d11['hsbsl'] = str(round(HSBSL[dd4], 4))
        d11['BSL'] = str(round(BSL[dd4], 2))
        d11['SumofBSL']=str(round(SumofBSL[d4['EntityID']], 4))
        d11['WeightedPreKCounts'] = str(round(WeightedPreKCounts[dd4], 3))
        d11['WeightedElemCounts'] = str(round(WeightedElemCounts[dd4], 3))
        d11['WeightedHSCounts'] = str(round(WeightedHSCounts[dd4], 3))
        d11['TotalLocalLevy'] = str(round(TotalLocalLevy[dd4], 3))
        d11['UncapturedQTR'] = str(round(UncapturedQTR[dd4], 3))
        d11['TotalStateAid'] = str(round(TotalStateAid[dd4], 3))
        d11['Final_K_8SmWgt'] = str(round(Final_K_8SmWgt[dd4], 3))
        d11['Final_9_12SmWgt'] = str(round(Final_9_12SmWgt[dd4], 3))
        d11['RCL'] = str(round(RCL[dd4], 4))
        d11['TRCL'] = str(round(TRCL[dd4], 4))
        d11['DSL'] = str(round(DSL[dd4], 4))
        d11['TSL'] = str(round(TSL[dd4], 4))
        d11['LEABaseLevel'] = str(round(LEABaseLevel[dd4], 4))
        d11['BSLWithoutAdjustment']=str(round(BSLWithoutAdjustment[dd4],4))
        d11['PreKWeightedPupilsuser_specifiedSWWreduction'] = str(round(PreKWeightedPupilsuser_specifiedSWWreduction[dd4], 4))
        d11['K_8WeightedPupilsuser_specifiedSWWreduction'] = str(round(K_8WeightedPupilsuser_specifiedSWWreduction[dd4], 4))
        d11['nine_12WeightedPupilsuser_specifiedSWWreduction'] = str(round(nine_12WeightedPupilsuser_specifiedSWWreduction[dd4], 4))
        d11['TotalStateFundingEqualised'] = str(round(TotalStateFundingEqualised[dd4], 4))
        d11['NetworkElemADM'] = str(round(NetworkElemADM[dd4], 4))
        d11['NetworkHSADM'] = str(round(NetworkHSADM[dd4], 4))
        d11['PREKADM'] = str(round(PREKADM[dd4], 4))
        d11['ELEMADM'] = str(round(ELEMADM[dd4], 4))
        d11['HSADM'] = str(round(HSADM[dd4], 4))
        d11['GroupBWeightedAddonCounts'] = str(round(GroupBWeightedAddonCounts[dd4], 3))
        d11['SSWELEMINCREMENTALWEIGHTPP'] = str(round(SSWELEMINCREMENTALWEIGHTPP[dd4], 3))
        d11['ElemBaseWeight'] = str(round(ElemBaseWeight[dd4], 3))
        d11['GroupBBSL'] = str(round(GroupBBSL[dd4], 2))
        d11['HSBSL'] = str(round(HSBSL[dd4], 2))
        d11['AuditBaseLevelAdjustment'] = str(round(AuditBaseLevelAdjustment[dd4], 3))
        d11['ELEMRange'] = (ELEMRange[dd4])
        d11['AdditionalAssistance']=AdditionalAssistance[dd4]
        d11['ElemBSL'] = str(round(ELEMBSL[dd4], 3))
        # print(type(d4['ESSmallIsolated']))
        d11['ESSmallIsolated'] = str(round(d4['ESSmallIsolated'], 3))
        d11['HSSmallIsolated'] = str(round(d4['HSSmallIsolated'], 3))
        d11['GB1_EDMIDSLD'] = str(round(GB1_EDMIDSLD[dd4], 3))
        d11['GB2_K3Reading'] = str(round(GB2_K3Reading[dd4], 3))
        d11['GB4_ELL'] = str(round(GB4_ELL[dd4], 3))
        d11['GB5_OI_R'] = str(round(GB5_OI_R[dd4], 3))
        d11['GB6_PS_D'] = str(round(GB6_PS_D[dd4], 3))
        d11['GB7_MOID'] = str(round(GB7_MOID[dd4], 3))
        d11['GB8_HI'] = str(round(GB8_HI[dd4], 3))
        d11['GB9_VI'] = str(round(GB9_VI[dd4], 3))
        d11['GB10_ED_P'] = str(round(GB10_ED_P[dd4], 4))
        d11['GB11_MDSC'] = str(round(GB11_MDSC[dd4], 4))
        d11['GB12_MD_R'] = str(round(GB12_MD_R[dd4], 4))
        d11['GB13_OI_SC'] = str(round(GB13_OI_SC[dd4], 4))
        d11['GB14_MD_SSI'] = str(round(GB14_MD_SSI[dd4], 4))
        d11['TotalFormulaDistrictAA'] = str(round(TotalFormulaDistrictAA[dd4], 4))
        d11['TotalNetDistrictAA'] = str(round(TotalNetDistrictAA[dd4], 4))
        d11['FinalFormulaAAwithReduction'] = str(round(FinalFormulaAAwithReduction[dd4], 4))
        d11['FinalFormulaAdditionalAssistance'] = str(round(FinalFormulaAdditionalAssistance[dd4], 4))
        d11['ElemLL'] = str(round(ElemLL[dd4], 4))
        d11['HSLL'] = str(round(HSLL[dd4], 4))
        D.append(d11)
        dd4 += 1

    return flask.render_template('table2.html', string1=D)


if __name__ == '__main__':
    app.run()
