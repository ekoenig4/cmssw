import FWCore.ParameterSet.Config as cms

RCTConfigProducers = cms.ESProducer("RCTConfigProducers",
    eGammaHCalScaleFactors = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
    eMaxForFGCut = cms.double(-999.0),
    noiseVetoHB = cms.bool(False),
    eMaxForHoECut = cms.double(-999.0),
    hOeCut = cms.double(999.0),
    eGammaECalScaleFactors = cms.vdouble(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
    eMinForHoECut = cms.double(999.0),
    hActivityCut = cms.double(999.0),
    eActivityCut = cms.double(999.0),
    jetMETHCalScaleFactors = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    noiseVetoHEplus = cms.bool(False),
    eicIsolationThreshold = cms.double(7.0),
    jetMETLSB = cms.double(1.0),
    jetMETECalScaleFactors = cms.vdouble(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    eGammaLSB = cms.double(1.0),
    eMinForFGCut = cms.double(999.0),
    hMinForHoECut = cms.double(999.0),
    noiseVetoHEminus = cms.bool(False)
)


