import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.hltPhotonEcalIsol_cfi import *
import copy
from RecoEgamma.EgammaHLTProducers.hltPhotonEcalIsol_cfi import *
l1IsolatedPhotonEcalIsol = copy.deepcopy(hltPhotonEcalIsol)
l1IsolatedPhotonEcalIsol.bcBarrelProducer = cms.InputTag("hltIslandBasicClustersBarrelL1Isolated","islandBarrelBasicClusters")
l1IsolatedPhotonEcalIsol.bcEndcapProducer = cms.InputTag("hltIslandBasicClustersEndcapL1Isolated","islandEndcapBasicClusters")
l1IsolatedPhotonEcalIsol.scIslandBarrelProducer = 'correctedIslandBarrelSuperClustersL1Isolated'
l1IsolatedPhotonEcalIsol.scIslandEndcapProducer = 'correctedEndcapSuperClustersWithPreshowerL1Isolated'
l1IsolatedPhotonEcalIsol.recoEcalCandidateProducer = 'l1IsoRecoEcalCandidate'

