import FWCore.ParameterSet.Config as cms

l1GtAnalyz = cms.EDAnalyzer("L1GtAnalyzer",
    ConditionName = cms.string('DoubleTauJet50_2'),
    # input tag for GT readout collection: 
    #     GT emulator:  gtDigis  
    #     GT unpacker:  l1GtUnpack  
    DaqGtInputTag = cms.InputTag("gtDigis"),
    # input tag for GMT readout collection: 
    #     gmtDigis = GMT emulator
    #     l1GtUnpack     = GT unpacker (common GT/GMT unpacker)
    GmtInputTag = cms.InputTag("gmtDigis"),
    # input tag for GT object map collection
    #     only the L1 GT emulator produces it,
    #     no map collection is produced by hardware
    #
    #     GT emulator:  gtDigis  
    GtObjectMapTag = cms.InputTag("gtDigis"),
    # an algorithm and a condition in that algorithm to test the object maps
    AlgorithmName = cms.string('L1_DoubleJet50_ETM20')
)


