import flask
from sqlalchemy import create_engine
import json
import os
import pandas as pd
import decimal,time, datetime
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
            return flask.render_template('yearselect.html')

    if ll == 0:
        error = 'Invalid Credentials. Please try again.'
        return flask.render_template("login.html", error=error)
@app.route('/yearselect',methods=['GET','POST'])
def yearselect():
    return flask.render_template('yearselect.html')
@app.route('/input',methods=['GET','POST'])
def input():
    return flask.render_template('input variables.html')
@app.route('/year',methods=['GET','POST'])
def year():
    flask.session['yearnum']=flask.request.form['yearnum']
    yearnum = int((flask.request.form['yearnum']))
    def alchemyencoder(obj):
        """JSON encoder function for SQLAlchemy special classes."""
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    def example1():
        basesup = engine.execute('SELECT min(BaseAmount) as minbase FROM DCSchoolFinance.SaAporBaseSupportLevelCalcs2 where FiscalYear=(%s)',(yearnum))
        return json.dumps([dict(r) for r in basesup], default=alchemyencoder)

    BaseSupport = (example1())
    de = json.loads(BaseSupport)
    BaseSupport = float(de[0]['minbase'])
    flask.session['basesupport'] = BaseSupport
    return flask.render_template('input variables.html')
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask.session['username'] = None
    flask.session['password'] = None
    return flask.render_template('login.html')

# Defining input variables with input values from nigel file
#start of input variables to be posted  in front end
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
Transportation123TSL = 1
TransportationPerPupilOptionTRCL = 0
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
DistrictReduction = 352442700
ActualDistrictReduction = -381355874.7
AvgDistrictPPReduction = 382.77165
AvgActualDistReduction = -414.1729064
AvgCharterPPReduction = 109.6679608
# CALCULATION OF VALUES
@app.route('/wftf', methods=['GET', 'POST'])
def wftf(yearnum,g,Yeardef):
    # start of input variables to be posted  in front end
    def alchemyencoder(obj):
        """JSON encoder function for SQLAlchemy special classes."""
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    def example1():
        basesup = engine.execute('SELECT min(BaseAmount) as minbase FROM DCSchoolFinance.SaAporBaseSupportLevelCalcs2 where FiscalYear=(%s)',(yearnum))
        # use special handler for dates and decimals
        return json.dumps([dict(r) for r in basesup], default=alchemyencoder)

    BaseSupport = (example1())
    de = json.loads(BaseSupport)
    BaseSupport=float(de[0]['minbase'])
    flask.session['yearnum'] = yearnum
    TeacherCompPercent = 1.25
    Percent200DayCalender = 5
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
    FullTimeAOI = 0.95
    HalfTimeAOI = 0.85
    QTRK_8 = 2.0793
    QTR9_12 = 2.0793
    QTRCTED = 0.05
    CharterReduction = 18656000
    CharSuppLvlAllK_8 = 1752.1
    CharSuppLvlAll9_12 = 2042.04
    GroupAFinalGroupAWeightsPSD = 1.45
    GroupAFinalGroupAWeightsK_8 = 1.158
    GroupAFinalGroupAWeights9_12 = 1.268
    GroupAFinalGroupAWeightsCTED = 1.339
    DistSuppLvlAllPSD = 450.76
    DistSuppLvl1to99K_8 = 544.58
    DistSuppLvl100to599K_8 = 389.25
    DistSuppLvl600AndOverK_8 = 450.76
    DistSuppLvl1to999_12 = 601.24
    DistSuppLvl100to5999_12 = 405.59
    DistSuppLvl600AndOver9_12 = 492.94
    TEI10 = 1
    AdditionalAssistant_eqformula = 1
    AdditonalAssistantReduction = 1
    # End of input variables to be posted  in front end
    QTRUnified = QTRK_8 + QTR9_12
    TeacherCompAmount = BaseSupport + (BaseSupport * TeacherCompPercent)
    Amount200DayCalender = BaseSupport + (BaseSupport * Percent200DayCalender)
    TeacherCompAnd200DayCalender = (BaseSupport + (BaseSupport * TeacherCompPercent)) * (1 + Percent200DayCalender)
    gi=time.time()
    #def example():
     #   preresult = engine.execute('select truck.*,lorry.PsdCapOutlayRevLimitAmt,lorry.ElemCapOutlayRevLimitAmt,lorry.HsPrlmCapOutlayRevLimitAmt,lorry.HsBooksCapOutlayRevLimitAmt,lorry.PSElTransAdj,lorry.HSTransAdj from (select kvs.*, CSH.parentOrganization, CSH.NetworkForFundingPurposes, CSH.ESSmallIsolated, CSH.HSSmallIsolated from (select ftfmaintype.*,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (Select ftfmain.*,EntityName,Entityshort.County,Entityshort.Type from (select EntityID, sum(PsdCount) as sumOfPsdCount,sum(PsdCYCount) as sumOfPsdCYCount,sum(ElemCount) as sumOfElemCount,sum(ElemCYCount) as sumOfElemCYCount,sum(DSCSElemCnt) as sumOfDSCSElemCount,sum(HsCount) as sumOfHsCount,sum(HsCYCount) as sumOfHsCYCount, sum(DSCSHsCnt) as sumOfDSCSHsCount, FiscalYear,TEI,BaseAmount as MaxOfBaseAmount,BaseAdjsAmount as MaxofBaseAdjsAmount, sum(MDSSICnt) as sumOfMDSSICnt,sum(MDSSICYCnt) as sumOfMDSSICYCnt, sum(DSCSMDSSICnt)as sumOfDSCSMDSSICnt, sum(DSCSVICnt)as sumOfDSCSVICnt, sum(DSCSOISCCnt) as sumOfDSCSOISCCnt, sum(DSCSPSDCnt)as sumOfDSCSPSDCnt, sum(DSCSMDSCCnt)as sumOfDSCSMDSCCnt, sum(DSCSHICnt)as sumOfDSCSHICnt, sum(DSCSMOMRCnt)as sumOfDSCSMOMRCnt, sum(DSCSEDPPrivateCnt)as sumOfDSCSEDPPrivateCnt, sum(DSCSMDResCnt)as sumOfDSCSMDResCnt, sum(DSCSOIResCnt)as sumOfDSCSOIResCnt, sum(DSCSEDMIMRCnt)as sumOfDSCSEDMIMRCnt, sum(DSCSLEPCnt)as sumOfDSCSLEPCnt, sum(DSCSK3Cnt)as SumOfDSCSK3Cnt,sum(PSDCnt)as sumOfPSDCnt, sum(PSDCYCnt)as sumOfPSDCYCnt,sum(VICnt)as sumOfVICnt, sum(VICYCnt)as sumOfVICYCnt, sum(OISCCnt)as sumOfOISCCnt, sum(OISCCYCnt)as sumOfOISCCYCnt, sum(MDSCCnt)as sumOfMDSCCnt, sum(MDSCCYCnt)as sumOfMDSCCYCnt,sum(HICYCnt)as sumOfHICYCnt,sum(HICnt)as sumOfHICnt,sum(MOMRCnt)as sumOfMOMRCnt, sum(MOMRCYCnt)as sumOfMOMRCYCnt, sum(EDPPrivateCYCnt)as sumOfEDPPrivateCYCnt,sum(EDPPrivateCnt)as sumOfEDPPrivateCnt,sum(MDResCnt)as sumOfMDResCnt, sum(MDResCYCnt)as sumOfMDResCYCnt,sum(OIResCnt)as sumOfOIResCnt, sum(OIResCYCnt)as sumOfOIResCYCnt,sum(EDMIMRCYCnt)as sumOfEDMIMRCYCnt, sum(EDMIMRCnt)as sumOfEDMIMRCnt,sum(LEPCnt)as sumOfLEPCnt, sum(LEPCYCnt)as sumOfLEPCYCnt, sum(K3Cnt)as sumOfK3Cnt,sum(K3CYCnt)as sumOfK3CYCnt, FTFStatus from ((select t.EntityID,t.FiscalYear,t.PsdCYCount,t.PsdCount,t.ElemCYCount,t.ElemCount,t.DSCSElemCnt,t.HsCYCount,t.HsCount,t.DSCSHsCnt,t.DSCSK3Cnt,t.TEI,t.PaymentMonth,t.FTFStatus,t.BaseAmount,t.BaseAdjsAmount,t.MDSSICnt,t.MDSSICYCnt,t.DSCSMDSSICnt, t.DSCSVICnt,t.DSCSOISCCnt,t.DSCSPSDCnt,t.DSCSMDSCCnt,t.DSCSHICnt,t.DSCSMOMRCnt,t.DSCSEDPPrivateCnt,t.DSCSMDResCnt,t.DSCSOIResCnt,t.DSCSEDMIMRCnt,t.DSCSLEPCnt,t.PSDCYCnt,t.PSDCnt,t.VICYCnt,t.VICnt,t.OISCCYCnt,t.OISCCnt,t.MDSCCYCnt, t.MDSCCnt,t.HICYCnt,t.HICnt,t.MOMRCYCnt,t.MOMRCnt,t.EDPPrivateCYCnt,t.EDPPrivateCnt,t.MDResCYCnt,t.MDResCnt,t.OIResCYCnt,t.OIResCnt,t.EDMIMRCYCnt,t.EDMIMRCnt,t.LEPCYCnt,t.LEPCnt,t.K3CYCnt,t.K3Cnt from SaAporBaseSupportLevelCalcs2 t use index(aporbasei,aporbase2,aporbasei3,aporbasei4,aporbasei5) inner join (select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporBaseSupportLevelCalcs2 use index(aporbasei,aporbase2,aporbasei3,aporbasei4,aporbasei5) group by EntityID) tm on t.EntityID=tm.EntityID and t.PaymentMonth=tm.MaxPaymentMonth and t.FiscalYear=(%s)) union all select yy.EntityID,yy.FiscalYear,yy.PsdCYCount,yy.PsdCount,yy.ElemCYCount, yy.ElemCount, yy.DSCSElemCnt,yy.HsCYCount,yy.HsCount,yy.DSCSHsCnt,yy.DSCSK3Cnt,yy.TEI,yy.PaymentMonth,yy.FTFStatus,yy.BaseAmount,yy.BaseAdjsAmount, yy.MDSSICnt, yy.MDSSICYCnt,yy.DSCSMDSSICnt, yy.DSCSVICnt,yy.DSCSOISCCnt,yy.DSCSPSDCnt,yy.DSCSMDSCCnt,yy.DSCSHICnt,yy.DSCSMOMRCnt,yy.DSCSEDPPrivateCnt,yy.DSCSMDResCnt,yy.DSCSOIResCnt,yy.DSCSEDMIMRCnt,yy.DSCSLEPCnt,yy.PSDCYCnt,yy.PSDCnt, yy.VICYCnt,yy.VICnt,yy.OISCCYCnt,yy.OISCCnt,yy.MDSCCYCnt, yy.MDSCCnt,yy.HICYCnt,yy.HICnt,yy.MOMRCYCnt,yy.MOMRCnt,yy.EDPPrivateCYCnt, yy.EDPPrivateCnt,yy.MDResCYCnt,yy.MDResCnt,yy.OIResCYCnt,yy.OIResCnt, yy.EDMIMRCYCnt,yy.EDMIMRCnt,yy.LEPCYCnt,yy.LEPCnt,yy.K3CYCnt,yy.K3Cnt from SaCharBaseSupportLevelCalcs2 yy use index(cbasei,cbasei2,cbasei3,cbasei4) inner join (select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaCharBaseSupportLevelCalcs2 use index(cbasei,cbasei2,cbasei3,cbasei4) group by EntityID)ym on yy.EntityId=ym.EntityID and yy.PaymentMonth=ym.MaxPaymentMonth and yy.FiscalYear=(%s))uni where FiscalYear=(%s) group by EntityID,FTFStatus )ftfmain left join (select EntityID,EntityName,County,Entity.Type from Entity)Entityshort on ftfmain.EntityID=Entityshort.EntityID )ftfmaintype left join (select TRCLTSL.EntityID,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (select TRCL.EntityID,TRCL,TSL from ((select j.EntityID,j.TRCL from SaAporTransRevCtlLimit2 j  Use index(TRCLi) inner join ( select EntityID,max(PaymentMonth)as MaxPaymentMonth from SaAporTransRevCtlLimit2 Use index(TRCLi) group by EntityID) jm on j.EntityID=jm.EntityID and j.PaymentMonth=jm.MaxPaymentMonth and j.FiscalYear=(%s)))TRCL left join ((select k.EntityID,k.TSL from SaAporTransSupptLvl2 k use index(TSLi)  inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporTransSupptLvl2 use index(TSLi) group by EntityID)km where k.EntityID=km.EntityID and k.PaymentMonth=km.MaxPaymentMonth and k.FiscalYear=(%s)))TSL on TRCL.EntityID=TSL.EntityID)TRCLTSL left join ((Select l.EntityID,l.TotalPSElAssessValAmt,l.TotalHSAssessValAmt from SaAporQualLevy2 l use index(quallevyi) inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporQualLevy2 use index(quallevyi) group by EntityID)lm where l.EntityID=lm.EntityID and l.PaymentMonth=lm.MaxPaymentMonth and l.FiscalYear=(%s)))PSEl on TRCLTSL.EntityID=PSEl.EntityID )Bike on ftfmaintype.EntityID=Bike.EntityID) kvs left join (select s1.EntityID, s1.Name as EntityName, CWN.parentOrganization, CWN.NetworkForFundingPurposes, s1.ESSmallIsolated, s1.HSSmallIsolated from (select EntityID, ChartersWithNetwork.OrganizationName as EntityName, ParentOrganization, ifnull(Charters4Funding.NetworkForFundingPurposes,0) as NetworkForFundingPurposes  from ChartersWithNetwork use index(chneti) left join Charters4Funding use index(charfundi) on ChartersWithNetwork.ParentOrganization = Charters4Funding.OrganizationName) CWN right join SmallIsolatedList s1 use index(smallisoi) on CWN.EntityID = s1.EntityID)CSH on kvs.EntityID = CSH.EntityID)truck left join(select car1.EntityID,PsdCapOutlayRevLimitAmt,ElemCapOutlayRevLimitAmt,HsPrlmCapOutlayRevLimitAmt,HsBooksCapOutlayRevLimitAmt,PSElTransAdj,HSTransAdj from ((select g.EntityID,g.PsdCapOutlayRevLimitAmt,g.ElemCapOutlayRevLimitAmt,g.HsPrlmCapOutlayRevLimitAmt,g.HsBooksCapOutlayRevLimitAmt from SaAporCapitalOutlayCalcs2 g use index(acapoutlaycalci) inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporCapitalOutlayCalcs2 use index(acapoutlaycalci) group by EntityID ) gm where g.EntityID=gm.EntityID and g.PaymentMonth=gm.MaxPaymentMonth and g.FiscalYear=(%s)) )bike1 left join ((select d.EntityID,d.PSElTransAdj,d.HSTransAdj from SaAporSoftCapAlloc2 d use index(aporsoftcapi) inner join (Select EntityID,max(PaymentMonth) as MaxPaymentMonth from SaAporSoftCapAlloc2 use index(aporsoftcapi)group by EntityID)dm where d.EntityID=dm.EntityID and d.PaymentMonth=dm.MaxPaymentMonth and d.FiscalYear=(%s)) )car1 on car1.EntityID=bike1.EntityID)lorry on lorry.EntityID=truck.EntityID',(yearnum,yearnum,yearnum,yearnum,yearnum,yearnum,yearnum,yearnum))
        # use special handler for dates and decimals
      #  return json.dumps([dict(r) for r in preresult], default=alchemyencoder)
    counter1 = 0
    #g = example()
    decoded = json.loads(g)
    # ASSIGNING VARIABLES FOR CALCULATION
    # DEFINING VARIABLES FOR FURTHER CALCULATION
    sumprekadm={}
    sumelemadm={}
    sumhsadm={}
    Final_9_12SmWgt={}
    Final_K_8SmWgt={}
    AuditBaseLevelAdjustment=[]
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
    HSBaseWeight={}
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
    bslbytype = {}
    admbytype = {}
    bslbyEHType = {}
    admbyEHType = {}
    bslbyCounty={}
    admbyCounty={}
    perpupilbyCounty={}
    FinalFormulaAAwithReduction = []
    AdditionalAssistance = []
    EqualisationBase=[]
    Equalisationassistance=[]
    Reductionsum=0
    sumHSTution=0
    sumTotalLocalLevydefault=0
    sumTotalStateAiddefualt=0
    sumtotalqtryeild=0
    sumtotaluncapturedqtr=0
    sumtotaladditionalassistancedefault=0
    CAAdefault=0
    DAAdefault=0
    HSRange = {}
    ELEMRange = {}
    TotalStateEqualisationFunding = []
    OppurtunityWeight = []
    TRCL = []
    sumtrcl=0
    TSL = []
    sumtsl=0
    RCL = []
    sumrcl=0
    DSL = []
    sumdsl=0
    TeacherComp = []
    Basecompflag=[]
    twohundereddaycalendar = []
    techercompand200daycalender = []
    SumofPreKWeightedPupilsuser_specifiedSWWreduction = {}
    Sumofk_8WeightedPupilsuser_specifiedSWWreduction = {}
    Sumof9_12WeightedPupilsuser_specifiedSWWreduction = {}
    sumCharterElemADM={}
    sumCharterHSADM={}
    BSLWithoutAdjustment=[]
    SumofBSL={}
    sumofadm = {}
    perpupilpertype = {}
    perpupilbyEHType={}
    # STORE THE NETWORK NAMES
    parentorg = engine.execute('select distinct (ParentOrganization) from ChartersWithNetwork')
    for row2 in parentorg:
        d2 = row2[0]
        if d2 != '':
            sumofnetworkelemadm[d2]=0
            sumofnetworkhsadm[d2]=0
    count = 0
    schooltype = {}

    schoolEHType={}
    schooltypeanddistricttype = {}
    admbyschooltype = {}
    bslbyschooltype = {}
    admbyschooltypeanddistricttype = {}
    bslbyschooltypeanddistricttype = {}
    perpupilbyschooltypeanddistricttype = {}
    perpupilbyschooltype = {}
    # CALCULATION OF ADM VALUES
    for pred in decoded:
        #pred = dict(prerow.items())
        entityid = pred['EntityID']
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS
        if (pred['EHType'] == 'Charter Holder - University' or pred['EHType'] == 'Charter Holder-Charter Board'):
            pred['EHType'] = "Charter"

        elif (pred['EHType'] == 'School District - Vocational/Technical'):
            pred['EHType'] = "CTED"
        elif (pred['EHType'] == None):
            pred['EHType']="None"
        elif (pred['EHType'] == 'School District - Accommodation'):
            pred['EHType'] = "Accomodation"
        elif (pred['EHType'] == 'School District - Elementary In High School'):
            pred['EHType'] = "Elementary with HS Students"
        elif (pred['EHType'] == "School District - Elementary Not In High School"):
            pred['EHType'] = "Elementary district"
        elif (pred['EHType'] == "School District - Unified"):
            pred['EHType'] = "Unified district"
        schoolEHType[pred['EntityID']] = pred['EHType']
        if (pred['Type'] == 'Charter Holder-Charter Board'):
            pred['Type'] = "Charter"
        elif (pred['Type'] == 'Charter Holder - University'):
            pred['Type'] = "Charter"
        elif (pred['Type'] == 'School District - Vocational/Technical'):
            pred['Type'] = "CTED"
        else:
            pred['Type'] = "District"
        # calculation of PREKADM
        if Yeardef=="CY" and (pred['Type']!="Charter" and pred['Type']!="CTED"):
            if pred['sumOfPsdCYCount'] == None:
                pred['sumOfPsdCYCount'] = 0
            PREKADM.append(float(pred['sumOfPsdCYCount']))
            if pred['sumOfElemCYCount'] == None:
                pred['sumOfElemCYCount'] = 0
            if pred['sumOfDSCSElemCount'] == None:
                pred['sumOfDSCSElemCount'] = 0
            ELEMADM.append(float(pred['sumOfElemCYCount']) + float(pred['sumOfDSCSElemCount']))
            # CALCULATION OF HSADM VALUE
            if pred['sumOfHsCYCount'] == None:
                pred['sumOfHsCYCount'] = 0
            if pred['sumOfDSCSHsCount'] == None:
                pred['sumOfDSCSHsCount'] = 0
            HSADM.append(float(pred['sumOfHsCYCount']) + float(pred['sumOfDSCSHsCount']))
        else:
            if pred['sumOfPsdCount'] == None:
                pred['sumOfPsdCount'] = 0
            PREKADM.append(float(pred['sumOfPsdCount']))
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
        # CALCULATION OF ELEM ADM
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
        sumofadm[pred['EntityID']] = 0
        # if (PREKADM[count] == 0 and ELEMADM[count] == 0 and HSADM[count] == 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "novalue"
        # elif (PREKADM[count] == 0 and ELEMADM[count] == 0 and HSADM[count] > 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "High School District"
        #
        # elif (PREKADM[count] == 0 and ELEMADM[count] > 0 and HSADM[count] == 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Elementary District"
        #
        # elif (PREKADM[count] == 0 and ELEMADM[count] > 0 and HSADM[count] > 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Unified District"
        #
        # elif (PREKADM[count] > 0 and ELEMADM[count] == 0 and HSADM[count] == 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Nottype"
        #
        # elif (PREKADM[count] > 0 and ELEMADM[count] == 0 and HSADM[count] > 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Nottype"
        #
        # elif (PREKADM[count] > 0 and ELEMADM[count] > 0 and HSADM[count] == 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Elementary District"
        #
        # elif (PREKADM[count] > 0 and ELEMADM[count] > 0 and HSADM[count] > 0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']] = "Unified District"

        # calcschooltypeanddistricttype

        # if schooltype[pred['EntityID']] == "novalue" and pred['Type'] == "Charter":
        #     schooltypeanddistricttype[pred['EntityID']] = "novalue and Charter"
        #
        # elif schooltype[pred['EntityID']] == "High School District" and pred['Type'] == "Charter":
        #     schooltypeanddistricttype[pred['EntityID']] = "High School District and Charter"
        #
        # elif schooltype[pred['EntityID']] == "Elementary District" and pred['Type'] == "Charter":
        #     schooltypeanddistricttype[pred['EntityID']] = "Elementary District and Charter"
        #
        # elif schooltype[pred['EntityID']] == "Unified District" and pred['Type'] == "Charter":
        #     schooltypeanddistricttype[pred['EntityID']] = "Unified District and Charter"
        #
        # elif schooltype[pred['EntityID']] == "Nottype" and pred['Type'] == "Charter":
        #     schooltypeanddistricttype[pred['EntityID']] = "Nottype and Charter"
        #
        # if schooltype[pred['EntityID']] == "novalue" and pred['Type'] == "CTED":
        #     schooltypeanddistricttype[pred['EntityID']] = "novalue and CTED"
        #
        # elif schooltype[pred['EntityID']] == "High School District" and pred['Type'] == "CTED":
        #     schooltypeanddistricttype[pred['EntityID']] = "High School District and CTED"
        #
        # elif schooltype[pred['EntityID']] == "Elementary District" and pred['Type'] == "CTED":
        #     schooltypeanddistricttype[pred['EntityID']] = "Elementary District and CTED"
        #
        # elif schooltype[pred['EntityID']] == "Unified District" and pred['Type'] == "CTED":
        #     schooltypeanddistricttype[pred['EntityID']] = "Unified District and CTED"
        #
        # elif schooltype[pred['EntityID']] == "Nottype" and pred['Type'] == "CTED":
        #     schooltypeanddistricttype[pred['EntityID']] = "Nottype and CTED"
        #
        # if schooltype[pred['EntityID']] == "novalue" and pred['Type'] == "District":
        #     schooltypeanddistricttype[pred['EntityID']] = "novalue and District"
        #
        # elif schooltype[pred['EntityID']] == "High School District" and pred['Type'] == "District":
        #     schooltypeanddistricttype[pred['EntityID']] = "High School District and District"
        #
        # elif schooltype[pred['EntityID']] == "Elementary District" and pred['Type'] == "District":
        #     schooltypeanddistricttype[pred['EntityID']] = "Elementary District and District"
        #
        # elif schooltype[pred['EntityID']] == "Unified District" and pred['Type'] == "District":
        #     schooltypeanddistricttype[pred['EntityID']] = "Unified District and District"
        #
        # elif schooltype[pred['EntityID']] == "Nottype" and pred['Type'] == "District":
        #     schooltypeanddistricttype[pred['EntityID']] = "Nottype and District"

        count += 1
    entitynull=[]
    for d in decoded:
        # Creating a dictionary of the values retrieved from the query
        #d = dict(row.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS

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
            if NetworkHSADM[counter1] >= float(1) and NetworkHSADM[counter1] < float(100):
                HSRange[d['EntityID']]=("1to99")
            elif NetworkHSADM[counter1] >= float(100) and NetworkHSADM[counter1] < float(500):
                HSRange[d['EntityID']]=("100to499")
            elif NetworkHSADM[counter1] >= (float(500)) and NetworkHSADM[counter1] < (float(600)):
                HSRange[d['EntityID']]=("500to599")
            elif (NetworkHSADM[counter1] >= float(600)):
                HSRange[d['EntityID']]=(">600")
            else:
                HSRange[d['EntityID']]=(None)
            if NetworkElemADM[counter1] >= float(1) and NetworkElemADM[counter1] < float(100):
                ELEMRange[d['EntityID']]=("1to99")
            elif NetworkElemADM[counter1] >= float(100) and NetworkElemADM[counter1] < float(500):
                ELEMRange[d['EntityID']]=("100to499")
            elif NetworkElemADM[counter1] >= (float(500)) and NetworkElemADM[counter1] < (float(600)):
                ELEMRange[d['EntityID']]=("500to599")
            elif (NetworkElemADM[counter1] >= float(600)):
                ELEMRange[d['EntityID']]=(">600")
            else:
                ELEMRange[d['EntityID']]=(None)
        else:
            NetworkElemADM.append(0)
            NetworkHSADM.append(0)
            if sumhsadm[d['EntityID']] >= float(1) and sumhsadm[d['EntityID']] < float(100):
                HSRange[d['EntityID']]=("1to99")
            elif sumhsadm[d['EntityID']] >= float(100) and sumhsadm[d['EntityID']] < float(500):
                HSRange[d['EntityID']]=("100to499")
            elif sumhsadm[d['EntityID']] >= (float(500)) and sumhsadm[d['EntityID']] < (float(600)):
                HSRange[d['EntityID']]=("500to599")
            elif (sumhsadm[d['EntityID']] >= float(600)):
                HSRange[d['EntityID']]=(">600")
            else:
                HSRange[d['EntityID']]=(None)
            if sumelemadm[d['EntityID']] >= float(1) and sumelemadm[d['EntityID']] < float(100):
                ELEMRange[d['EntityID']]=("1to99")
            elif sumelemadm[d['EntityID']] >= float(100) and sumelemadm[d['EntityID']] < float(500):
                ELEMRange[d['EntityID']]=("100to499")
            elif sumelemadm[d['EntityID']] >= (float(500)) and sumelemadm[d['EntityID']] < (float(600)):
                ELEMRange[d['EntityID']]=("500to599")
            elif (sumelemadm[d['EntityID']] >= float(600)):
                ELEMRange[d['EntityID']]=(">600")
            else:
                ELEMRange[d['EntityID']]=(None)
        #CALCULATION OF SSWHSINCREMENTALWEIGHTPP
        if (d['Type'] == "CTED"):
            SSWHSINCREMENTALWEIGHTPP.append(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[d['EntityID']] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
            else:
                if HSRange[d['EntityID']] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
        #CALCULATION OF FinalHSBASEWEIGHT
        if (d['Type'] == "CTED"):
            HSBaseWeight[d['EntityID']]=(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[d['EntityID']] == "1to99":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso500to5999_12)
                else:
                    HSBaseWeight[d['EntityID']]=(0)
            else:
                if HSRange[d['EntityID']] == "1to99":
                    HSBaseWeight[d['EntityID']]=(WtSmall1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    HSBaseWeight[d['EntityID']]=(WtSmall100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    HSBaseWeight[d['EntityID']]=(WtSmall500to5999_12)
                else:
                    HSBaseWeight[d['EntityID']]=(0)
        if HSRange[d['EntityID']]==None and ELEMRange[d['EntityID']]==None:
             entitynull.append(d['EntityID'])
        #     bothnull+=1
        # totalcount+=1
        #CALCUATION OF Final9-12WEIGHT
        if d['Type'] == "CTED":
            Final_9_12SmWgt[d['EntityID']]=(GroupAFinalGroupAWeightsCTED)
        else:
            if HSRange[d['EntityID']] == ">600":
                Final_9_12SmWgt[d['EntityID']]=(GroupAFinalGroupAWeights9_12)
            elif HSRange[d['EntityID']] == "1to99":
                Final_9_12SmWgt[d['EntityID']]=(HSBaseWeight[d['EntityID']])
            elif HSRange[d['EntityID']] == "100to499":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (
                                float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (
                            float(float(500) - float(NetworkHSADM[counter1])))))
                else:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (
                                float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (
                            float(float(500) - float(sumhsadm[d['EntityID']])))))
            elif HSRange[d['EntityID']] == "500to599":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (
                                float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (
                            float(float(600) - float(NetworkHSADM[counter1])))))
                else:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (
                                float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (
                            float(float(600) - float(sumhsadm[d['EntityID']])))))
            else:
                Final_9_12SmWgt[d['EntityID']]=(GroupAFinalGroupAWeights9_12)
        # CALCULATION OF SSWELEMINCREMENTALWEIGHTPP
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[d['EntityID']] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        else:
            if ELEMRange[d['EntityID']] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        # CALCULATION OF FINALELEMBASEWEIGHT
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[d['EntityID']] == "1to99":
                ElemBaseWeight.append(WtSmallIso1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                ElemBaseWeight.append(WtSmallIso100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                ElemBaseWeight.append(WtSmallIso500to599K_8)
            else:
                ElemBaseWeight.append(0)
        else:
            if ELEMRange[d['EntityID']] == "1to99":
                ElemBaseWeight.append(WtSmall1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                ElemBaseWeight.append(WtSmall100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                ElemBaseWeight.append(WtSmall500to599K_8)
            else:
                ElemBaseWeight.append(0)
        # CALCUATION OF K-8WEIGHT
        if ELEMRange[d['EntityID']] == ">600":
            Final_K_8SmWgt[d['EntityID']]=(GroupAFinalGroupAWeightsK_8)
        elif ELEMRange[d['EntityID']] == "1to99":
            Final_K_8SmWgt[d['EntityID']]=(ElemBaseWeight[counter1])
        elif ELEMRange[d['EntityID']] == "100to499":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (
                            float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(500 - NetworkElemADM[counter1]))))
            else:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (
                            float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(500 - sumelemadm[d['EntityID']]))))
        elif ELEMRange[d['EntityID']] == "500to599":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (
                            float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(600 - NetworkElemADM[counter1]))))
            else:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (
                            float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(600 - sumelemadm[d['EntityID']]))))
        else:
            Final_K_8SmWgt[d['EntityID']]=(GroupAFinalGroupAWeightsK_8)
        # CALCULATION OF VARIABLES FOR GROUP B WEIGHTS
        if Yeardef=="PY":
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
        elif Yeardef=="CY":
            if d['sumOfDSCSEDMIMRCnt'] == None:
                d['sumOfDSCSEDMIMRCnt'] = 0
            if d['sumOfEDMIMRCYCnt'] == None:
                d['sumOfEDMIMRCYCnt'] = 0
            GB1_EDMIDSLD.append(float(d['sumOfEDMIMRCYCnt']) + float(d['sumOfDSCSEDMIMRCnt']))
            if d['sumOfK3CYCnt'] == None:
                d['sumOfK3CYCnt'] = 0
            if d['SumOfDSCSK3Cnt'] == None:
                d['SumOfDSCSK3Cnt'] = 0
            GB2_K3Reading.append(float(d['sumOfK3CYCnt']) + float(d['SumOfDSCSK3Cnt']))
            GB3_K3.append(float(d['sumOfK3CYCnt']) + float(d['SumOfDSCSK3Cnt']))
            if d['sumOfLEPCYCnt'] == None:
                d['sumOfLEPCYCnt'] = 0
            if d['sumOfDSCSLEPCnt'] == None:
                d['sumOfDSCSLEPCnt'] = 0
            GB4_ELL.append(float(d['sumOfLEPCYCnt']) + float(d['sumOfDSCSLEPCnt']))
            if d['sumOfOIResCYCnt'] == None:
                d['sumOfOIResCYCnt'] = 0
            if d['sumOfDSCSOIResCnt'] == None:
                d['sumOfDSCSOIResCnt'] = 0
            GB5_OI_R.append(float(d['sumOfOIResCYCnt']) + float(d['sumOfDSCSOIResCnt']))
            if d['sumOfPSDCYCnt'] == None:
                d['sumOfPSDCYCnt'] = 0
            if d['sumOfDSCSPSDCnt'] == None:
                d['sumOfDSCSPSDCnt'] = 0
            GB6_PS_D.append(float(d['sumOfPSDCYCnt']) + float(d['sumOfDSCSPSDCnt']))
            if d['sumOfMOMRCYCnt'] == None:
                d['sumOfMOMRCYCnt'] = 0
            if d['sumOfDSCSMOMRCnt'] == None:
                d['sumOfDSCSMOMRCnt'] = 0
            GB7_MOID.append(float(d['sumOfMOMRCYCnt']) + float(d['sumOfDSCSMOMRCnt']))
            if d['sumOfHICYCnt'] == None:
                d['sumOfHICYCnt'] = 0
            if d['sumOfDSCSHICnt'] == None:
                d['sumOfDSCSHICnt'] = 0
            GB8_HI.append(float(d['sumOfHICYCnt']) + float(d['sumOfDSCSHICnt']))
            if d['sumOfVICYCnt'] == None:
                d['sumOfVICYCnt'] = 0
            if d['sumOfDSCSVICnt'] == None:
                d['sumOfDSCSVICnt'] = 0
            GB9_VI.append(float(d['sumOfVICYCnt']) + float(d['sumOfDSCSVICnt']))
            if d['sumOfEDPPrivateCYCnt'] == None:
                d['sumOfEDPPrivateCYCnt'] = 0
            if d['sumOfDSCSEDPPrivateCnt'] == None:
                d['sumOfDSCSEDPPrivateCnt'] = 0
            GB10_ED_P.append(float(d['sumOfEDPPrivateCYCnt']) + float(d['sumOfDSCSEDPPrivateCnt']))
            if d['sumOfMDSCCYCnt'] == None:
                d['sumOfMDSCCYCnt'] = 0
            if d['sumOfDSCSMDSCCnt'] == None:
                d['sumOfDSCSMDSCCnt'] = 0
            GB11_MDSC.append(float(d['sumOfMDSCCYCnt']) + float(d['sumOfDSCSMDSCCnt']))
            if d['sumOfMDResCYCnt'] == None:
                d['sumOfMDResCYCnt'] = 0
            if d['sumOfDSCSMDResCnt'] == None:
                d['sumOfDSCSMDResCnt'] = 0
            GB12_MD_R.append(float(d['sumOfMDResCYCnt']) + float(d['sumOfDSCSMDResCnt']))
            if d['sumOfOISCCYCnt'] == None:
                d['sumOfOISCCYCnt'] = 0
            if d['sumOfDSCSOISCCnt'] == None:
                d['sumOfDSCSOISCCnt'] = 0
            GB13_OI_SC.append(float(d['sumOfOISCCYCnt']) + float(d['sumOfDSCSOISCCnt']))
            if d['sumOfMDSSICYCnt'] == None:
                d['sumOfMDSSICYCnt'] = 0
            if d['sumOfDSCSMDSSICnt'] == None:
                d['sumOfDSCSMDSSICnt'] = 0
            GB14_MD_SSI.append(float(d['sumOfMDSSICYCnt']) + float(d['sumOfDSCSMDSSICnt']))
        if d["TEI"] == None:
            d["TEI"] = 0
        # CALCULATION OF TEI
        TEI.append(float(max(TEI10, d["TEI"])))
        # calculation of BASEAMOUNT
        if float(d["MaxOfBaseAmount"]) == TeacherCompAmount:
            TeacherComp.append(1)
        else:
            TeacherComp.append(0)
        if float(d["MaxOfBaseAmount"]) == TeacherCompAnd200DayCalender:
            techercompand200daycalender.append(1)
        else:
            techercompand200daycalender.append(0)
        if float(d["MaxOfBaseAmount"]) == BaseSupport:
            Basecompflag.append(1)
        else:
            Basecompflag.append(0)
        # if TeacherComp[counter1]==1:
        #    LEABaseLevel.append(float(d["MaxOfBaseAmount"])+(float(d["MaxOfBaseAmount"])*TeacherCompPercent))
        # elif techercompand200daycalender[counter1]==1:

        #   LEABaseLevel.append(float(d["MaxOfBaseAmount"]) + (float(d["MaxOfBaseAmount"]) * Percent200DayCalender))
        # else:
        LEABaseLevel.append(float(d["MaxOfBaseAmount"]))
        # calculation of O
        WeightedElemCounts.append(float(ELEMADM[counter1]) * round(float(Final_K_8SmWgt[d['EntityID']]), 3))
        # calculation of P
        WeightedHSCounts.append(float(HSADM[counter1]) * round(float(Final_9_12SmWgt[d['EntityID']]), 3))
        # CALCULATION of WEIGHTED PREKCOUNT
        WeightedPreKCounts.append(float(PREKADM[counter1] * float(GroupAFinalGroupAWeightsPSD)))
        # CALCULATION OF PREKBSL
        if d['FTFStatus'] == '1':
            PrekBSL.append(
                (float(TEI[counter1])) * (float(LEABaseLevel[counter1])) * round(float(WeightedPreKCounts[counter1]),
                                                                                  3) * float(FullTimeAOI))
        elif d['FTFStatus'] == '0':
            PrekBSL.append(
                (float(TEI[counter1])) * (float(LEABaseLevel[counter1])) * round(float(WeightedPreKCounts[counter1]),
                                                                                  3) * float(HalfTimeAOI))
        else:
            PrekBSL.append(
                (float(TEI[counter1])) * (float(LEABaseLevel[counter1])) * round(float(WeightedPreKCounts[counter1]),
                                                                                  3))
        # CALCULATION OF ELEMBSL AND HSBSL
        if (d["FTFStatus"] == '0'):
            ELEMBSL.append(
                (float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]),
                                                                                  3) * float(HalfTimeAOI))
            HSBSL.append(
                (float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]),
                                                                                  3) * float(HalfTimeAOI))
        elif (d["FTFStatus"] == '1'):
            ELEMBSL.append(
                (float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]),
                                                                                  3) * float(FullTimeAOI))
            HSBSL.append(
                (float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]),
                                                                                  3) * float(FullTimeAOI))
        else:
            ELEMBSL.append(
                ((LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]), 3))
            HSBSL.append(
                (float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]), 3))
        # CALCULATION OF VARIABLES FOR Q(GROUP B WEIGHTED ADD ON COUNTS) FROM STUDENT COUNTS FY2016_CLEAN
        Weighted_GB1_EDMIDSLD.append(float(GB1_EDMIDSLD[counter1]) * float(GroupB1))
        Weighted_GB2_K3Reading.append(float(GB2_K3Reading[counter1]) * float(GroupB2))
        Weighted_GB3_K3.append(float(GB3_K3[counter1]) * float(GroupB3))
        Weighted_.append(float(GB4_ELL[counter1]) * float(GroupB4))
        Weighted_GB5_OI_R.append(float(GB5_OI_R[counter1]) * float(GroupB5))
        Weighted_GB6_PS_D.append(float(GB6_PS_D[counter1]) * float(GroupB6))
        Weighted_GB7_MOID.append(float(GB7_MOID[counter1]) * float(GroupB7))
        Weighted_GB8_HI.append(float(GB8_HI[counter1]) * float(GroupB8))
        Weighted_GB9_VI.append(float(GB9_VI[counter1]) * float(GroupB9))
        Weighted_GB10_ED_P.append(float(GB10_ED_P[counter1]) * float(GroupB10))
        Weighted_GB11_MDSC.append(float(GB11_MDSC[counter1]) * float(GroupB11))
        Weighted_GB12_MD_R.append(float(GB12_MD_R[counter1]) * float(GroupB12))
        Weighted_GB13_OI_SC.append(float(GB13_OI_SC[counter1]) * float(GroupB13))
        Weighted_GB14_MD_SSI.append(float(GB14_MD_SSI[counter1]) * float(GroupB14))
        # CALCULATION OF GROUP B WEIGHTED ADD ON COUNTS
        GroupBWeightedAddonCounts.append(
            round(Weighted_GB1_EDMIDSLD[counter1], 3) + round(Weighted_GB2_K3Reading[counter1], 3) + round(
                Weighted_GB3_K3[counter1], 3) + round(Weighted_[counter1], 3) +
            round(Weighted_GB5_OI_R[counter1], 3) + round(Weighted_GB6_PS_D[counter1], 3) + round(
                Weighted_GB7_MOID[counter1], 3) + round(Weighted_GB8_HI[counter1], 3) +
            round(Weighted_GB9_VI[counter1], 3) + round(Weighted_GB10_ED_P[counter1], 3) + round(
                Weighted_GB11_MDSC[counter1], 3) + round(Weighted_GB12_MD_R[counter1], 3) +
            round(Weighted_GB13_OI_SC[counter1], 3) + round(Weighted_GB14_MD_SSI[counter1], 3))
        # CALCULATION OF GROUP B BSL
        if (d["FTFStatus"] == '0'):
            GroupBBSL.append((float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(
                float(GroupBWeightedAddonCounts[counter1]), 3) * (float(HalfTimeAOI)))

        elif (d["FTFStatus"] == '1'):
            GroupBBSL.append((float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(
                float(GroupBWeightedAddonCounts[counter1]), 3) * (float(FullTimeAOI)))
        else:
            GroupBBSL.append((float(LEABaseLevel[counter1])) * (float(TEI[counter1])) * round(
                float(GroupBWeightedAddonCounts[counter1]), 3))
        # CALCULATION OF AuditBaseLevelAdjustment
        if (d["FTFStatus"] == None):
            AuditBaseLevelAdjustment.append(float(d["MaxofBaseAdjsAmount"]))
        else:
            AuditBaseLevelAdjustment.append(float(0))
        # CALCULATION OF LOSS FROM SSW OF K-8 FUNDING AND LOSS FROM SSW OF 9-12 FUNDING
        AB2.append(float(LEABaseLevel[counter1]) * float(Final_K_8SmWgt[d['EntityID']]) * float(ELEMADM[counter1]))
        AH.append(0)
        # AH.append(float(AB2[counter1])-float(AB2[counter1]*float(sixtyseven/100)))
        AC2.append(float(LEABaseLevel[counter1]) * float(Final_9_12SmWgt[d['EntityID']]) * float(HSADM[counter1]))
        AI.append(0)
        # AI.append(float(AC2[counter1]) - float(AC2[counter1] * float(sixtyseven / 100)))
        # CALCULATION OF BSL VALUE
        BSLWithoutAdjustment.append((float(PrekBSL[counter1]) + float(ELEMBSL[counter1]) + round(float(HSBSL[counter1]),
                                                                                                 3) + round(
            float(GroupBBSL[counter1]), 3)))
        BSL.append((float(PrekBSL[counter1]) + float(ELEMBSL[counter1]) + round(float(HSBSL[counter1]), 3) + round(
            float(GroupBBSL[counter1]), 3) + float(AuditBaseLevelAdjustment[counter1])))

        SumofBSL[d['EntityID']] += BSL[counter1]
        sumofadm[d['EntityID']]+= ELEMADM[counter1] + PREKADM[counter1] + HSADM[counter1]

        if d['County'] not in bslbyCounty:
            bslbyCounty[d['County']]=BSL[counter1]
        else:
            bslbyCounty[d['County']]+=BSL[counter1]
        if d['County'] not in admbyCounty:
            admbyCounty[d['County']]=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        else:
            admbyCounty[d['County']]+=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])


        if d['EHType'] not in bslbyEHType:
            bslbyEHType[d['EHType']]=BSL[counter1]
        else:
            bslbyEHType[d['EHType']]+=BSL[counter1]
        if d['EHType'] not in admbyEHType:
            admbyEHType[d['EHType']]=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        else:
            admbyEHType[d['EHType']]+=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        # if schooltype[d['EntityID']] not in bslbyschooltype:
        #     bslbyschooltype[schooltype[d['EntityID']]] = BSL[counter1]
        # else:
        #     bslbyschooltype[schooltype[d['EntityID']]] += BSL[counter1]
        # if schooltype[d['EntityID']] not in admbyschooltype:
        #     admbyschooltype[schooltype[d['EntityID']]] = (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])
        # else:
        #     admbyschooltype[schooltype[d['EntityID']]] += (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])

        if d['Type'] not in bslbytype:
            bslbytype[d['Type']] = float(SumofBSL[d['EntityID']])
        else:
            bslbytype[d['Type']] += float(SumofBSL[d['EntityID']])
        if d['Type'] not in admbytype:
            admbytype[d['Type']] = float(sumofadm[d['EntityID']])
        else:
            admbytype[d['Type']] += float(sumofadm[d['EntityID']])

        # calculate by type and schooltype
        # if schooltypeanddistricttype[d['EntityID']] not in bslbyschooltypeanddistricttype:
        #     bslbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] = BSL[counter1]
        # else:
        #     bslbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] += BSL[counter1]
        # if schooltypeanddistricttype[d['EntityID']] not in admbyschooltypeanddistricttype:
        #     admbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] = (
        #                 PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])
        # else:
        #     admbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] += (
        #                 PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])

        # STORING ENTITY ID
        EID.append(d['EntityID'])
        # STORING ENTITY NAME
        Ename.append(d['EntityName'])
        # CALCULATION OF TOTOAL NET CHARTER AA
        if d['EntityID'] not in sumCharterElemADM.keys():
            LEApercentofCharterElemADM.append(0)
        elif (sumCharterElemADM[d['EntityID']] == 0 or sumCharterElemADM[d['EntityID']] == None):
            LEApercentofCharterElemADM.append(0)
        else:
            LEApercentofCharterElemADM.append(float(sumCharterElemADM[d['EntityID']] / sum(sumCharterElemADM)))
        if d['EntityID'] not in sumCharterHSADM.keys():
            LEApercentofCharterHSADM.append(0)
        elif sumCharterHSADM[d['EntityID']] == 0 or sumCharterHSADM[d['EntityID']] == None:
            LEApercentofCharterHSADM.append(0)
        else:
            LEApercentofCharterHSADM.append(float(sumCharterHSADM[d['EntityID']] / sum(sumCharterHSADM)))

        if (sum(CharterElemAA) + sum(CharterHSAA)) == 0:
            K_8PercentofTotalcharterAA.append(0)
        else:
            K_8PercentofTotalcharterAA.append(float(sum(CharterElemAA) / (sum(CharterElemAA) + sum(CharterHSAA))))
        TotalCharterElemReduction.append(float(CharterReduction) * float(K_8PercentofTotalcharterAA[counter1]))
        TotalCharterHSReduction.append(
            float(CharterReduction) * float((1 - float(K_8PercentofTotalcharterAA[counter1]))))
        CharterElemAAReduction.append(
            float(LEApercentofCharterElemADM[counter1]) * float(TotalCharterElemReduction[counter1]))
        CharterHSAAReduction.append(
            float(LEApercentofCharterHSADM[counter1]) * float(TotalCharterHSReduction[counter1]))
        TotalNetCharterAA.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]) - (
            float(CharterElemAAReduction[counter1] + CharterHSAAReduction[counter1])))
        Reductionsum+=(float(CharterElemAAReduction[counter1] + CharterHSAAReduction[counter1]))
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
            FinalFormulaAAwithReduction.append(float(TotalNetCharterAA[counter1]))
            FinalFormulaAdditionalAssistance.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]))
        else:
            if AdditionalAssistant_eqformula == 2:

                DistrictHSTextbooksAA.append(0)
                DistrictPreKAA.append(float(DistSuppLvlAllPSD * sumprekadm[d['EntityID']]))

                if HSRange[d['EntityID']] == "1to99":
                    DistrictHSAA.append(float(DistSuppLvl1to999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[d['EntityID']] == "100to499" or HSRange[d['EntityID']] == "100to499":
                    DistrictHSAA.append(float(DistSuppLvl100to5999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[d['EntityID']] == ">600":
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                else:
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                if ELEMRange[d['EntityID']] == "1to99":
                    DistrictElemAA.append(float(DistSuppLvl1to99K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[d['EntityID']] == "100to499" or ELEMRange[d['EntityID']] == "500to599":
                    DistrictElemAA.append(float(DistSuppLvl100to599K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[d['EntityID']] == ">600":
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
            TotalDistrictAAReduction.append(float(DistrictPreKElemReduction[counter1] + DistrictHSReduction[counter1]))
            TotalFormulaDistrictAA.append(float(
                DistrictHSTextbooksAA[counter1] + DistrictHSAA[counter1] + DistrictElemAA[counter1] + DistrictPreKAA[
                    counter1]))
            TotalNetDistrictAA.append(float(TotalFormulaDistrictAA[counter1] + TotalDistrictAAReduction[counter1]))
            FinalFormulaAAwithReduction.append(TotalNetDistrictAA[counter1])
            FinalFormulaAdditionalAssistance.append(TotalFormulaDistrictAA[counter1])
            Reductionsum+=(TotalDistrictAAReduction[counter1] * (-1))
        # CALCULATION OF FINALAAALLOCATION

        if AdditonalAssistantReduction == 1:
            if d['Type'] == "Charter":
                CAAdefault += (FinalFormulaAAwithReduction[counter1])
            else:
                DAAdefault += (FinalFormulaAAwithReduction[counter1])
            FinalAAAllocation.append(FinalFormulaAAwithReduction[counter1])
        else:
            if d['Type'] == "Charter":
                CAAdefault += FinalFormulaAdditionalAssistance[counter1]
            else:
                DAAdefault += FinalFormulaAdditionalAssistance[counter1]
            FinalAAAllocation.append(FinalFormulaAdditionalAssistance[counter1])
        AdditionalAssistance.append(FinalAAAllocation[counter1])
        OppurtunityWeight.append(float(0))
        if d['TRCL'] == None:
            d['TRCL'] = 0
        if d['TSL'] == None:
            d['TSL'] = 0
        TRCL.append(float(d['TRCL']))
        TSL.append(float(d['TSL']))
        # CALCULATION OF  WEIGHTED PUPILS USER SPECIFIED SSW REDUCTION
        PreKWeightedPupilsuser_specifiedSWWreduction.append(
            float(float(PREKADM[counter1] * float(GroupAFinalGroupAWeightsPSD)) - 0))
        K_8WeightedPupilsuser_specifiedSWWreduction.append(
            (float(ELEMADM[counter1]) * float(Final_K_8SmWgt[d['EntityID']])) - 0)
        nine_12WeightedPupilsuser_specifiedSWWreduction.append(
            (float(HSADM[counter1]) * float(Final_9_12SmWgt[d['EntityID']])) - 0)
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += \
        PreKWeightedPupilsuser_specifiedSWWreduction[counter1]
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += K_8WeightedPupilsuser_specifiedSWWreduction[
            counter1]
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += \
        nine_12WeightedPupilsuser_specifiedSWWreduction[counter1]
        counter1 += 1
    counter2 = 0
    for i in bslbyCounty:
        if admbyCounty[i]==0:
            perpupilbyCounty[i]=0
        else:
            perpupilbyCounty[i]=(bslbyCounty[i]/admbyCounty[i])
    for i in bslbytype:
        if admbytype[i] == 0:
            perpupilpertype[i] = 0
        else:
            perpupilpertype[i] = (bslbytype[i] / 3) / (admbytype[i] / 3)
    for i in bslbyEHType:
        if admbyEHType[i]==0:
            perpupilbyEHType[i]=0
        else:
            perpupilbyEHType[i]=(bslbyEHType[i]/admbyEHType[i])
    # for i in bslbyschooltype:
    #     if admbyschooltype[i] == 0:
    #         perpupilbyschooltype[i] = 0
    #     else:
    #         perpupilbyschooltype[i] = (bslbyschooltype[i] / admbyschooltype[i])
    # for i in bslbyschooltypeanddistricttype:
    #     if admbyschooltypeanddistricttype[i] == 0:
    #         perpupilbyschooltypeanddistricttype[i] = 0
    #     else:
    #         perpupilbyschooltypeanddistricttype[i] = (
    #                     bslbyschooltypeanddistricttype[i] / admbyschooltypeanddistricttype[i])

    for d4 in range(len(decoded)):
        dictionary = {}
        # Creating a dictionary of the values retrieved from the query
        # d4 = dict(row1.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS

        # CALCULATION OF PERCENTAGE OF PREK_8 OF TOTAL AND HS OF TOTAL
        temp5 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        temp6 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumof9_12WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        temp7 = Sumof9_12WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        if temp6 == 0:
            PercPreK_8ofTotal.append(float(0))
            PercHSofTotal.append(float(0))
        else:
            PercPreK_8ofTotal.append(float(temp5) / float(temp6))
            PercHSofTotal.append(float(temp7) / float(temp6))
        if decoded[d4]['HSTuitionOutAmt1']==None:
            decoded[d4]['HSTuitionOutAmt1']=0
        RCL.append(float(SumofBSL[decoded[d4]['EntityID']]) + OppurtunityWeight[counter2] + TRCL[counter2] + float(decoded[d4]['HSTuitionOutAmt1']))

        DSL.append(float(SumofBSL[decoded[d4]['EntityID']] + OppurtunityWeight[counter2] + TSL[counter2]+ float(decoded[d4]['HSTuitionOutAmt1'])))

        TotalStateEqualisationFunding.append(min(RCL[counter2], DSL[counter2]))

        # CALCULATION OF ELEMENTARY AND HSTOTALSTATE FORMULA
        ElemTotalStateFormula.append(
            float(TotalStateEqualisationFunding[counter2]) * float(PercPreK_8ofTotal[counter2]))
        HSTotalStateFormula.append(float(TotalStateEqualisationFunding[counter2]) * float(PercHSofTotal[counter2]))
        # CALCULATION OF lOCAL LEVY
        if decoded[d4]['TotalHSAssessValAmt'] == None:
            decoded[d4]['TotalHSAssessValAmt'] = 0
        HSAssessedValuation.append(float(decoded[d4]['TotalHSAssessValAmt']))
        if sumhsadm[decoded[d4]['EntityID']] == 0:
            HSQTRYield.append(0)
        elif decoded[d4]['Type'] == "CTED":
            HSQTRYield.append(float(HSAssessedValuation[counter2]) * float(0.01) * float(QTRCTED))
        else:
            HSQTRYield.append(float(HSAssessedValuation[counter2]) * float(0.01) * float(QTR9_12))
        HSLL.append(min(HSTotalStateFormula[counter2], HSQTRYield[counter2]))
        if decoded[d4]['TotalPSElAssessValAmt'] == None:
            decoded[d4]['TotalPSElAssessValAmt'] = 0
        ElemAssessedValuation.append(float(decoded[d4]['TotalPSElAssessValAmt']))
        if sumelemadm[decoded[d4]['EntityID']] == 0:
            ElemQTRYield.append(0)
        else:
            ElemQTRYield.append(float(ElemAssessedValuation[counter2]) * float(QTRK_8) * float(0.01))
        ElemLL.append(min(ElemTotalStateFormula[counter2], ElemQTRYield[counter2]))
        TotalLocalLevy.append(ElemLL[counter2] + HSLL[counter2])
        #sumTotalLocalLevydefault+=(ElemLL[counter2] + HSLL[counter2])
        # CALCUALTION OF TOTAL STATE AID
        if ElemTotalStateFormula[counter2] > ElemQTRYield[counter2]:
            ElemStateAid.append(float(ElemTotalStateFormula[counter2] - ElemQTRYield[counter2]))
        else:
            ElemStateAid.append(0)
        if HSTotalStateFormula[counter2] > HSQTRYield[counter2]:
            HSStateAid.append(float(HSTotalStateFormula[counter2] - HSQTRYield[counter2]))
        else:
            HSStateAid.append(0)
        TotalStateAid.append(ElemStateAid[counter2] + HSStateAid[counter2])
        #sumTotalStateAiddefualt+=ElemStateAid[counter2] + HSStateAid[counter2]
        # CALCULATION OF NO STATE AID
        if ((float(PREKADM[counter2]) + float(sumelemadm[decoded[d4]['EntityID']])) > 0) and (float(ElemStateAid[counter2]) == 0):
            ElemNoStateAidDistrict.append(float(1))
        else:
            ElemNoStateAidDistrict.append(float(0))
        if (sumhsadm[decoded[d4]['EntityID']] > 0) and (HSStateAid[counter2] == 0):
            HSNoStateAidDistrict.append(float(1))
        else:
            HSNoStateAidDistrict.append(float(0))
        if ((float(ElemNoStateAidDistrict[counter2]) + float(HSNoStateAidDistrict[counter2])) > 0) and (
                float(TotalStateAid[counter2]) == 0):
            NoStateAidDistrict.append(float(1))
        else:
            NoStateAidDistrict.append(float(0))
        TotalQTRYield.append(float(ElemQTRYield[counter2] + HSQTRYield[counter2]))
        #sumtotalqtryeild+=(float(ElemQTRYield[counter2] + HSQTRYield[counter2]))
        UncapturedQTR.append(float(TotalQTRYield[counter2] - TotalLocalLevy[counter2]))
        #sumtotaluncapturedqtr+=(float(TotalQTRYield[counter2] - TotalLocalLevy[counter2]))
        TotalStateFundingEqualised.append(float(ElemTotalStateFormula[counter2] + HSTotalStateFormula[counter2]))
        if decoded[d4]['ESSmallIsolated'] == None:
            decoded[d4]['ESSmallIsolated'] = 0
        if decoded[d4]['HSSmallIsolated'] == None:
            decoded[d4]['HSSmallIsolated'] = 0
        sumHSTution+=decoded[d4]["HSTuitionOutAmt1"]
        EqualisationBase.append(TotalStateEqualisationFunding[counter2] + AdditionalAssistance[counter2] + decoded[d4]['HSTuitionOutAmt1'])
        Equalisationassistance.append(EqualisationBase[counter2] - TotalLocalLevy[counter2])
        #df=pandas.DataFrame(entitynull)
        #df.to_csv('C:/Users/jjoth/Desktop/asu/EA/entityfile.csv')
        #dictionary['ElemAssessedValuation']=str(round(ElemAssessedValuation[counter2],4))
        dictionary['ElemQTRYield'] =str(round(ElemQTRYield[counter2], 4))
        dictionary['ElemTotalStateFormula']=str(round(ElemTotalStateFormula[counter2], 4))
        #dictionary['DistrictPreKElemReduction']=str(round(DistrictPreKElemReduction[counter2], 4))
        #dictionary['DistrictHSReduction'] = str(round(DistrictHSReduction[counter2], 4))
        #dictionary['TotalDistrictAAReduction'] = str(round(TotalDistrictAAReduction[counter2], 4))
        #dictionary['NetworkForFundingPurposes']=str(decoded[d4]['NetworkForFundingPurposes'])
        dictionary['EntityID'] = EID[counter2]
        dictionary['prekadm'] = str(round(PREKADM[counter2], 4))
        dictionary['NoStateAidDistrict'] = str(round(NoStateAidDistrict[counter2], 4))
        dictionary['EntityName'] = Ename[counter2]
        # dictionary['schooltype']=str(schooltype[decoded[d4]['EntityID']])
        dictionary['County'] = decoded[d4]['County']
        #dictionary['AOI'] = str(decoded[d4]['FTFStatus'])
        #dictionary['TEI'] = str(round(TEI[counter2], 5))
        dictionary['Type']=str(decoded[d4]['Type'])
        # dictionary['bslbyschooltype'] = str(round(bslbyschooltype[schooltype[decoded[d4]['EntityID']]],2))
        # dictionary['admbyschooltype'] = str(round(admbyschooltype[schooltype[decoded[d4]['EntityID']]],2))
        dictionary['bslbyEHType']=str(round(bslbyEHType[schoolEHType[decoded[d4]['EntityID']]],2))
        dictionary['admbyEHType']=str(round(admbyEHType[schoolEHType[decoded[d4]['EntityID']]],2))
        dictionary['perpupilbyEHType']=str(round(perpupilbyEHType[schoolEHType[decoded[d4]['EntityID']]],2))
        dictionary['bslbytype']=str(round((bslbytype[decoded[d4]['Type']]/3),2))
        dictionary['admbytype']=str(round((admbytype[decoded[d4]['Type']]/3),2))
        # dictionary['perpupilbyschooltype']=str(round((perpupilbyschooltype[schooltype[decoded[d4]['EntityID']]]),2))
        dictionary['perpupilpertype'] = str(round((perpupilpertype[decoded[d4]['Type']]), 2))
        # dictionary['perpupilbyschooltypeanddistricttype'] = str(round((perpupilbyschooltypeanddistricttype[schooltypeanddistricttype[decoded[d4]['EntityID']]]), 2))
        #dictionary['DistrictHSAA'] = str(round(DistrictHSAA[counter2], 5))
        #dictionary['DistrictElemAA'] = str(round(DistrictElemAA[counter2], 5))
        #dictionary['DistrictPreKAA'] = str(round(DistrictPreKAA[counter2], 5))
        dictionary['hsadm'] = str(round(HSADM[counter2], 4))
        dictionary['elemadm'] = str(round(ELEMADM[counter2], 4))
        #dictionary['prekbsl'] = str(round(PrekBSL[counter2], 4))
        #dictionary['elembsl'] = str(round(ELEMBSL[counter2], 4))
        #dictionary['hsbsl'] = str(round(HSBSL[counter2], 4))
        dictionary['BSL'] = str(round(BSL[counter2], 2))
        if sumofadm[decoded[d4]['EntityID']] ==0:
            dictionary['sumofBSLcalcperpupil'] = str(0)
        else:
            dictionary['sumofBSLcalcperpupil']=str(round(round(SumofBSL[decoded[d4]['EntityID']], 2)/(sumofadm[decoded[d4]['EntityID']]),2))
        dictionary['SumofBSL']=str(round(SumofBSL[decoded[d4]['EntityID']], 4))
        dictionary['TotalBSL'] = str(round(sum(SumofBSL.values()), 2))
        #dictionary['WeightedPreKCounts'] = str(round(WeightedPreKCounts[counter2], 3))
        #dictionary['WeightedElemCounts'] = str(round(WeightedElemCounts[counter2], 3))
        #dictionary['WeightedHSCounts'] = str(round(WeightedHSCounts[counter2], 3))
        dictionary['TotalLocalLevy'] = str(round(TotalLocalLevy[counter2], 3))
        dictionary['UncapturedQTR'] = str(round(UncapturedQTR[counter2], 3))
        dictionary['TotalStateAid'] = str(round(TotalStateAid[counter2], 3))
        #dictionary['Final_K_8SmWgt'] = str(round(Final_K_8SmWgt[decoded[d4]['EntityID']], 3))
        #dictionary['Final_9_12SmWgt'] = str(round(Final_9_12SmWgt[decoded[d4]['EntityID']], 3))
        dictionary['bslbyCounty'] = str(round(bslbyCounty[decoded[d4]['County']], 2))
        dictionary['admbyCounty'] = str(round(admbyCounty[decoded[d4]['County']], 2))
        dictionary['perpupilbyCounty'] = str(round(perpupilbyCounty[decoded[d4]['County']], 2))
        dictionary['RCL'] = str(round(RCL[counter2], 4))
        dictionary['TRCL'] = str(round(TRCL[counter2], 4))
        dictionary['DSL'] = str(round(DSL[counter2], 4))
        dictionary['TSL'] = str(round(TSL[counter2], 4))
        #dictionary['LEABaseLevel'] = str(round(LEABaseLevel[counter2], 4))
        #dictionary['BSLWithoutAdjustment']=str(round(BSLWithoutAdjustment[counter2],4))
        #dictionary['PreKWeightedPupilsuser_specifiedSWWreduction'] = str(round(PreKWeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        #dictionary['K_8WeightedPupilsuser_specifiedSWWreduction'] = str(round(K_8WeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        #dictionary['nine_12WeightedPupilsuser_specifiedSWWreduction'] = str(round(nine_12WeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        dictionary['TotalStateFundingEqualised'] = str(round(TotalStateFundingEqualised[counter2], 4))
        #dictionary['NetworkElemADM'] = str(round(NetworkElemADM[counter2], 4))
        #dictionary['NetworkHSADM'] = str(round(NetworkHSADM[counter2], 4))
        #dictionary['PREKADM'] = str(round(PREKADM[counter2], 4))
        #dictionary['ELEMADM'] = str(round(ELEMADM[counter2], 4))
        #dictionary['HSADM'] = str(round(HSADM[counter2], 4))
        #dictionary['GroupBWeightedAddonCounts'] = str(round(GroupBWeightedAddonCounts[counter2], 3))
        #dictionary['SSWELEMINCREMENTALWEIGHTPP'] = str(round(SSWELEMINCREMENTALWEIGHTPP[counter2], 3))
        #dictionary['ElemBaseWeight'] = str(round(ElemBaseWeight[counter2], 3))
        #dictionary['GroupBBSL'] = str(round(GroupBBSL[counter2], 2))
        #dictionary['HSBSL'] = str(round(HSBSL[counter2], 2))
        #dictionary['AuditBaseLevelAdjustment'] = str(round(AuditBaseLevelAdjustment[counter2], 3))
        #dictionary['ELEMRange'] = (ELEMRange[decoded[d4]['EntityID']])
        #dictionary['HSRange'] = (HSRange[decoded[d4]['EntityID']])
        #dictionary['HSSmallIsolated'] = str(round(decoded[d4]['HSSmallIsolated'], 3))

        dictionary['AdditionalAssistance']=AdditionalAssistance[counter2]
        #dictionary['ElemBSL'] = str(round(ELEMBSL[counter2], 3))
        # print(type(d4['ESSmallIsolated']))
        #dictionary['ESSmallIsolated'] = str(round(decoded[d4]['ESSmallIsolated'], 3))
        #dictionary['TotalFormulaDistrictAA'] = str(round(TotalFormulaDistrictAA[counter2], 4))
        #dictionary['TotalNetDistrictAA'] = str(round(TotalNetDistrictAA[counter2], 4))
        #dictionary['FinalFormulaAAwithReduction'] = str(round(FinalFormulaAAwithReduction[counter2], 4))
        #dictionary['FinalFormulaAdditionalAssistance'] = str(round(FinalFormulaAdditionalAssistance[counter2], 4))
        #dictionary['ElemLL'] = str(round(ElemLL[counter2], 4))
        #dictionary['HSBaseWeight'] = str(round(HSBaseWeight[decoded[d4]['EntityID']], 4))
        #dictionary['HSLL'] = str(round(HSLL[counter2], 4))
        #dictionary['SSWHSINCREMENTALWEIGHTPP'] = str(round(SSWHSINCREMENTALWEIGHTPP[counter2], 4))
        D.append(dictionary)
        counter2 += 1
        ti=time.time()
    sumbsl=sum(SumofBSL)
    sumtrcl=sum(TRCL)/3
    sumtsl=sum(TSL)/3
    sumrcl=sum(RCL)/3
    sumdsl=sum(DSL)/3
    sumtotaladditionalassistancedefault=sum(AdditionalAssistance)/3
    sumTotalLocalLevydefault=sum(TotalLocalLevy)/3
    sumTotalStateAiddefualt=sum(TotalStateAid)/3
    sumtotalqtryeild=sum(TotalQTRYield)/3
    sumtotaluncapturedqtr=sum(UncapturedQTR)/3
    sumEqualisationAssistance=sum(Equalisationassistance)/3
    sumEqualisationbase=sum(EqualisationBase)/3

    Reductionsum/=3
    sumHSTution/=3
    #dict1 =pd.DataFrame([[sumbsl,sumtrcl,sumtsl,sumrcl,sumdsl,sumtotaladditionalassistancedefault,sumTotalLocalLevydefault,sumTotalStateAiddefualt,sumtotalqtryeild,sumtotaluncapturedqtr,sumEqualisationAssistance,sumEqualisationbase,Reductionsum,sumHSTution]],columns=["sumbsl","sumtrcl","sumtsl","sumrcl","sumdsl","sumtotaladditionalassistancedefault","sumTotalLocalLevydefault","sumTotalStateAiddefualt","sumtotalqtryeild","sumtotaluncapturedqtr","sumEqualisationAssistance","sumEqualisationbase","Reductionsum","sumHSTution"])
    #dict1.to_csv(str("whole values"+str(yearnum)+"_"+str(Yeardef)+".csv"),header=True)
    return D


@app.route('/wftf2', methods=['GET', 'POST'])
def wftf2():
    # start of input variables to be posted  in front end
    yearnum = int((flask.request.form['yearnum']))
    BaseSupport = float(flask.request.form['BaseSupport'])
    Yeardef = (flask.request.form['Yeardef'])
    flask.session['Yeardef'] = Yeardef
    def alchemyencoder(obj):
        """JSON encoder function for SQLAlchemy special classes."""
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    def example():
        preresult = engine.execute('Select flight.*,fm.TuitionOutCnt,fm.HSTuitionOutAmt1 from (select truck.*,lorry.PsdCapOutlayRevLimitAmt,lorry.ElemCapOutlayRevLimitAmt,lorry.HsPrlmCapOutlayRevLimitAmt,lorry.HsBooksCapOutlayRevLimitAmt,lorry.PSElTransAdj,lorry.HSTransAdj from (select kvs.*, CSH.parentOrganization, CSH.NetworkForFundingPurposes, CSH.ESSmallIsolated, CSH.HSSmallIsolated from (select ftfmaintype.*,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (Select ftfmain.*,EntityName,Entityshort.County,Entityshort.Type,Entityshort.EHType from (select EntityID, sum(PsdCount) as sumOfPsdCount,sum(PsdCYCount) as sumOfPsdCYCount,sum(ElemCount) as sumOfElemCount,sum(ElemCYCount) as sumOfElemCYCount,sum(DSCSElemCnt) as sumOfDSCSElemCount,sum(HsCount) as sumOfHsCount,sum(HsCYCount) as sumOfHsCYCount, sum(DSCSHsCnt) as sumOfDSCSHsCount, FiscalYear,TEI,BaseAmount as MaxOfBaseAmount,BaseAdjsAmount as MaxofBaseAdjsAmount, sum(MDSSICnt) as sumOfMDSSICnt,sum(MDSSICYCnt) as sumOfMDSSICYCnt, sum(DSCSMDSSICnt)as sumOfDSCSMDSSICnt, sum(DSCSVICnt)as sumOfDSCSVICnt, sum(DSCSOISCCnt) as sumOfDSCSOISCCnt, sum(DSCSPSDCnt)as sumOfDSCSPSDCnt, sum(DSCSMDSCCnt)as sumOfDSCSMDSCCnt, sum(DSCSHICnt)as sumOfDSCSHICnt, sum(DSCSMOMRCnt)as sumOfDSCSMOMRCnt, sum(DSCSEDPPrivateCnt)as sumOfDSCSEDPPrivateCnt, sum(DSCSMDResCnt)as sumOfDSCSMDResCnt, sum(DSCSOIResCnt)as sumOfDSCSOIResCnt, sum(DSCSEDMIMRCnt)as sumOfDSCSEDMIMRCnt, sum(DSCSLEPCnt)as sumOfDSCSLEPCnt, sum(DSCSK3Cnt)as SumOfDSCSK3Cnt,sum(PSDCnt)as sumOfPSDCnt, sum(PSDCYCnt)as sumOfPSDCYCnt,sum(VICnt)as sumOfVICnt, sum(VICYCnt)as sumOfVICYCnt, sum(OISCCnt)as sumOfOISCCnt, sum(OISCCYCnt)as sumOfOISCCYCnt, sum(MDSCCnt)as sumOfMDSCCnt, sum(MDSCCYCnt)as sumOfMDSCCYCnt,sum(HICYCnt)as sumOfHICYCnt,sum(HICnt)as sumOfHICnt,sum(MOMRCnt)as sumOfMOMRCnt, sum(MOMRCYCnt)as sumOfMOMRCYCnt, sum(EDPPrivateCYCnt)as sumOfEDPPrivateCYCnt,sum(EDPPrivateCnt)as sumOfEDPPrivateCnt,sum(MDResCnt)as sumOfMDResCnt, sum(MDResCYCnt)as sumOfMDResCYCnt,sum(OIResCnt)as sumOfOIResCnt, sum(OIResCYCnt)as sumOfOIResCYCnt,sum(EDMIMRCYCnt)as sumOfEDMIMRCYCnt, sum(EDMIMRCnt)as sumOfEDMIMRCnt,sum(LEPCnt)as sumOfLEPCnt, sum(LEPCYCnt)as sumOfLEPCYCnt, sum(K3Cnt)as sumOfK3Cnt,sum(K3CYCnt)as sumOfK3CYCnt, FTFStatus from ((select t.EntityID,t.FiscalYear,t.PsdCYCount,t.PsdCount,t.ElemCYCount,t.ElemCount,t.DSCSElemCnt,t.HsCYCount,t.HsCount,t.DSCSHsCnt,t.DSCSK3Cnt,t.TEI,t.PaymentMonth,t.FTFStatus,t.BaseAmount,t.BaseAdjsAmount,t.MDSSICnt,t.MDSSICYCnt,t.DSCSMDSSICnt, t.DSCSVICnt,t.DSCSOISCCnt,t.DSCSPSDCnt,t.DSCSMDSCCnt,t.DSCSHICnt,t.DSCSMOMRCnt,t.DSCSEDPPrivateCnt,t.DSCSMDResCnt,t.DSCSOIResCnt,t.DSCSEDMIMRCnt,t.DSCSLEPCnt,t.PSDCYCnt,t.PSDCnt,t.VICYCnt,t.VICnt,t.OISCCYCnt,t.OISCCnt,t.MDSCCYCnt, t.MDSCCnt,t.HICYCnt,t.HICnt,t.MOMRCYCnt,t.MOMRCnt,t.EDPPrivateCYCnt,t.EDPPrivateCnt,t.MDResCYCnt,t.MDResCnt,t.OIResCYCnt,t.OIResCnt,t.EDMIMRCYCnt,t.EDMIMRCnt,t.LEPCYCnt,t.LEPCnt,t.K3CYCnt,t.K3Cnt from SaAporBaseSupportLevelCalcs2 t use index(aporbasei,aporbase2,aporbasei3,aporbasei4,aporbasei5) inner join (select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaAporBaseSupportLevelCalcs2 use index(aporbasei,aporbase2,aporbasei3,aporbasei4,aporbasei5) group by EntityID,FiscalYear having FiscalYear=(%s)) tm on t.EntityID=tm.EntityID and t.PaymentMonth=tm.MaxPaymentMonth and tm.FiscalYear=t.FiscalYear   ) union all select yy.EntityID,yy.FiscalYear,yy.PsdCYCount,yy.PsdCount,yy.ElemCYCount, yy.ElemCount, yy.DSCSElemCnt,yy.HsCYCount,yy.HsCount,yy.DSCSHsCnt,yy.DSCSK3Cnt,yy.TEI,yy.PaymentMonth,yy.FTFStatus,yy.BaseAmount,yy.BaseAdjsAmount, yy.MDSSICnt, yy.MDSSICYCnt,yy.DSCSMDSSICnt, yy.DSCSVICnt,yy.DSCSOISCCnt,yy.DSCSPSDCnt,yy.DSCSMDSCCnt,yy.DSCSHICnt,yy.DSCSMOMRCnt,yy.DSCSEDPPrivateCnt,yy.DSCSMDResCnt,yy.DSCSOIResCnt,yy.DSCSEDMIMRCnt,yy.DSCSLEPCnt,yy.PSDCYCnt,yy.PSDCnt, yy.VICYCnt,yy.VICnt,yy.OISCCYCnt,yy.OISCCnt,yy.MDSCCYCnt, yy.MDSCCnt,yy.HICYCnt,yy.HICnt,yy.MOMRCYCnt,yy.MOMRCnt,yy.EDPPrivateCYCnt, yy.EDPPrivateCnt,yy.MDResCYCnt,yy.MDResCnt,yy.OIResCYCnt,yy.OIResCnt, yy.EDMIMRCYCnt,yy.EDMIMRCnt,yy.LEPCYCnt,yy.LEPCnt,yy.K3CYCnt,yy.K3Cnt from SaCharBaseSupportLevelCalcs2 yy use index(cbasei,cbasei2,cbasei3,cbasei4) inner join (select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaCharBaseSupportLevelCalcs2 use index(cbasei,cbasei2,cbasei3,cbasei4) group by EntityID,FiscalYear having FiscalYear=(%s))ym on yy.EntityId=ym.EntityID and yy.PaymentMonth=ym.MaxPaymentMonth and ym.FiscalYear=yy.FiscalYear  )uni where FiscalYear=(%s) group by EntityID,FTFStatus )ftfmain left join (select EntityID,EntityName,County,Type,Type as EHType from Entity use index(Enti))Entityshort on ftfmain.EntityID=Entityshort.EntityID )ftfmaintype left join (select TRCLTSL.EntityID,TRCL,TSL,TotalPSElAssessValAmt,TotalHSAssessValAmt from (select TRCL.EntityID,TRCL,TSL from ((select j.EntityID,j.TRCL from SaAporTransRevCtlLimit2 j  Use index(TRCLi) inner join ( select EntityID,FiscalYear,max(PaymentMonth)as MaxPaymentMonth from SaAporTransRevCtlLimit2 Use index(TRCLi) group by EntityID,FiscalYear having FiscalYear=(%s)) jm on j.EntityID=jm.EntityID and j.PaymentMonth=jm.MaxPaymentMonth and jm.FiscalYear=j.FiscalYear   ))TRCL left join ((select k.EntityID,k.TSL from SaAporTransSupptLvl2 k use index(TSLi)  inner join (Select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaAporTransSupptLvl2 use index(TSLi) group by EntityID,FiscalYear having FiscalYear=(%s))km where k.EntityID=km.EntityID and k.PaymentMonth=km.MaxPaymentMonth and km.FiscalYear=k.FiscalYear   ))TSL on TRCL.EntityID=TSL.EntityID)TRCLTSL left join ((Select l.EntityID,l.TotalPSElAssessValAmt,l.TotalHSAssessValAmt from SaAporQualLevy2 l use index(quallevyi1) inner join (Select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaAporQualLevy2 use index(quallevyi1) group by EntityID,FiscalYear having FiscalYear=(%s))lm where l.EntityID=lm.EntityID and l.PaymentMonth=lm.MaxPaymentMonth and lm.FiscalYear=l.FiscalYear  ))PSEl on TRCLTSL.EntityID=PSEl.EntityID )Bike on ftfmaintype.EntityID=Bike.EntityID) kvs left join (select s1.EntityID, s1.Name as EntityName, CWN.parentOrganization, CWN.NetworkForFundingPurposes, s1.ESSmallIsolated, s1.HSSmallIsolated from (select EntityID, ChartersWithNetwork.OrganizationName as EntityName, ParentOrganization, ifnull(Charters4Funding.NetworkForFundingPurposes,0) as NetworkForFundingPurposes  from ChartersWithNetwork use index(chneti) left join Charters4Funding use index(charfundi) on ChartersWithNetwork.ParentOrganization = Charters4Funding.OrganizationName) CWN right join SmallIsolatedList s1 use index(smallisoi) on CWN.EntityID = s1.EntityID)CSH on kvs.EntityID = CSH.EntityID)truck left join(select car1.EntityID,PsdCapOutlayRevLimitAmt,ElemCapOutlayRevLimitAmt,HsPrlmCapOutlayRevLimitAmt,HsBooksCapOutlayRevLimitAmt,PSElTransAdj,HSTransAdj from ((select g.EntityID,g.PsdCapOutlayRevLimitAmt,g.ElemCapOutlayRevLimitAmt,g.HsPrlmCapOutlayRevLimitAmt,g.HsBooksCapOutlayRevLimitAmt from SaAporCapitalOutlayCalcs2 g use index(acapoutlaycalci) inner join (Select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaAporCapitalOutlayCalcs2 use index(acapoutlaycalci) group by EntityID,FiscalYear having FiscalYear=(%s) ) gm where g.EntityID=gm.EntityID and g.PaymentMonth=gm.MaxPaymentMonth and gm.FiscalYear=g.FiscalYear   ) )bike1 left join ((select d.EntityID,d.PSElTransAdj,d.HSTransAdj from SaAporSoftCapAlloc2 d use index(aporsoftcapi) inner join (Select EntityID,FiscalYear,max(PaymentMonth) as MaxPaymentMonth from SaAporSoftCapAlloc2 use index(aporsoftcapi) group by EntityID,FiscalYear having FiscalYear=(%s))dm where d.EntityID=dm.EntityID and d.PaymentMonth=dm.MaxPaymentMonth and dm.FiscalYear=d.FiscalYear   ) )car1 on car1.EntityID=bike1.EntityID)lorry on lorry.EntityID=truck.EntityID)flight left join(SELECT EntityID,FiscalYear,TuitionOutCnt,HSTuitionOutAmt1 FROM Tutionoutcount use index(Tui) where FiscalYear=(%s))fm on fm.EntityID=flight.EntityID',(yearnum,yearnum,yearnum,yearnum,yearnum,yearnum,yearnum,yearnum,yearnum))

        # use special handler for dates and decimals
        return json.dumps([dict(r) for r in preresult], default=alchemyencoder)

    def example1():
        basesup = engine.execute('SELECT min(BaseAmount) as minbase FROM DCSchoolFinance.SaAporBaseSupportLevelCalcs2 where FiscalYear=(%s)',(yearnum))
        return json.dumps([dict(r) for r in basesup], default=alchemyencoder)

    Bs = (example1())
    de = json.loads(Bs)
    actualBaseSupport=float(de[0]['minbase'])
    actualTeachercomp= round(actualBaseSupport * (1 + (1.25/100)),2)

    actualTeacherCompAnd200DayCalender =round((actualBaseSupport * (1 + (1.25/100)))+(actualBaseSupport * (1 + (1.25/100)))*(5/100),2)

    actual200daycalender=round(actualBaseSupport + (actualBaseSupport * (5)/100),2)

    diffBaseSupport=actualBaseSupport-BaseSupport
    counter1 = 0
    g = example()
    Original = wftf(yearnum,g, Yeardef)
    decoded = json.loads(g)
    TeacherCompPercent = float(flask.request.form['TeacherCompPercent'])
    Percent200DayCalender = float(flask.request.form['Percent200DayCalender'])
    WtSmallIso1to99K_8 = float(flask.request.form['WtSmallIso1to99K_8'])
    WtSmallIso100to499K_8 = float(flask.request.form['WtSmallIso100to499K_8'])
    WtSmallIso500to599K_8 = float(flask.request.form['WtSmallIso500to599K_8'])
    WtSmallIso600AndOverK_8 = float(flask.request.form['WtSmallIso600AndOverK_8'])
    WtSmall1to99K_8 = float(flask.request.form['WtSmall1to99K_8'])
    WtSmall100to499K_8 = float(flask.request.form['WtSmall100to499K_8'])
    WtSmall500to599K_8 = float(flask.request.form['WtSmall500to599K_8'])
    WtSmall600AndOverK_8 = float(flask.request.form['WtSmall600AndOverK_8'])
    WtSmallIso1to999_12 = float(flask.request.form['WtSmallIso1to999_12'])
    WtSmallIso100to4999_12 = float(flask.request.form['WtSmallIso100to4999_12'])
    WtSmallIso500to5999_12 = float(flask.request.form['WtSmallIso500to5999_12'])
    WtSmallIso600AndOver9_12 = float(flask.request.form['WtSmallIso600AndOver9_12'])
    WtSmall1to999_12 = float(flask.request.form['WtSmall1to999_12'])
    WtSmall100to4999_12 = float(flask.request.form['WtSmall100to4999_12'])
    WtSmall500to5999_12 = float(flask.request.form['WtSmall500to5999_12'])
    WtSmall600AndOver9_12 = float(flask.request.form['WtSmall600AndOver9_12'])
    IncWtSmallIso1to99K_8 = float(flask.request.form['IncWtSmallIso1to99K_8'])
    IncWtSmallIso100to499K_8 = float(flask.request.form['IncWtSmallIso100to499K_8'])
    IncWtSmallIso500to599K_8 = float(flask.request.form['IncWtSmallIso500to599K_8'])
    IncWtSmallIso600AndOverK_8 = float(flask.request.form['IncWtSmallIso600AndOverK_8'])
    IncWtSmall1to99K_8 = float(flask.request.form['IncWtSmall1to99K_8'])
    IncWtSmall100to499K_8 = float(flask.request.form['IncWtSmall100to499K_8'])
    IncWtSmall500to599K_8 = float(flask.request.form['IncWtSmall500to599K_8'])
    IncWtSmall600AndOverK_8 = float(flask.request.form['IncWtSmall600AndOverK_8'])
    IncWtSmallIso1to999_12 = float(flask.request.form['IncWtSmallIso1to999_12'])
    IncWtSmallIso100to4999_12 = float(flask.request.form['IncWtSmallIso100to4999_12'])
    IncWtSmallIso500to5999_12 = float(flask.request.form['IncWtSmallIso500to5999_12'])
    IncWtSmallIso600AndOver9_12 = float(flask.request.form['IncWtSmallIso600AndOver9_12'])
    IncWtSmall1to999_12 = float(flask.request.form['IncWtSmall1to999_12'])
    IncWtSmall100to4999_12 = float(flask.request.form['IncWtSmall100to4999_12'])
    IncWtSmall500to5999_12 = float(flask.request.form['IncWtSmall500to5999_12'])
    IncWtSmall600AndOver9_12 = float(flask.request.form['IncWtSmall600AndOver9_12'])
    FullTimeAOI = float(flask.request.form['FullTimeAOI'])
    HalfTimeAOI = float(flask.request.form['HalfTimeAOI'])
    QTRK_8 = float(flask.request.form['QTRK_8'])
    QTR9_12 = float(flask.request.form['QTR9_12'])
    QTRCTED = float(flask.request.form['QTRCTED'])
    CharterReduction = float(flask.request.form['CharterReduction'])
    CharSuppLvlAllK_8 = float(flask.request.form['CharSuppLvlAllK_8'])
    CharSuppLvlAll9_12 = float(flask.request.form['CharSuppLvlAll9_12'])
    GroupAFinalGroupAWeightsPSD = float(flask.request.form['GroupAFinalGroupAWeightsPSD'])
    GroupAFinalGroupAWeightsK_8 = float(flask.request.form['GroupAFinalGroupAWeightsK_8'])
    GroupAFinalGroupAWeights9_12 = float(flask.request.form['GroupAFinalGroupAWeights9_12'])
    GroupAFinalGroupAWeightsCTED = float(flask.request.form['GroupAFinalGroupAWeightsCTED'])
    DistSuppLvlAllPSD = float(flask.request.form['DistSuppLvlAllPSD'])
    DistSuppLvl1to99K_8 = float(flask.request.form['DistSuppLvl1to99K_8'])
    DistSuppLvl100to599K_8 = float(flask.request.form['DistSuppLvl100to599K_8'])
    DistSuppLvl600AndOverK_8 = float(flask.request.form['DistSuppLvl600AndOverK_8'])
    DistSuppLvl1to999_12 = float(flask.request.form['DistSuppLvl1to999_12'])
    DistSuppLvl100to5999_12 = float(flask.request.form['DistSuppLvl100to5999_12'])
    DistSuppLvl600AndOver9_12 = float(flask.request.form['GroupB1'])
    GroupB1 = float(flask.request.form['GroupB1'])
    GroupB2 = float(flask.request.form['GroupB2'])
    GroupB3 = float(flask.request.form['GroupB3'])
    GroupB4 = float(flask.request.form['GroupB4'])
    GroupB5 = float(flask.request.form['GroupB5'])
    GroupB6 = float(flask.request.form['GroupB6'])
    GroupB7 = float(flask.request.form['GroupB7'])
    GroupB8 = float(flask.request.form['GroupB8'])
    GroupB9 = float(flask.request.form['GroupB9'])
    GroupB10 = float(flask.request.form['GroupB10'])
    GroupB11 = float(flask.request.form['GroupB11'])
    GroupB12 = float(flask.request.form['GroupB12'])
    GroupB13 = float(flask.request.form['GroupB13'])
    GroupB14 = float(flask.request.form['GroupB14'])
    TEI10 = float(flask.request.form['TEI10'])
    AdditionalAssistant_eqformula = float(flask.request.form['AdditionalAssistant_eqformula'])
    AdditonalAssistantReduction = float(flask.request.form['AdditonalAssistantReduction'])
    # End of input variables to be posted  in front end
    QTRUnified = QTRK_8 + QTR9_12
    TeacherCompAmount = BaseSupport + (BaseSupport * TeacherCompPercent)
    Amount200DayCalender = BaseSupport + (BaseSupport * Percent200DayCalender)
    TeacherCompAnd200DayCalender = (BaseSupport + (BaseSupport * TeacherCompPercent)) * (1 + Percent200DayCalender)
    gi=time.time()

    # ASSIGNING VARIABLES FOR CALCULATION

    # DEFINING VARIABLES FOR FURTHER CALCULATION
    EqualisationAssistance=[]
    sumprekadm={}
    sumelemadm={}
    sumhsadm={}
    Final_9_12SmWgt={}
    Final_K_8SmWgt={}
    AuditBaseLevelAdjustment=[]
    FinalFormulaAdditionalAssistance=[]
    FinalAAAllocation=[]
    EID=[]
    Ename=[]
    D=[]
    BSL=[]
    TEI=[]
    LEABaseLevel1=[]
    WeightedElemCounts=[]
    WeightedHSCounts=[]
    GroupBWeightedAddonCounts=[]
    ElemBaseWeight=[]
    HSBaseWeight={}
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
    bslbytype={}
    admbytype={}
    FinalFormulaAAwithReduction = []
    AdditionalAssistance = []
    sumTotalLocalLevy=0
    sumtotalstateaid=0
    sumAdditionalAssistance=0
    CAA=0
    DAA=0
    HSRange = {}
    ELEMRange = {}
    TotalStateEqualisationFunding = []
    OppurtunityWeight = []
    TRCL = []
    TSL = []
    RCL = []
    DSL = []
    TeacherComp = []
    Basecompflag=[]
    twohundereddaycalendar = []
    techercompand200daycalender = []
    SumofPreKWeightedPupilsuser_specifiedSWWreduction = {}
    Sumofk_8WeightedPupilsuser_specifiedSWWreduction = {}
    Sumof9_12WeightedPupilsuser_specifiedSWWreduction = {}
    sumCharterElemADM={}
    sumCharterHSADM={}
    BSLWithoutAdjustment=[]
    SumofBSL={}
    sumofadm={}
    perpupilpertype={}
    # STORE THE NETWORK NAMES
    parentorg = engine.execute('select distinct (ParentOrganization) from ChartersWithNetwork')
    for row2 in parentorg:
        d2 = row2[0]
        if d2 != '':
            sumofnetworkelemadm[d2]=0
            sumofnetworkhsadm[d2]=0
    count = 0
    # schooltype = {}
    schoolEHType={}
    # schooltypeanddistricttype={}
    # admbyschooltype={}
    # bslbyschooltype={}
    bslbyEHType={}
    admbyEHType={}
    bslbyCounty={}
    admbyCounty={}
    perpupilbyCounty={}

    # admbyschooltypeanddistricttype={}
    # bslbyschooltypeanddistricttype={}
    # perpupilbyschooltypeanddistricttype={}
    # perpupilbyschooltype={}
    perpupilbyEHType={}
    # CALCULATION OF ADM VALUES
    for pred in decoded:
        #pred = dict(prerow.items())
        entityid = pred['EntityID']
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[entityid] = 0
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS
        if (pred['EHType']=='Charter Holder - University' or pred['EHType']=='Charter Holder-Charter Board'):
            pred['EHType']="Charter"
        elif(pred['EHType']=='School District - Vocational/Technical'):
            pred['EHType']="CTED"
        elif(pred['EHType']==None):
            pred['EHType'] = "None"
        elif(pred['EHType']=='School District - Accommodation'):
            pred['EHType']="Accomodation"
        elif(pred['EHType']=='School District - Elementary In High School'):
            pred['EHType']="Elementary with HS Students"
        elif(pred['EHType']=="School District - Elementary Not In High School"):
            pred['EHType']="Elementary district"
        elif(pred['EHType']=="School District - Unified"):
            pred['EHType']="Unified district"
        schoolEHType[pred['EntityID']] = pred['EHType']
        if (pred['Type'] == 'Charter Holder-Charter Board'):

            pred['Type'] = "Charter"
        elif (pred['Type'] == 'Charter Holder - University'):
            pred['Type'] = "Charter"

        elif (pred['Type'] == 'School District - Vocational/Technical'):
            pred['Type'] = "CTED"
        else:
            pred['Type'] = "District"
        # calculation of PREKADM
        if Yeardef=="CY" and (pred['Type']!="Charter" and pred['Type']!="CTED"):
            if pred['sumOfPsdCYCount'] == None:
                pred['sumOfPsdCYCount'] = 0
            PREKADM.append(float(pred['sumOfPsdCYCount']))
            if pred['sumOfElemCYCount'] == None:
                pred['sumOfElemCYCount'] = 0
            if pred['sumOfDSCSElemCount'] == None:
                pred['sumOfDSCSElemCount'] = 0
            ELEMADM.append(float(pred['sumOfElemCYCount']) + float(pred['sumOfDSCSElemCount']))
            # CALCULATION OF HSADM VALUE
            if pred['sumOfHsCYCount'] == None:
                pred['sumOfHsCYCount'] = 0
            if pred['sumOfDSCSHsCount'] == None:
                pred['sumOfDSCSHsCount'] = 0
            HSADM.append(float(pred['sumOfHsCYCount']) + float(pred['sumOfDSCSHsCount']))
        else:
            if pred['sumOfPsdCount'] == None:
                pred['sumOfPsdCount'] = 0
            PREKADM.append(float(pred['sumOfPsdCount']))
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
        # CALCULATION OF ELEM ADM
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
        sumofadm[pred['EntityID']]=0
        # if (PREKADM[count]==0 and ELEMADM[count]==0 and HSADM[count]==0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="novalue"
        # elif (PREKADM[count]==0 and ELEMADM[count]==0 and HSADM[count]>0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="High School District"
        #
        # elif (PREKADM[count]==0 and ELEMADM[count]>0 and HSADM[count]==0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Elementary District"
        #
        # elif (PREKADM[count]==0 and ELEMADM[count]>0 and HSADM[count]>0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Unified District"
        #
        # elif (PREKADM[count]>0 and ELEMADM[count]==0 and HSADM[count]==0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Nottype"
        #
        # elif (PREKADM[count]>0 and ELEMADM[count]==0 and HSADM[count]>0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Nottype"
        #
        # elif (PREKADM[count]>0 and ELEMADM[count]>0 and HSADM[count]==0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Elementary District"
        #
        # elif (PREKADM[count]>0 and ELEMADM[count]>0 and HSADM[count]>0) and pred["FTFStatus"] == None:
        #     schooltype[pred['EntityID']]="Unified District"

        #calcschooltypeanddistricttype


        # if schooltype[pred['EntityID']]=="novalue" and pred['Type']=="Charter":
        #     schooltypeanddistricttype[pred['EntityID']]="novalue and Charter"
        #
        # elif schooltype[pred['EntityID']]=="High School District" and pred['Type']=="Charter":
        #     schooltypeanddistricttype[pred['EntityID']]="High School District and Charter"
        #
        # elif schooltype[pred['EntityID']]=="Elementary District" and pred['Type']=="Charter":
        #     schooltypeanddistricttype[pred['EntityID']]="Elementary District and Charter"
        #
        # elif schooltype[pred['EntityID']]=="Unified District" and pred['Type']=="Charter":
        #     schooltypeanddistricttype[pred['EntityID']]="Unified District and Charter"
        #
        # elif schooltype[pred['EntityID']]=="Nottype" and pred['Type']=="Charter":
        #     schooltypeanddistricttype[pred['EntityID']]="Nottype and Charter"
        #
        #
        # if schooltype[pred['EntityID']]=="novalue" and pred['Type']=="CTED":
        #     schooltypeanddistricttype[pred['EntityID']]="novalue and CTED"
        #
        # elif schooltype[pred['EntityID']]=="High School District" and pred['Type']=="CTED":
        #     schooltypeanddistricttype[pred['EntityID']]="High School District and CTED"
        #
        # elif schooltype[pred['EntityID']]=="Elementary District" and pred['Type']=="CTED":
        #     schooltypeanddistricttype[pred['EntityID']]="Elementary District and CTED"
        #
        # elif schooltype[pred['EntityID']]=="Unified District" and pred['Type']=="CTED":
        #     schooltypeanddistricttype[pred['EntityID']]="Unified District and CTED"
        #
        # elif schooltype[pred['EntityID']]=="Nottype" and pred['Type']=="CTED":
        #     schooltypeanddistricttype[pred['EntityID']]="Nottype and CTED"
        #
        #
        # if schooltype[pred['EntityID']]=="novalue" and pred['Type']=="District":
        #     schooltypeanddistricttype[pred['EntityID']]="novalue and District"
        #
        # elif schooltype[pred['EntityID']]=="High School District" and pred['Type']=="District":
        #     schooltypeanddistricttype[pred['EntityID']]="High School District and District"
        #
        # elif schooltype[pred['EntityID']]=="Elementary District" and pred['Type']=="District":
        #     schooltypeanddistricttype[pred['EntityID']]="Elementary District and District"
        #
        # elif schooltype[pred['EntityID']]=="Unified District" and pred['Type']=="District":
        #     schooltypeanddistricttype[pred['EntityID']]="Unified District and District"
        #
        # elif schooltype[pred['EntityID']]=="Nottype" and pred['Type']=="District":
        #     schooltypeanddistricttype[pred['EntityID']]="Nottype and District"


        count += 1
    entitynull=[]


    for d in decoded:
        # Creating a dictionary of the values retrieved from the query
        #d = dict(row.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS


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
            if NetworkHSADM[counter1] >= float(1) and NetworkHSADM[counter1] < float(100):
                HSRange[d['EntityID']]=("1to99")
            elif NetworkHSADM[counter1] >= float(100) and NetworkHSADM[counter1] < float(500):
                HSRange[d['EntityID']]=("100to499")
            elif NetworkHSADM[counter1] >= (float(500)) and NetworkHSADM[counter1] < (float(600)):
                HSRange[d['EntityID']]=("500to599")
            elif (NetworkHSADM[counter1] >= float(600)):
                HSRange[d['EntityID']]=(">600")
            else:
                HSRange[d['EntityID']]=(None)
            if NetworkElemADM[counter1] >= float(1) and NetworkElemADM[counter1] < float(100):
                ELEMRange[d['EntityID']]=("1to99")
            elif NetworkElemADM[counter1] >= float(100) and NetworkElemADM[counter1] < float(500):
                ELEMRange[d['EntityID']]=("100to499")
            elif NetworkElemADM[counter1] >= (float(500)) and NetworkElemADM[counter1] < (float(600)):
                ELEMRange[d['EntityID']]=("500to599")
            elif (NetworkElemADM[counter1] >= float(600)):
                ELEMRange[d['EntityID']]=(">600")
            else:
                ELEMRange[d['EntityID']]=(None)
        else:
            NetworkElemADM.append(0)
            NetworkHSADM.append(0)
            if sumhsadm[d['EntityID']] >= float(1) and sumhsadm[d['EntityID']] < float(100):
                HSRange[d['EntityID']]=("1to99")
            elif sumhsadm[d['EntityID']] >= float(100) and sumhsadm[d['EntityID']] < float(500):
                HSRange[d['EntityID']]=("100to499")
            elif sumhsadm[d['EntityID']] >= (float(500)) and sumhsadm[d['EntityID']] < (float(600)):
                HSRange[d['EntityID']]=("500to599")
            elif (sumhsadm[d['EntityID']] >= float(600)):
                HSRange[d['EntityID']]=(">600")
            else:
                HSRange[d['EntityID']]=(None)
            if sumelemadm[d['EntityID']] >= float(1) and sumelemadm[d['EntityID']] < float(100):
                ELEMRange[d['EntityID']]=("1to99")
            elif sumelemadm[d['EntityID']] >= float(100) and sumelemadm[d['EntityID']] < float(500):
                ELEMRange[d['EntityID']]=("100to499")
            elif sumelemadm[d['EntityID']] >= (float(500)) and sumelemadm[d['EntityID']] < (float(600)):
                ELEMRange[d['EntityID']]=("500to599")
            elif (sumelemadm[d['EntityID']] >= float(600)):
                ELEMRange[d['EntityID']]=(">600")
            else:
                ELEMRange[d['EntityID']]=(None)
        #CALCULATION OF SSWHSINCREMENTALWEIGHTPP
        if (d['Type'] == "CTED"):
            SSWHSINCREMENTALWEIGHTPP.append(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[d['EntityID']] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmallIso500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
            else:
                if HSRange[d['EntityID']] == "1to99":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    SSWHSINCREMENTALWEIGHTPP.append(IncWtSmall500to5999_12)
                else:
                    SSWHSINCREMENTALWEIGHTPP.append(0)
        #CALCULATION OF FinalHSBASEWEIGHT
        if (d['Type'] == "CTED"):
            HSBaseWeight[d['EntityID']]=(0)
        else:
            if d['HSSmallIsolated'] == 1:
                if HSRange[d['EntityID']] == "1to99":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    HSBaseWeight[d['EntityID']]=(WtSmallIso500to5999_12)
                else:
                    HSBaseWeight[d['EntityID']]=(0)
            else:
                if HSRange[d['EntityID']] == "1to99":
                    HSBaseWeight[d['EntityID']]=(WtSmall1to999_12)
                elif HSRange[d['EntityID']] == "100to499":
                    HSBaseWeight[d['EntityID']]=(WtSmall100to4999_12)
                elif HSRange[d['EntityID']] == "500to599":
                    HSBaseWeight[d['EntityID']]=(WtSmall500to5999_12)
                else:
                    HSBaseWeight[d['EntityID']]=(0)

        if HSRange[d['EntityID']]==None and ELEMRange[d['EntityID']]==None:
             entitynull.append(d['EntityID'])
        #     bothnull+=1
        # totalcount+=1
        #CALCUATION OF Final9-12WEIGHT
        if d['Type'] == "CTED":

            Final_9_12SmWgt[d['EntityID']]=GroupAFinalGroupAWeightsCTED
        else:
            if HSRange[d['EntityID']] == ">600":
                Final_9_12SmWgt[d['EntityID']]=(GroupAFinalGroupAWeights9_12)
            elif HSRange[d['EntityID']] == "1to99":
                Final_9_12SmWgt[d['EntityID']]=(HSBaseWeight[d['EntityID']])
            elif HSRange[d['EntityID']] == "100to499":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (float(float(500) - float(NetworkHSADM[counter1])))))
                else:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (float(float(500) - float(sumhsadm[d['EntityID']])))))
            elif HSRange[d['EntityID']] == "500to599":
                if d['NetworkForFundingPurposes'] == 1:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (float(float(600) - float(NetworkHSADM[counter1])))))
                else:
                    Final_9_12SmWgt[d['EntityID']]=(float(HSBaseWeight[d['EntityID']]) + (float(SSWHSINCREMENTALWEIGHTPP[counter1]) * (float(float(600) - float(sumhsadm[d['EntityID']])))))
            else:
                Final_9_12SmWgt[d['EntityID']]=(GroupAFinalGroupAWeights9_12)
        # CALCULATION OF SSWELEMINCREMENTALWEIGHTPP
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[d['EntityID']] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmallIso500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        else:
            if ELEMRange[d['EntityID']] == "1to99":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                SSWELEMINCREMENTALWEIGHTPP.append(IncWtSmall500to599K_8)
            else:
                SSWELEMINCREMENTALWEIGHTPP.append(0)
        # CALCULATION OF FINALELEMBASEWEIGHT
        if d['ESSmallIsolated'] == 1:
            if ELEMRange[d['EntityID']] == "1to99":
                ElemBaseWeight.append(WtSmallIso1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                ElemBaseWeight.append(WtSmallIso100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                ElemBaseWeight.append(WtSmallIso500to599K_8)
            else:
                ElemBaseWeight.append(0)
        else:
            if ELEMRange[d['EntityID']] == "1to99":
                ElemBaseWeight.append(WtSmall1to99K_8)
            elif ELEMRange[d['EntityID']] == "100to499":
                ElemBaseWeight.append(WtSmall100to499K_8)
            elif ELEMRange[d['EntityID']] == "500to599":
                ElemBaseWeight.append(WtSmall500to599K_8)
            else:
                ElemBaseWeight.append(0)
        # CALCUATION OF K-8WEIGHT
        if ELEMRange[d['EntityID']] == ">600":
            Final_K_8SmWgt[d['EntityID']]=(GroupAFinalGroupAWeightsK_8)
        elif ELEMRange[d['EntityID']] == "1to99":
            Final_K_8SmWgt[d['EntityID']]=(ElemBaseWeight[counter1])
        elif ELEMRange[d['EntityID']] == "100to499":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(500 - NetworkElemADM[counter1]))))
            else:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(500 - sumelemadm[d['EntityID']]))))
        elif ELEMRange[d['EntityID']] == "500to599":
            if d['NetworkForFundingPurposes'] == 1:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(600 - NetworkElemADM[counter1]))))
            else:
                Final_K_8SmWgt[d['EntityID']]=(float(ElemBaseWeight[counter1]) + (float(SSWELEMINCREMENTALWEIGHTPP[counter1]) * (float(600 - sumelemadm[d['EntityID']]))))
        else:
            Final_K_8SmWgt[d['EntityID']]=(GroupAFinalGroupAWeightsK_8)
        # CALCULATION OF VARIABLES FOR GROUP B WEIGHTS
        if Yeardef=="PY":
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
        elif Yeardef=="CY":
            if d['sumOfDSCSEDMIMRCnt'] == None:
                d['sumOfDSCSEDMIMRCnt'] = 0
            if d['sumOfEDMIMRCYCnt'] == None:
                d['sumOfEDMIMRCYCnt'] = 0
            GB1_EDMIDSLD.append(float(d['sumOfEDMIMRCYCnt']) + float(d['sumOfDSCSEDMIMRCnt']))
            if d['sumOfK3CYCnt'] == None:
                d['sumOfK3CYCnt'] = 0
            if d['SumOfDSCSK3Cnt'] == None:
                d['SumOfDSCSK3Cnt'] = 0
            GB2_K3Reading.append(float(d['sumOfK3CYCnt']) + float(d['SumOfDSCSK3Cnt']))
            GB3_K3.append(float(d['sumOfK3CYCnt']) + float(d['SumOfDSCSK3Cnt']))
            if d['sumOfLEPCYCnt'] == None:
                d['sumOfLEPCYCnt'] = 0
            if d['sumOfDSCSLEPCnt'] == None:
                d['sumOfDSCSLEPCnt'] = 0
            GB4_ELL.append(float(d['sumOfLEPCYCnt']) + float(d['sumOfDSCSLEPCnt']))
            if d['sumOfOIResCYCnt'] == None:
                d['sumOfOIResCYCnt'] = 0
            if d['sumOfDSCSOIResCnt'] == None:
                d['sumOfDSCSOIResCnt'] = 0
            GB5_OI_R.append(float(d['sumOfOIResCYCnt']) + float(d['sumOfDSCSOIResCnt']))
            if d['sumOfPSDCYCnt'] == None:
                d['sumOfPSDCYCnt'] = 0
            if d['sumOfDSCSPSDCnt'] == None:
                d['sumOfDSCSPSDCnt'] = 0
            GB6_PS_D.append(float(d['sumOfPSDCYCnt']) + float(d['sumOfDSCSPSDCnt']))
            if d['sumOfMOMRCYCnt'] == None:
                d['sumOfMOMRCYCnt'] = 0
            if d['sumOfDSCSMOMRCnt'] == None:
                d['sumOfDSCSMOMRCnt'] = 0
            GB7_MOID.append(float(d['sumOfMOMRCYCnt']) + float(d['sumOfDSCSMOMRCnt']))
            if d['sumOfHICYCnt'] == None:
                d['sumOfHICYCnt'] = 0
            if d['sumOfDSCSHICnt'] == None:
                d['sumOfDSCSHICnt'] = 0
            GB8_HI.append(float(d['sumOfHICYCnt']) + float(d['sumOfDSCSHICnt']))
            if d['sumOfVICYCnt'] == None:
                d['sumOfVICYCnt'] = 0
            if d['sumOfDSCSVICnt'] == None:
                d['sumOfDSCSVICnt'] = 0
            GB9_VI.append(float(d['sumOfVICYCnt']) + float(d['sumOfDSCSVICnt']))
            if d['sumOfEDPPrivateCYCnt'] == None:
                d['sumOfEDPPrivateCYCnt'] = 0
            if d['sumOfDSCSEDPPrivateCnt'] == None:
                d['sumOfDSCSEDPPrivateCnt'] = 0
            GB10_ED_P.append(float(d['sumOfEDPPrivateCYCnt']) + float(d['sumOfDSCSEDPPrivateCnt']))
            if d['sumOfMDSCCYCnt'] == None:
                d['sumOfMDSCCYCnt'] = 0
            if d['sumOfDSCSMDSCCnt'] == None:
                d['sumOfDSCSMDSCCnt'] = 0
            GB11_MDSC.append(float(d['sumOfMDSCCYCnt']) + float(d['sumOfDSCSMDSCCnt']))
            if d['sumOfMDResCYCnt'] == None:
                d['sumOfMDResCYCnt'] = 0
            if d['sumOfDSCSMDResCnt'] == None:
                d['sumOfDSCSMDResCnt'] = 0
            GB12_MD_R.append(float(d['sumOfMDResCYCnt']) + float(d['sumOfDSCSMDResCnt']))
            if d['sumOfOISCCYCnt'] == None:
                d['sumOfOISCCYCnt'] = 0
            if d['sumOfDSCSOISCCnt'] == None:
                d['sumOfDSCSOISCCnt'] = 0
            GB13_OI_SC.append(float(d['sumOfOISCCYCnt']) + float(d['sumOfDSCSOISCCnt']))
            if d['sumOfMDSSICYCnt'] == None:
                d['sumOfMDSSICYCnt'] = 0
            if d['sumOfDSCSMDSSICnt'] == None:
                d['sumOfDSCSMDSSICnt'] = 0
            GB14_MD_SSI.append(float(d['sumOfMDSSICYCnt']) + float(d['sumOfDSCSMDSSICnt']))
        if d["TEI"] == None:
            d["TEI"] = 0
        # CALCULATION OF TEI
        TEI.append(float(max(TEI10, d["TEI"])))

        # calculation of BASEAMOUNT
        if float(d["MaxOfBaseAmount"]) == actualTeachercomp:
            LEABaseLevel1.append(round(BaseSupport * (1 + (TeacherCompPercent / 100)), 2))
        elif float(d["MaxOfBaseAmount"]) == actual200daycalender:
            LEABaseLevel1.append(round(BaseSupport + (BaseSupport * (Percent200DayCalender) / 100), 2))
        elif float(d["MaxOfBaseAmount"]) == actualTeacherCompAnd200DayCalender:

            LEABaseLevel1.append(round(
            (BaseSupport * (1 + (TeacherCompPercent / 100))) + (BaseSupport * (1 + (TeacherCompPercent / 100))) * (
                        Percent200DayCalender / 100), 2))
        elif float(d["MaxOfBaseAmount"]) == actualBaseSupport:

            LEABaseLevel1.append(BaseSupport)

        else:
            LEABaseLevel1.append(float(d["MaxOfBaseAmount"]))
        # if TeacherComp[counter1]==1:
        #    LEABaseLevel.append(float(d["MaxOfBaseAmount"])+(float(d["MaxOfBaseAmount"])*TeacherCompPercent))
        # elif techercompand200daycalender[counter1]==1:

        #   LEABaseLevel.append(float(d["MaxOfBaseAmount"]) + (float(d["MaxOfBaseAmount"]) * Percent200DayCalender))
        # else:

        # calculation of O
        WeightedElemCounts.append(float(ELEMADM[counter1]) * round(float(Final_K_8SmWgt[d['EntityID']]),3))
        # calculation of P
        WeightedHSCounts.append(float(HSADM[counter1]) * round(float(Final_9_12SmWgt[d['EntityID']]),3))
        # CALCULATION of WEIGHTED PREKCOUNT
        WeightedPreKCounts.append(float(PREKADM[counter1] * float(GroupAFinalGroupAWeightsPSD)))
        # CALCULATION OF PREKBSL
        if d['FTFStatus'] == '1':
            PrekBSL.append((float(TEI[counter1])) * (float(LEABaseLevel1[counter1])) * round(float(WeightedPreKCounts[counter1]),3) * float(FullTimeAOI))
        elif d['FTFStatus'] == '0':
            PrekBSL.append((float(TEI[counter1])) * (float(LEABaseLevel1[counter1])) * round(float(WeightedPreKCounts[counter1]),3) * float(HalfTimeAOI))
        else:
            PrekBSL.append((float(TEI[counter1])) * (float(LEABaseLevel1[counter1])) * round(float(WeightedPreKCounts[counter1]),3))
        # CALCULATION OF ELEMBSL AND HSBSL
        if (d["FTFStatus"] == '0'):
            ELEMBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]),3) * float(HalfTimeAOI))
            HSBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]),3) * float(HalfTimeAOI))
        elif (d["FTFStatus"] == '1'):
            ELEMBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]),3) * float(FullTimeAOI))
            HSBSL.append(
                (float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]),3) * float(FullTimeAOI))
        else:
            ELEMBSL.append(
                ((LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedElemCounts[counter1]),3))
            HSBSL.append(
                (float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(WeightedHSCounts[counter1]),3))
        # CALCULATION OF VARIABLES FOR Q(GROUP B WEIGHTED ADD ON COUNTS) FROM STUDENT COUNTS FY2016_CLEAN
        Weighted_GB1_EDMIDSLD.append(float(GB1_EDMIDSLD[counter1]) * float(GroupB1))
        Weighted_GB2_K3Reading.append(float(GB2_K3Reading[counter1]) * float(GroupB2))
        Weighted_GB3_K3.append(float(GB3_K3[counter1]) * float(GroupB3))
        Weighted_.append(float(GB4_ELL[counter1]) * float(GroupB4))
        Weighted_GB5_OI_R.append(float(GB5_OI_R[counter1]) * float(GroupB5))
        Weighted_GB6_PS_D.append(float(GB6_PS_D[counter1]) * float(GroupB6))
        Weighted_GB7_MOID.append(float(GB7_MOID[counter1]) * float(GroupB7))
        Weighted_GB8_HI.append(float(GB8_HI[counter1]) * float(GroupB8))
        Weighted_GB9_VI.append(float(GB9_VI[counter1]) * float(GroupB9))
        Weighted_GB10_ED_P.append(float(GB10_ED_P[counter1]) * float(GroupB10))
        Weighted_GB11_MDSC.append(float(GB11_MDSC[counter1]) * float(GroupB11))
        Weighted_GB12_MD_R.append(float(GB12_MD_R[counter1]) * float(GroupB12))
        Weighted_GB13_OI_SC.append(float(GB13_OI_SC[counter1]) * float(GroupB13))
        Weighted_GB14_MD_SSI.append(float(GB14_MD_SSI[counter1]) * float(GroupB14))
        # CALCULATION OF GROUP B WEIGHTED ADD ON COUNTS
        GroupBWeightedAddonCounts.append(
            round(Weighted_GB1_EDMIDSLD[counter1],3) + round(Weighted_GB2_K3Reading[counter1],3) + round(Weighted_GB3_K3[counter1],3) + round(Weighted_[counter1],3) +
            round(Weighted_GB5_OI_R[counter1],3) + round(Weighted_GB6_PS_D[counter1],3) + round(Weighted_GB7_MOID[counter1],3) + round(Weighted_GB8_HI[counter1],3) +
            round(Weighted_GB9_VI[counter1],3) + round(Weighted_GB10_ED_P[counter1],3) + round(Weighted_GB11_MDSC[counter1],3) + round(Weighted_GB12_MD_R[counter1],3) +
            round(Weighted_GB13_OI_SC[counter1],3) + round(Weighted_GB14_MD_SSI[counter1],3))
        # CALCULATION OF GROUP B BSL
        if (d["FTFStatus"] == '0'):
            GroupBBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(GroupBWeightedAddonCounts[counter1]),3) * (float(HalfTimeAOI)))

        elif (d["FTFStatus"] == '1'):
            GroupBBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) * round(float(GroupBWeightedAddonCounts[counter1]),3) *(float(FullTimeAOI)))
        else:
            GroupBBSL.append((float(LEABaseLevel1[counter1])) * (float(TEI[counter1])) *round(float(GroupBWeightedAddonCounts[counter1]),3))
        # CALCULATION OF AuditBaseLevelAdjustment
        if (d["FTFStatus"] == None):
            AuditBaseLevelAdjustment.append(float(d["MaxofBaseAdjsAmount"]))
        else:
            AuditBaseLevelAdjustment.append(float(0))
        # CALCULATION OF LOSS FROM SSW OF K-8 FUNDING AND LOSS FROM SSW OF 9-12 FUNDING
        AB2.append(float(LEABaseLevel1[counter1]) * float(Final_K_8SmWgt[d['EntityID']]) * float(ELEMADM[counter1]))
        AH.append(0)
        # AH.append(float(AB2[counter1])-float(AB2[counter1]*float(sixtyseven/100)))
        AC2.append(float(LEABaseLevel1[counter1]) * float(Final_9_12SmWgt[d['EntityID']]) * float(HSADM[counter1]))
        AI.append(0)
        # AI.append(float(AC2[counter1]) - float(AC2[counter1] * float(sixtyseven / 100)))
        # CALCULATION OF BSL VALUE
        BSLWithoutAdjustment.append((float(PrekBSL[counter1]) + float(ELEMBSL[counter1]) + round(float(HSBSL[counter1]), 3) + round(float(GroupBBSL[counter1]), 3)  ))
        BSL.append((float(PrekBSL[counter1]) + float(ELEMBSL[counter1]) + round(float(HSBSL[counter1]),3) + round(float(GroupBBSL[counter1]),3) + float(AuditBaseLevelAdjustment[counter1])))

        SumofBSL[d['EntityID']]+=BSL[counter1]
        sumofadm[d['EntityID']]+=ELEMADM[counter1]+PREKADM[counter1]+HSADM[counter1]
        if d['County'] not in bslbyCounty:
            bslbyCounty[d['County']]=BSL[counter1]
        else:
            bslbyCounty[d['County']]+=BSL[counter1]
        if d['County'] not in admbyCounty:
            admbyCounty[d['County']]=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        else:
            admbyCounty[d['County']]+=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])

        if d['EHType'] not in bslbyEHType:
            bslbyEHType[d['EHType']]=BSL[counter1]
        else:
            bslbyEHType[d['EHType']]+=BSL[counter1]
        if d['EHType'] not in admbyEHType:
            admbyEHType[d['EHType']]=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        else:
            admbyEHType[d['EHType']]+=(PREKADM[counter1]+ELEMADM[counter1]+HSADM[counter1])
        # if schooltype[d['EntityID']] not in bslbyschooltype:
        #     bslbyschooltype[schooltype[d['EntityID']]] = BSL[counter1]
        # else:
        #     bslbyschooltype[schooltype[d['EntityID']]] += BSL[counter1]
        # if schooltype[d['EntityID']] not in admbyschooltype:
        #     admbyschooltype[schooltype[d['EntityID']]] = (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])
        # else:
        #     admbyschooltype[schooltype[d['EntityID']]] += (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])

        if d['Type'] not in bslbytype:
            bslbytype[d['Type']]=float(SumofBSL[d['EntityID']])
        else:
            bslbytype[d['Type']]+=float(SumofBSL[d['EntityID']])
        if d['Type'] not in admbytype:
            admbytype[d['Type']]=float(sumofadm[d['EntityID']])
        else:
            admbytype[d['Type']]+=float(sumofadm[d['EntityID']])

        #calculate by type and schooltype
        # if schooltypeanddistricttype[d['EntityID']] not in bslbyschooltypeanddistricttype:
        #     bslbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] = BSL[counter1]
        # else:
        #     bslbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] += BSL[counter1]
        # if schooltypeanddistricttype[d['EntityID']] not in admbyschooltypeanddistricttype:
        #     admbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] = (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])
        # else:
        #     admbyschooltypeanddistricttype[schooltypeanddistricttype[d['EntityID']]] += (PREKADM[counter1] + ELEMADM[counter1] + HSADM[counter1])



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
        TotalCharterElemReduction.append(float(CharterReduction) * float(K_8PercentofTotalcharterAA[counter1]))
        TotalCharterHSReduction.append(float(CharterReduction) * float((1 - float(K_8PercentofTotalcharterAA[counter1]))))
        CharterElemAAReduction.append(float(LEApercentofCharterElemADM[counter1]) * float(TotalCharterElemReduction[counter1]))
        CharterHSAAReduction.append(float(LEApercentofCharterHSADM[counter1]) * float(TotalCharterHSReduction[counter1]))
        TotalNetCharterAA.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]) - (float(CharterElemAAReduction[counter1] + CharterHSAAReduction[counter1])))
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
            FinalFormulaAAwithReduction.append(float(TotalNetCharterAA[counter1]))
            FinalFormulaAdditionalAssistance.append(float(CharterElemAA[d['EntityID']] + CharterHSAA[d['EntityID']]))
        else:
            if AdditionalAssistant_eqformula == 2:

                DistrictHSTextbooksAA.append(0)
                DistrictPreKAA.append(float(DistSuppLvlAllPSD * sumprekadm[d['EntityID']]))

                if HSRange[d['EntityID']] == "1to99":
                    DistrictHSAA.append(float(DistSuppLvl1to999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[d['EntityID']] == "100to499" or HSRange[d['EntityID']] == "100to499":
                    DistrictHSAA.append(float(DistSuppLvl100to5999_12 * sumhsadm[d['EntityID']]))
                elif HSRange[d['EntityID']] == ">600":
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                else:
                    DistrictHSAA.append(float(DistSuppLvl600AndOver9_12 * sumhsadm[d['EntityID']]))
                if ELEMRange[d['EntityID']] == "1to99":
                    DistrictElemAA.append(float(DistSuppLvl1to99K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[d['EntityID']] == "100to499" or ELEMRange[d['EntityID']] == "500to599":
                    DistrictElemAA.append(float(DistSuppLvl100to599K_8 * sumelemadm[d['EntityID']]))
                elif ELEMRange[d['EntityID']] == ">600":
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
            TotalDistrictAAReduction.append(float(DistrictPreKElemReduction[counter1] + DistrictHSReduction[counter1]))
            TotalFormulaDistrictAA.append(float(DistrictHSTextbooksAA[counter1] + DistrictHSAA[counter1] + DistrictElemAA[counter1] + DistrictPreKAA[counter1]))
            TotalNetDistrictAA.append(float(TotalFormulaDistrictAA[counter1] + TotalDistrictAAReduction[counter1]))
            FinalFormulaAAwithReduction.append(TotalNetDistrictAA[counter1])
            FinalFormulaAdditionalAssistance.append(TotalFormulaDistrictAA[counter1])

        # CALCULATION OF FINALAAALLOCATION

        if AdditonalAssistantReduction == 1:
            if d['Type'] == "Charter":
                CAA+=(FinalFormulaAAwithReduction[counter1])
            else:
                DAA+=(FinalFormulaAAwithReduction[counter1])
            FinalAAAllocation.append(FinalFormulaAAwithReduction[counter1])
        else:
            if d['Type']=="Charter":
                CAA+=FinalFormulaAdditionalAssistance[counter1]
            else:
                DAA+=FinalFormulaAdditionalAssistance[counter1]
            FinalAAAllocation.append(FinalFormulaAdditionalAssistance[counter1])

        AdditionalAssistance.append(FinalAAAllocation[counter1])
        sumAdditionalAssistance+=FinalAAAllocation[counter1]
        OppurtunityWeight.append(float(0))
        if d['TRCL'] == None:
            d['TRCL'] = 0
        if d['TSL'] == None:
            d['TSL'] = 0
        TRCL.append(float(d['TRCL']))
        TSL.append(float(d['TSL']))
        # CALCULATION OF  WEIGHTED PUPILS USER SPECIFIED SSW REDUCTION
        PreKWeightedPupilsuser_specifiedSWWreduction.append(
            float(float(PREKADM[counter1] * float(GroupAFinalGroupAWeightsPSD)) - 0))
        K_8WeightedPupilsuser_specifiedSWWreduction.append((float(ELEMADM[counter1]) * float(Final_K_8SmWgt[d['EntityID']])) - 0)
        nine_12WeightedPupilsuser_specifiedSWWreduction.append((float(HSADM[counter1]) * float(Final_9_12SmWgt[d['EntityID']])) - 0)
        SumofPreKWeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += PreKWeightedPupilsuser_specifiedSWWreduction[counter1]
        Sumofk_8WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += K_8WeightedPupilsuser_specifiedSWWreduction[counter1]
        Sumof9_12WeightedPupilsuser_specifiedSWWreduction[d['EntityID']] += nine_12WeightedPupilsuser_specifiedSWWreduction[counter1]
        counter1 += 1
    counter2 = 0
    for i in bslbyCounty:
        if admbyCounty[i]==0:
            perpupilbyCounty[i]=0
        else:
            perpupilbyCounty[i]=(bslbyCounty[i]/admbyCounty[i])
    for i in bslbytype:
        if admbytype[i]==0:
            perpupilpertype[i] =0
        else:
            perpupilpertype[i]=(bslbytype[i]/3)/(admbytype[i]/3)
    for i in bslbyEHType:
        if admbyEHType[i]==0:
            perpupilbyEHType[i]=0
        else:
            perpupilbyEHType[i]=(bslbyEHType[i]/admbyEHType[i])
    # for i in bslbyschooltype:
    #     if admbyschooltype[i]==0:
    #         perpupilbyschooltype[i] =0
    #     else:
    #         perpupilbyschooltype[i]=(bslbyschooltype[i]/admbyschooltype[i])
    # for i in bslbyschooltypeanddistricttype:
    #     if admbyschooltypeanddistricttype[i]==0:
    #         perpupilbyschooltypeanddistricttype[i]=0
    #     else:
    #         perpupilbyschooltypeanddistricttype[i]=(bslbyschooltypeanddistricttype[i]/admbyschooltypeanddistricttype[i])

    for d4 in range(len(decoded)):
        dictionary = {}
        # Creating a dictionary of the values retrieved from the query
        #d4 = dict(row1.items())
        # MAKING THE TYPE OF SCHOOL COMPACT FOR CALCULATIONS

        # CALCULATION OF PERCENTAGE OF PREK_8 OF TOTAL AND HS OF TOTAL
        temp5 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        temp6 = SumofPreKWeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumof9_12WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']] + \
                Sumofk_8WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        temp7 = Sumof9_12WeightedPupilsuser_specifiedSWWreduction[decoded[d4]['EntityID']]
        if temp6 == 0:
            PercPreK_8ofTotal.append(float(0))
            PercHSofTotal.append(float(0))
        else:
            PercPreK_8ofTotal.append(float(temp5) / float(temp6))
            PercHSofTotal.append(float(temp7) / float(temp6))

        if decoded[d4]['HSTuitionOutAmt1']==None:
            decoded[d4]['HSTuitionOutAmt1']=0
        RCL.append(float(SumofBSL[decoded[d4]['EntityID']]) + OppurtunityWeight[counter2] + TRCL[counter2] + float(decoded[d4]['HSTuitionOutAmt1']) )
        DSL.append(float(SumofBSL[decoded[d4]['EntityID']] + OppurtunityWeight[counter2] + TSL[counter2]+ float(decoded[d4]['HSTuitionOutAmt1'])))
        TotalStateEqualisationFunding.append(min(RCL[counter2], DSL[counter2]))
        # CALCULATION OF ELEMENTARY AND HSTOTALSTATE FORMULA
        ElemTotalStateFormula.append(float(TotalStateEqualisationFunding[counter2]) * float(PercPreK_8ofTotal[counter2]))
        HSTotalStateFormula.append(float(TotalStateEqualisationFunding[counter2]) * float(PercHSofTotal[counter2]))
        # CALCULATION OF lOCAL LEVY
        if decoded[d4]['TotalHSAssessValAmt'] == None:
            decoded[d4]['TotalHSAssessValAmt'] = 0
        HSAssessedValuation.append(float(decoded[d4]['TotalHSAssessValAmt']))
        if sumhsadm[decoded[d4]['EntityID']] == 0:
            HSQTRYield.append(0)
        elif decoded[d4]['Type'] == "CTED":
            HSQTRYield.append(float(HSAssessedValuation[counter2]) * float(0.01) * float(QTRCTED))
        else:
            HSQTRYield.append(float(HSAssessedValuation[counter2]) * float(0.01) * float(QTR9_12))
        HSLL.append(min(HSTotalStateFormula[counter2], HSQTRYield[counter2]))
        if decoded[d4]['TotalPSElAssessValAmt'] == None:
            decoded[d4]['TotalPSElAssessValAmt'] = 0
        ElemAssessedValuation.append(float(decoded[d4]['TotalPSElAssessValAmt']))
        if sumelemadm[decoded[d4]['EntityID']] == 0:
            ElemQTRYield.append(0)
        else:
            ElemQTRYield.append(float(ElemAssessedValuation[counter2]) * float(QTRK_8) * float(0.01))
        ElemLL.append(min(ElemTotalStateFormula[counter2], ElemQTRYield[counter2]))
        TotalLocalLevy.append(ElemLL[counter2] + HSLL[counter2])
        sumTotalLocalLevy+=ElemLL[counter2] + HSLL[counter2]
        # CALCUALTION OF TOTAL STATE AID
        if ElemTotalStateFormula[counter2] > ElemQTRYield[counter2]:
            ElemStateAid.append(float(ElemTotalStateFormula[counter2] - ElemQTRYield[counter2]))
        else:
            ElemStateAid.append(0)
        if HSTotalStateFormula[counter2] > HSQTRYield[counter2]:
            HSStateAid.append(float(HSTotalStateFormula[counter2] - HSQTRYield[counter2]))
        else:
            HSStateAid.append(0)
        TotalStateAid.append(ElemStateAid[counter2] + HSStateAid[counter2])

        # CALCULATION OF NO STATE AID
        if ((float(PREKADM[counter2]) + float(sumelemadm[decoded[d4]['EntityID']])) > 0) and (float(ElemStateAid[counter2]) == 0):
            ElemNoStateAidDistrict.append(float(1))
        else:
            ElemNoStateAidDistrict.append(float(0))
        if (sumhsadm[decoded[d4]['EntityID']] > 0) and (HSStateAid[counter2] == 0):
            HSNoStateAidDistrict.append(float(1))
        else:
            HSNoStateAidDistrict.append(float(0))
        if ((float(ElemNoStateAidDistrict[counter2]) + float(HSNoStateAidDistrict[counter2])) > 0) and (float(TotalStateAid[counter2]) == 0):
            NoStateAidDistrict.append(float(1))
        else:
            NoStateAidDistrict.append(float(0))
        TotalQTRYield.append(float(ElemQTRYield[counter2] + HSQTRYield[counter2]))
        UncapturedQTR.append(float(TotalQTRYield[counter2] - TotalLocalLevy[counter2]))
        TotalStateFundingEqualised.append(float(ElemTotalStateFormula[counter2] + HSTotalStateFormula[counter2]))
        if decoded[d4]['ESSmallIsolated'] == None:
            decoded[d4]['ESSmallIsolated'] = 0
        if decoded[d4]['HSSmallIsolated']==None:
            decoded[d4]['HSSmallIsolated']=0
        EqualisationAssistance.append(TotalStateEqualisationFunding[counter2]+AdditionalAssistance[counter2]+decoded[d4]['HSTuitionOutAmt1']-TotalLocalLevy[counter2])
        #df=pandas.DataFrame(entitynull)
        #df.to_csv('C:/Users/jjoth/Desktop/asu/EA/entityfile.csv')
        dictionary['EqualisationAssistance']=str(round(EqualisationAssistance[counter2],4))
        #dictionary['ElemAssessedValuation']=str(round(ElemAssessedValuation[counter2],4))
        #dictionary['ElemQTRYield'] =str(round(ElemQTRYield[counter2], 4))
        #dictionary['ElemTotalStateFormula']=str(round(ElemTotalStateFormula[counter2], 4))
        #dictionary['HSTotalStateFormula']=str(round(HSTotalStateFormula[counter2], 4))
        dictionary['TotalStateEqualisationFunding'] = str(round(TotalStateEqualisationFunding[counter2], 4))
        #dictionary['DistrictPreKElemReduction']=str(round(DistrictPreKElemReduction[counter2], 4))
        #dictionary['DistrictHSReduction'] = str(round(DistrictHSReduction[counter2], 4))
        #dictionary['TotalDistrictAAReduction'] = str(round(TotalDistrictAAReduction[counter2], 4))
        #dictionary['NetworkForFundingPurposes']=str(decoded[d4]['NetworkForFundingPurposes'])
        dictionary['EntityID'] = EID[counter2]
        dictionary['prekadm'] = str(round(PREKADM[counter2], 4))
        #dictionary['NoStateAidDistrict'] = str(round(NoStateAidDistrict[counter2], 4))
        dictionary['EntityName'] = Ename[counter2]
        # dictionary['schooltype']=str(schooltype[decoded[d4]['EntityID']])
        dictionary['County'] = decoded[d4]['County']
        #dictionary['AOI'] = str(decoded[d4]['FTFStatus'])
        #dictionary['TEI'] = str(round(TEI[counter2], 5))
        dictionary['Type']=str(decoded[d4]['Type'])
        # dictionary['bslbyschooltype'] = str(round(bslbyschooltype[schooltype[decoded[d4]['EntityID']]],2))
        # dictionary['admbyschooltype'] = str(round(admbyschooltype[schooltype[decoded[d4]['EntityID']]],2))
        dictionary['bslbytype']=str(round((bslbytype[decoded[d4]['Type']]/3),2))
        dictionary['admbytype']=str(round((admbytype[decoded[d4]['Type']]/3),2))
        #dictionary['perpupilbyschooltypecalc']=str(round((perpupilbyschooltype[schooltype[decoded[d4]['EntityID']]]),2))
        #dictionary['perpupilbyschooltypedefault'] = str(round(float(Original[counter2]['perpupilbyschooltype']), 4))
        #dictionary['perpupilbyschooltypedifference'] = round((perpupilbyschooltype[schooltype[decoded[d4]['EntityID']]])-(float(Original[counter2]['perpupilbyschooltype'])),2)
        #dictionary['perpupilbyschooltypeanddistricttypecalc'] = str(round((perpupilbyschooltypeanddistricttype[schooltypeanddistricttype[decoded[d4]['EntityID']]]), 2))
        #dictionary['perpupilbyschooltypeanddistricttypedefault'] = str(round(float(Original[counter2]['perpupilbyschooltypeanddistricttype']), 4))
        #dictionary['perpupilbyschooltypeanddistricttypedifference'] = round((perpupilbyschooltypeanddistricttype[schooltypeanddistricttype[decoded[d4]['EntityID']]])-float(Original[counter2]['perpupilbyschooltypeanddistricttype']), 2)
        dictionary['perpupilpertypecalc']=str(round((perpupilpertype[decoded[d4]['Type']]),2))
        dictionary['perpupilpertypedefault'] = str(round(float(Original[counter2]['perpupilpertype']), 4))
        dictionary['perpupilpertypedifference'] = round(perpupilpertype[decoded[d4]['Type']]-float(Original[counter2]['perpupilpertype']),2)
        #dictionary['DistrictHSTextbooksAA'] = str(round(DistrictHSTextbooksAA[counter2], 5))
        #dictionary['DistrictHSAA'] = str(round(DistrictHSAA[counter2], 5))
        #dictionary['DistrictElemAA'] = str(round(DistrictElemAA[counter2], 5))
        #dictionary['DistrictPreKAA'] = str(round(DistrictPreKAA[counter2], 5))
        dictionary['bslbyCounty'] = str(round(bslbyCounty[decoded[d4]['County']], 2))
        dictionary['admbyCounty'] = str(round(admbyCounty[decoded[d4]['County']], 2))
        dictionary['perpupilbyCountycalc'] = str(round(perpupilbyCounty[decoded[d4]['County']], 2))
        dictionary['perpupilbyCountydefault'] = str(round(float(Original[counter2]['perpupilbyCounty']), 4))
        dictionary['perpupilbyCountydifference'] = str(round(perpupilbyCounty[decoded[d4]['County']] - float(Original[counter2]['perpupilbyCounty']), 2))
        dictionary['bslbyEHType'] = str(round(bslbyEHType[schoolEHType[decoded[d4]['EntityID']]], 2))
        dictionary['admbyEHType'] = str(round(admbyEHType[schoolEHType[decoded[d4]['EntityID']]], 2))
        dictionary['perpupilbyEHTypedefault'] = str(round(float(Original[counter2]['perpupilbyEHType']), 4))
        dictionary['perpupilbyEHTypecalc'] = str(round(perpupilbyEHType[schoolEHType[decoded[d4]['EntityID']]], 2))
        dictionary['perpupilbyEHTypedifference'] = str(round(perpupilbyEHType[schoolEHType[decoded[d4]['EntityID']]]-float(Original[counter2]['perpupilbyEHType']), 2))
        dictionary['hsadm'] = str(round(HSADM[counter2], 4))
        dictionary['elemadm'] = str(round(ELEMADM[counter2], 4))
        dictionary['sumofadm']=str(round(sumofadm[decoded[d4]['EntityID']],2))
        dictionary['prekbsl'] = str(round(PrekBSL[counter2], 4))
        dictionary['elembsl'] = str(round(ELEMBSL[counter2], 4))
        dictionary['hsbsl'] = str(round(HSBSL[counter2], 4))
        dictionary['BSLcalc'] = str(round(BSL[counter2], 2))
        dictionary['TotalBSLcalc']=str(round(sum(SumofBSL.values()),2))
        dictionary['TotalBSLoriginal']=str(round(float(Original[counter2]['TotalBSL']),2))
        dictionary['TotalBSLdifference'] = str(round(sum(SumofBSL.values())-float(Original[counter2]['TotalBSL']), 2))
        dictionary['BSLoriginal'] = str(round(float(Original[counter2]['BSL']), 2))
        dictionary['BSLdiffernce']=str((round(float(BSL[counter2])-float(Original[counter2]['BSL']), 2)))
        dictionary['SumofBSLcalc']=str(round(SumofBSL[decoded[d4]['EntityID']], 4))
        dictionary['SumofBSLoriginal'] = str(round(float(Original[counter2]['SumofBSL']), 4))
        dictionary['SumofBSLdifference'] = str(round(SumofBSL[decoded[d4]['EntityID']], 4)-round(float(Original[counter2]['SumofBSL']), 4))
        if sumofadm[decoded[d4]['EntityID']] ==0:
            dictionary['sumofBSLcalcperpupilcalc'] = str(0)
            dictionary['sumofBSLcalcperpupildifference'] = str(0-round(float(Original[counter2]['sumofBSLcalcperpupil']),4))
        else:
            dictionary['sumofBSLcalcperpupilcalc']=str(round(round(SumofBSL[decoded[d4]['EntityID']], 2)/(sumofadm[decoded[d4]['EntityID']]),2))
            dictionary['sumofBSLcalcperpupildifference'] = str(round(round(round(SumofBSL[decoded[d4]['EntityID']], 2)/(sumofadm[decoded[d4]['EntityID']]),2)-round(float(Original[counter2]['sumofBSLcalcperpupil']), 4),2))
        dictionary['sumofBSLcalcperpupildefault'] = str(round(float(Original[counter2]['sumofBSLcalcperpupil']), 4))
        #dictionary['WeightedPreKCounts'] = str(round(WeightedPreKCounts[counter2], 3))
        #dictionary['WeightedElemCounts'] = str(round(WeightedElemCounts[counter2], 3))
        #dictionary['WeightedHSCounts'] = str(round(WeightedHSCounts[counter2], 3))
        dictionary['TotalLocalLevycalc'] = str(round(TotalLocalLevy[counter2], 3))
        dictionary['TotalLocalLevyoriginal'] = str(round(float(Original[counter2]['TotalLocalLevy']), 3))
        dictionary['TotalLocalLevydifference'] = str(round(TotalLocalLevy[counter2], 3)-round(float(Original[counter2]['TotalLocalLevy']), 3))
        dictionary['UncapturedQTR'] = str(round(UncapturedQTR[counter2], 3))
        dictionary['TotalStateAidcalc'] = str(round(TotalStateAid[counter2], 3))
        dictionary['TotalStateAidoriginal'] = str(round(float(Original[counter2]['TotalStateAid']), 3))
        dictionary['TotalStateAiddifference'] = str(round(TotalStateAid[counter2]-float(Original[counter2]['TotalStateAid']), 3))
        #dictionary['Final_K_8SmWgt'] = str(round(Final_K_8SmWgt[decoded[d4]['EntityID']], 3))
        #dictionary['Final_9_12SmWgt'] = str(round(Final_9_12SmWgt[decoded[d4]['EntityID']], 3))
        dictionary['RCLcalc'] = str(round(RCL[counter2], 4))
        dictionary['RCLoriginal'] = str(round(float(Original[counter2]['RCL']), 4))
        dictionary['RCLdifference'] = str(round(RCL[counter2], 4)-round(float(Original[counter2]['RCL']), 4))
        dictionary['TRCL'] = str(round(TRCL[counter2], 4))
        dictionary['DSLcalc'] = str(round(DSL[counter2], 4))
        dictionary['DSLoriginal'] = str(round(float(Original[counter2]['DSL']), 4))
        dictionary['DSLdifference'] = str(round(DSL[counter2], 4)-round(float(Original[counter2]['DSL']), 4))
        dictionary['TSL'] = str(round(TSL[counter2], 4))
        dictionary['TutionoutCount']=str(decoded[d4]['TuitionOutCnt'])
        dictionary['HSTuitionOutAmt']=decoded[d4]['HSTuitionOutAmt1']
        dictionary['LEABaseLevel'] = str(round(LEABaseLevel1[counter2], 4))
        dictionary['BSLWithoutAdjustment']=str(round(BSLWithoutAdjustment[counter2],4))
        #dictionary['PreKWeightedPupilsuser_specifiedSWWreduction'] = str(round(PreKWeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        #dictionary['K_8WeightedPupilsuser_specifiedSWWreduction'] = str(round(K_8WeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        #dictionary['nine_12WeightedPupilsuser_specifiedSWWreduction'] = str(round(nine_12WeightedPupilsuser_specifiedSWWreduction[counter2], 4))
        dictionary['TotalStateFundingEqualised'] = str(round(TotalStateFundingEqualised[counter2], 4))
        #dictionary['NetworkElemADM'] = str(round(NetworkElemADM[counter2], 4))
        #dictionary['NetworkHSADM'] = str(round(NetworkHSADM[counter2], 4))
        #dictionary['PREKADM'] = str(round(PREKADM[counter2], 4))
        #dictionary['ELEMADM'] = str(round(ELEMADM[counter2], 4))
        #dictionary['HSADM'] = str(round(HSADM[counter2], 4))
        #dictionary['GroupBWeightedAddonCounts'] = str(round(GroupBWeightedAddonCounts[counter2], 3))
        #dictionary['SSWELEMINCREMENTALWEIGHTPP'] = str(round(SSWELEMINCREMENTALWEIGHTPP[counter2], 3))
        #dictionary['ElemBaseWeight'] = str(round(ElemBaseWeight[counter2], 3))
        dictionary['GroupBBSL'] = str(round(GroupBBSL[counter2], 2))
        #dictionary['HSBSL'] = str(round(HSBSL[counter2], 2))
        #dictionary['AuditBaseLevelAdjustment'] = str(round(AuditBaseLevelAdjustment[counter2], 3))
        #dictionary['ELEMRange'] = (ELEMRange[decoded[d4]['EntityID']])
        #dictionary['HSRange'] = (HSRange[decoded[d4]['EntityID']])
        #dictionary['HSSmallIsolated'] = str(round(decoded[d4]['HSSmallIsolated'], 3))
        dictionary['AdditionalAssistance']=AdditionalAssistance[counter2]
        dictionary['TotalFormulaDistrictAA'] = str(round(TotalFormulaDistrictAA[counter2], 3))
        #dictionary['ElemBSL'] = str(round(ELEMBSL[counter2], 3))
        dictionary['EHType'] = decoded[d4]['EHType']
        # print(type(d4['ESSmallIsolated']))
        #dictionary['ESSmallIsolated'] = str(round(decoded[d4]['ESSmallIsolated'], 3))
        #dictionary['TotalFormulaDistrictAA'] = str(round(TotalFormulaDistrictAA[counter2], 4))
        #dictionary['TotalNetDistrictAA'] = str(round(TotalNetDistrictAA[counter2], 4))
        #dictionary['FinalFormulaAAwithReduction'] = str(round(FinalFormulaAAwithReduction[counter2], 4))
        #dictionary['FinalFormulaAdditionalAssistance'] = str(round(FinalFormulaAdditionalAssistance[counter2], 4))
        #dictionary['ElemLL'] = str(round(ElemLL[counter2], 4))
        #dictionary['HSBaseWeight'] = str(round(HSBaseWeight[decoded[d4]['EntityID']], 4))
        #dictionary['HSLL'] = str(round(HSLL[counter2], 4))
        #dictionary['SSWHSINCREMENTALWEIGHTPP'] = str(round(SSWHSINCREMENTALWEIGHTPP[counter2], 4))
        #dictionary['color']="red"
        #dictionary['LEABaseLevel1']=str(round(LEABaseLevel1[counter2]))
        D.append(dictionary)
        counter2 += 1
        ti=time.time()
    print(ti-gi)
    return flask.render_template('table2.html', string1=D,g='green',r='red')
if __name__ == '__main__':
    app.run()
