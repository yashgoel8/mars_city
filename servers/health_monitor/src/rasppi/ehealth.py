# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ehealth', [dirname(__file__)])
        except ImportError:
            import _ehealth
            return _ehealth
        if fp is not None:
            try:
                _mod = imp.load_module('_ehealth', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ehealth = swig_import_helper()
    del swig_import_helper
else:
    import _ehealth
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class ar_Digivalue(_object):
    """Proxy of C++ DigivalueNS class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ar_Digivalue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ar_Digivalue, name)
    __repr__ = _swig_repr
    LOW = _ehealth.ar_Digivalue_LOW
    HIGH = _ehealth.ar_Digivalue_HIGH
    RISING = _ehealth.ar_Digivalue_RISING
    FALLING = _ehealth.ar_Digivalue_FALLING
    BOTH = _ehealth.ar_Digivalue_BOTH
    def __init__(self): 
        """__init__(DigivalueNS self) -> ar_Digivalue"""
        this = _ehealth.new_ar_Digivalue()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ehealth.delete_ar_Digivalue
    __del__ = lambda self : None;
ar_Digivalue_swigregister = _ehealth.ar_Digivalue_swigregister
ar_Digivalue_swigregister(ar_Digivalue)


def ar_delay(*args):
  """ar_delay(long millis)"""
  return _ehealth.ar_delay(*args)

def ar_delayMicroseconds(*args):
  """ar_delayMicroseconds(long micros)"""
  return _ehealth.ar_delayMicroseconds(*args)

def ar_millis():
  """ar_millis() -> long"""
  return _ehealth.ar_millis()
class glucoseData(_object):
    """Proxy of C++ glucoseData class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, glucoseData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, glucoseData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["year"] = _ehealth.glucoseData_year_set
    __swig_getmethods__["year"] = _ehealth.glucoseData_year_get
    if _newclass:year = _swig_property(_ehealth.glucoseData_year_get, _ehealth.glucoseData_year_set)
    __swig_setmethods__["month"] = _ehealth.glucoseData_month_set
    __swig_getmethods__["month"] = _ehealth.glucoseData_month_get
    if _newclass:month = _swig_property(_ehealth.glucoseData_month_get, _ehealth.glucoseData_month_set)
    __swig_setmethods__["day"] = _ehealth.glucoseData_day_set
    __swig_getmethods__["day"] = _ehealth.glucoseData_day_get
    if _newclass:day = _swig_property(_ehealth.glucoseData_day_get, _ehealth.glucoseData_day_set)
    __swig_setmethods__["hour"] = _ehealth.glucoseData_hour_set
    __swig_getmethods__["hour"] = _ehealth.glucoseData_hour_get
    if _newclass:hour = _swig_property(_ehealth.glucoseData_hour_get, _ehealth.glucoseData_hour_set)
    __swig_setmethods__["minutes"] = _ehealth.glucoseData_minutes_set
    __swig_getmethods__["minutes"] = _ehealth.glucoseData_minutes_get
    if _newclass:minutes = _swig_property(_ehealth.glucoseData_minutes_get, _ehealth.glucoseData_minutes_set)
    __swig_setmethods__["glucose"] = _ehealth.glucoseData_glucose_set
    __swig_getmethods__["glucose"] = _ehealth.glucoseData_glucose_get
    if _newclass:glucose = _swig_property(_ehealth.glucoseData_glucose_get, _ehealth.glucoseData_glucose_set)
    __swig_setmethods__["meridian"] = _ehealth.glucoseData_meridian_set
    __swig_getmethods__["meridian"] = _ehealth.glucoseData_meridian_get
    if _newclass:meridian = _swig_property(_ehealth.glucoseData_meridian_get, _ehealth.glucoseData_meridian_set)
    def __init__(self): 
        """__init__(glucoseData self) -> glucoseData"""
        this = _ehealth.new_glucoseData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ehealth.delete_glucoseData
    __del__ = lambda self : None;
glucoseData_swigregister = _ehealth.glucoseData_swigregister
glucoseData_swigregister(glucoseData)

class bloodPressureData(_object):
    """Proxy of C++ bloodPressureData class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, bloodPressureData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, bloodPressureData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["year"] = _ehealth.bloodPressureData_year_set
    __swig_getmethods__["year"] = _ehealth.bloodPressureData_year_get
    if _newclass:year = _swig_property(_ehealth.bloodPressureData_year_get, _ehealth.bloodPressureData_year_set)
    __swig_setmethods__["month"] = _ehealth.bloodPressureData_month_set
    __swig_getmethods__["month"] = _ehealth.bloodPressureData_month_get
    if _newclass:month = _swig_property(_ehealth.bloodPressureData_month_get, _ehealth.bloodPressureData_month_set)
    __swig_setmethods__["day"] = _ehealth.bloodPressureData_day_set
    __swig_getmethods__["day"] = _ehealth.bloodPressureData_day_get
    if _newclass:day = _swig_property(_ehealth.bloodPressureData_day_get, _ehealth.bloodPressureData_day_set)
    __swig_setmethods__["hour"] = _ehealth.bloodPressureData_hour_set
    __swig_getmethods__["hour"] = _ehealth.bloodPressureData_hour_get
    if _newclass:hour = _swig_property(_ehealth.bloodPressureData_hour_get, _ehealth.bloodPressureData_hour_set)
    __swig_setmethods__["minutes"] = _ehealth.bloodPressureData_minutes_set
    __swig_getmethods__["minutes"] = _ehealth.bloodPressureData_minutes_get
    if _newclass:minutes = _swig_property(_ehealth.bloodPressureData_minutes_get, _ehealth.bloodPressureData_minutes_set)
    __swig_setmethods__["systolic"] = _ehealth.bloodPressureData_systolic_set
    __swig_getmethods__["systolic"] = _ehealth.bloodPressureData_systolic_get
    if _newclass:systolic = _swig_property(_ehealth.bloodPressureData_systolic_get, _ehealth.bloodPressureData_systolic_set)
    __swig_setmethods__["diastolic"] = _ehealth.bloodPressureData_diastolic_set
    __swig_getmethods__["diastolic"] = _ehealth.bloodPressureData_diastolic_get
    if _newclass:diastolic = _swig_property(_ehealth.bloodPressureData_diastolic_get, _ehealth.bloodPressureData_diastolic_set)
    __swig_setmethods__["pulse"] = _ehealth.bloodPressureData_pulse_set
    __swig_getmethods__["pulse"] = _ehealth.bloodPressureData_pulse_get
    if _newclass:pulse = _swig_property(_ehealth.bloodPressureData_pulse_get, _ehealth.bloodPressureData_pulse_set)
    def __init__(self): 
        """__init__(bloodPressureData self) -> bloodPressureData"""
        this = _ehealth.new_bloodPressureData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ehealth.delete_bloodPressureData
    __del__ = lambda self : None;
bloodPressureData_swigregister = _ehealth.bloodPressureData_swigregister
bloodPressureData_swigregister(bloodPressureData)

class eHealthClass(_object):
    """Proxy of C++ eHealthClass class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, eHealthClass, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, eHealthClass, name)
    __repr__ = _swig_repr
    def __init__(self): 
        """__init__(eHealthClass self) -> eHealthClass"""
        this = _ehealth.new_eHealthClass()
        try: self.this.append(this)
        except: self.this = this
    def initPositionSensor():
        """initPositionSensor()"""
        return _ehealth.eHealthClass_initPositionSensor()

    if _newclass:initPositionSensor = staticmethod(initPositionSensor)
    __swig_getmethods__["initPositionSensor"] = lambda x: initPositionSensor
    def readBloodPressureSensor():
        """readBloodPressureSensor()"""
        return _ehealth.eHealthClass_readBloodPressureSensor()

    if _newclass:readBloodPressureSensor = staticmethod(readBloodPressureSensor)
    __swig_getmethods__["readBloodPressureSensor"] = lambda x: readBloodPressureSensor
    def initPulsioximeter(*args):
        """initPulsioximeter(int pulsioxSkipReadings)"""
        return _ehealth.eHealthClass_initPulsioximeter(*args)

    if _newclass:initPulsioximeter = staticmethod(initPulsioximeter)
    __swig_getmethods__["initPulsioximeter"] = lambda x: initPulsioximeter
    def readPulsioximeterLoop():
        """readPulsioximeterLoop()"""
        return _ehealth.eHealthClass_readPulsioximeterLoop()

    if _newclass:readPulsioximeterLoop = staticmethod(readPulsioximeterLoop)
    __swig_getmethods__["readPulsioximeterLoop"] = lambda x: readPulsioximeterLoop
    def readPulsioximeter():
        """readPulsioximeter()"""
        return _ehealth.eHealthClass_readPulsioximeter()

    if _newclass:readPulsioximeter = staticmethod(readPulsioximeter)
    __swig_getmethods__["readPulsioximeter"] = lambda x: readPulsioximeter
    def setupPulsioximeterForNextReading():
        """setupPulsioximeterForNextReading()"""
        return _ehealth.eHealthClass_setupPulsioximeterForNextReading()

    if _newclass:setupPulsioximeterForNextReading = staticmethod(setupPulsioximeterForNextReading)
    __swig_getmethods__["setupPulsioximeterForNextReading"] = lambda x: setupPulsioximeterForNextReading
    def getTemperature():
        """getTemperature() -> float"""
        return _ehealth.eHealthClass_getTemperature()

    if _newclass:getTemperature = staticmethod(getTemperature)
    __swig_getmethods__["getTemperature"] = lambda x: getTemperature
    def getOxygenSaturation():
        """getOxygenSaturation() -> int"""
        return _ehealth.eHealthClass_getOxygenSaturation()

    if _newclass:getOxygenSaturation = staticmethod(getOxygenSaturation)
    __swig_getmethods__["getOxygenSaturation"] = lambda x: getOxygenSaturation
    def getBPM():
        """getBPM() -> int"""
        return _ehealth.eHealthClass_getBPM()

    if _newclass:getBPM = staticmethod(getBPM)
    __swig_getmethods__["getBPM"] = lambda x: getBPM
    def getSkinConductance():
        """getSkinConductance() -> float"""
        return _ehealth.eHealthClass_getSkinConductance()

    if _newclass:getSkinConductance = staticmethod(getSkinConductance)
    __swig_getmethods__["getSkinConductance"] = lambda x: getSkinConductance
    def getSkinResistance():
        """getSkinResistance() -> float"""
        return _ehealth.eHealthClass_getSkinResistance()

    if _newclass:getSkinResistance = staticmethod(getSkinResistance)
    __swig_getmethods__["getSkinResistance"] = lambda x: getSkinResistance
    def getSkinConductanceVoltage():
        """getSkinConductanceVoltage() -> float"""
        return _ehealth.eHealthClass_getSkinConductanceVoltage()

    if _newclass:getSkinConductanceVoltage = staticmethod(getSkinConductanceVoltage)
    __swig_getmethods__["getSkinConductanceVoltage"] = lambda x: getSkinConductanceVoltage
    def getECG():
        """getECG() -> float"""
        return _ehealth.eHealthClass_getECG()

    if _newclass:getECG = staticmethod(getECG)
    __swig_getmethods__["getECG"] = lambda x: getECG
    def getEMG():
        """getEMG() -> int"""
        return _ehealth.eHealthClass_getEMG()

    if _newclass:getEMG = staticmethod(getEMG)
    __swig_getmethods__["getEMG"] = lambda x: getEMG
    def getBodyPosition():
        """getBodyPosition() -> uint8_t"""
        return _ehealth.eHealthClass_getBodyPosition()

    if _newclass:getBodyPosition = staticmethod(getBodyPosition)
    __swig_getmethods__["getBodyPosition"] = lambda x: getBodyPosition
    def getBodyAcceleration():
        """getBodyAcceleration() -> float *"""
        return _ehealth.eHealthClass_getBodyAcceleration()

    if _newclass:getBodyAcceleration = staticmethod(getBodyAcceleration)
    __swig_getmethods__["getBodyAcceleration"] = lambda x: getBodyAcceleration
    def getSystolicPressure(*args):
        """getSystolicPressure(int i) -> int"""
        return _ehealth.eHealthClass_getSystolicPressure(*args)

    if _newclass:getSystolicPressure = staticmethod(getSystolicPressure)
    __swig_getmethods__["getSystolicPressure"] = lambda x: getSystolicPressure
    def getDiastolicPressure(*args):
        """getDiastolicPressure(int i) -> int"""
        return _ehealth.eHealthClass_getDiastolicPressure(*args)

    if _newclass:getDiastolicPressure = staticmethod(getDiastolicPressure)
    __swig_getmethods__["getDiastolicPressure"] = lambda x: getDiastolicPressure
    def getAirFlow():
        """getAirFlow() -> int"""
        return _ehealth.eHealthClass_getAirFlow()

    if _newclass:getAirFlow = staticmethod(getAirFlow)
    __swig_getmethods__["getAirFlow"] = lambda x: getAirFlow
    def printPosition(*args):
        """printPosition(uint8_t position)"""
        return _ehealth.eHealthClass_printPosition(*args)

    if _newclass:printPosition = staticmethod(printPosition)
    __swig_getmethods__["printPosition"] = lambda x: printPosition
    def airFlowWave(*args):
        """airFlowWave(int air)"""
        return _ehealth.eHealthClass_airFlowWave(*args)

    if _newclass:airFlowWave = staticmethod(airFlowWave)
    __swig_getmethods__["airFlowWave"] = lambda x: airFlowWave
    def readGlucometer():
        """readGlucometer()"""
        return _ehealth.eHealthClass_readGlucometer()

    if _newclass:readGlucometer = staticmethod(readGlucometer)
    __swig_getmethods__["readGlucometer"] = lambda x: readGlucometer
    def getGlucometerLength():
        """getGlucometerLength() -> int"""
        return _ehealth.eHealthClass_getGlucometerLength()

    if _newclass:getGlucometerLength = staticmethod(getGlucometerLength)
    __swig_getmethods__["getGlucometerLength"] = lambda x: getGlucometerLength
    def getBloodPressureLength():
        """getBloodPressureLength() -> int"""
        return _ehealth.eHealthClass_getBloodPressureLength()

    if _newclass:getBloodPressureLength = staticmethod(getBloodPressureLength)
    __swig_getmethods__["getBloodPressureLength"] = lambda x: getBloodPressureLength
    def version():
        """version() -> int"""
        return _ehealth.eHealthClass_version()

    if _newclass:version = staticmethod(version)
    __swig_getmethods__["version"] = lambda x: version
    def numberToMonth(*args):
        """numberToMonth(int month) -> char const *"""
        return _ehealth.eHealthClass_numberToMonth(*args)

    if _newclass:numberToMonth = staticmethod(numberToMonth)
    __swig_getmethods__["numberToMonth"] = lambda x: numberToMonth
    __swig_setmethods__["glucoseDataVector"] = _ehealth.eHealthClass_glucoseDataVector_set
    __swig_getmethods__["glucoseDataVector"] = _ehealth.eHealthClass_glucoseDataVector_get
    if _newclass:glucoseDataVector = _swig_property(_ehealth.eHealthClass_glucoseDataVector_get, _ehealth.eHealthClass_glucoseDataVector_set)
    __swig_setmethods__["bloodPressureDataVector"] = _ehealth.eHealthClass_bloodPressureDataVector_set
    __swig_getmethods__["bloodPressureDataVector"] = _ehealth.eHealthClass_bloodPressureDataVector_get
    if _newclass:bloodPressureDataVector = _swig_property(_ehealth.eHealthClass_bloodPressureDataVector_get, _ehealth.eHealthClass_bloodPressureDataVector_set)
    __swig_destroy__ = _ehealth.delete_eHealthClass
    __del__ = lambda self : None;
eHealthClass_swigregister = _ehealth.eHealthClass_swigregister
eHealthClass_swigregister(eHealthClass)

def eHealthClass_initPositionSensor():
  """eHealthClass_initPositionSensor()"""
  return _ehealth.eHealthClass_initPositionSensor()

def eHealthClass_readBloodPressureSensor():
  """eHealthClass_readBloodPressureSensor()"""
  return _ehealth.eHealthClass_readBloodPressureSensor()

def eHealthClass_initPulsioximeter(*args):
  """eHealthClass_initPulsioximeter(int pulsioxSkipReadings)"""
  return _ehealth.eHealthClass_initPulsioximeter(*args)

def eHealthClass_readPulsioximeterLoop():
  """eHealthClass_readPulsioximeterLoop()"""
  return _ehealth.eHealthClass_readPulsioximeterLoop()

def eHealthClass_readPulsioximeter():
  """eHealthClass_readPulsioximeter()"""
  return _ehealth.eHealthClass_readPulsioximeter()

def eHealthClass_setupPulsioximeterForNextReading():
  """eHealthClass_setupPulsioximeterForNextReading()"""
  return _ehealth.eHealthClass_setupPulsioximeterForNextReading()

def eHealthClass_getTemperature():
  """eHealthClass_getTemperature() -> float"""
  return _ehealth.eHealthClass_getTemperature()

def eHealthClass_getOxygenSaturation():
  """eHealthClass_getOxygenSaturation() -> int"""
  return _ehealth.eHealthClass_getOxygenSaturation()

def eHealthClass_getBPM():
  """eHealthClass_getBPM() -> int"""
  return _ehealth.eHealthClass_getBPM()

def eHealthClass_getSkinConductance():
  """eHealthClass_getSkinConductance() -> float"""
  return _ehealth.eHealthClass_getSkinConductance()

def eHealthClass_getSkinResistance():
  """eHealthClass_getSkinResistance() -> float"""
  return _ehealth.eHealthClass_getSkinResistance()

def eHealthClass_getSkinConductanceVoltage():
  """eHealthClass_getSkinConductanceVoltage() -> float"""
  return _ehealth.eHealthClass_getSkinConductanceVoltage()

def eHealthClass_getECG():
  """eHealthClass_getECG() -> float"""
  return _ehealth.eHealthClass_getECG()

def eHealthClass_getEMG():
  """eHealthClass_getEMG() -> int"""
  return _ehealth.eHealthClass_getEMG()

def eHealthClass_getBodyPosition():
  """eHealthClass_getBodyPosition() -> uint8_t"""
  return _ehealth.eHealthClass_getBodyPosition()

def eHealthClass_getBodyAcceleration():
  """eHealthClass_getBodyAcceleration() -> float *"""
  return _ehealth.eHealthClass_getBodyAcceleration()

def eHealthClass_getSystolicPressure(*args):
  """eHealthClass_getSystolicPressure(int i) -> int"""
  return _ehealth.eHealthClass_getSystolicPressure(*args)

def eHealthClass_getDiastolicPressure(*args):
  """eHealthClass_getDiastolicPressure(int i) -> int"""
  return _ehealth.eHealthClass_getDiastolicPressure(*args)

def eHealthClass_getAirFlow():
  """eHealthClass_getAirFlow() -> int"""
  return _ehealth.eHealthClass_getAirFlow()

def eHealthClass_printPosition(*args):
  """eHealthClass_printPosition(uint8_t position)"""
  return _ehealth.eHealthClass_printPosition(*args)

def eHealthClass_airFlowWave(*args):
  """eHealthClass_airFlowWave(int air)"""
  return _ehealth.eHealthClass_airFlowWave(*args)

def eHealthClass_readGlucometer():
  """eHealthClass_readGlucometer()"""
  return _ehealth.eHealthClass_readGlucometer()

def eHealthClass_getGlucometerLength():
  """eHealthClass_getGlucometerLength() -> int"""
  return _ehealth.eHealthClass_getGlucometerLength()

def eHealthClass_getBloodPressureLength():
  """eHealthClass_getBloodPressureLength() -> int"""
  return _ehealth.eHealthClass_getBloodPressureLength()

def eHealthClass_version():
  """eHealthClass_version() -> int"""
  return _ehealth.eHealthClass_version()

def eHealthClass_numberToMonth(*args):
  """eHealthClass_numberToMonth(int month) -> char const *"""
  return _ehealth.eHealthClass_numberToMonth(*args)
cvar = _ehealth.cvar

class floatArray(_object):
    """Proxy of C++ floatArray class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, floatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, floatArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(floatArray self, size_t nelements) -> floatArray"""
        this = _ehealth.new_floatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ehealth.delete_floatArray
    __del__ = lambda self : None;
    def __getitem__(self, *args):
        """__getitem__(floatArray self, size_t index) -> float"""
        return _ehealth.floatArray___getitem__(self, *args)

    def __setitem__(self, *args):
        """__setitem__(floatArray self, size_t index, float value)"""
        return _ehealth.floatArray___setitem__(self, *args)

    def cast(self):
        """cast(floatArray self) -> float *"""
        return _ehealth.floatArray_cast(self)

    def frompointer(*args):
        """frompointer(float * t) -> floatArray"""
        return _ehealth.floatArray_frompointer(*args)

    if _newclass:frompointer = staticmethod(frompointer)
    __swig_getmethods__["frompointer"] = lambda x: frompointer
floatArray_swigregister = _ehealth.floatArray_swigregister
floatArray_swigregister(floatArray)

def floatArray_frompointer(*args):
  """floatArray_frompointer(float * t) -> floatArray"""
  return _ehealth.floatArray_frompointer(*args)

# This file is compatible with both classic and new-style classes.


