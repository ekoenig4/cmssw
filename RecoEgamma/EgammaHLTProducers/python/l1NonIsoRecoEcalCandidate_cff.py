import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaHLTProducers.hltRecoEcalCandidate_cfi import *
import copy
from RecoEgamma.EgammaHLTProducers.hltRecoEcalCandidate_cfi import *
l1NonIsoRecoEcalCandidate = copy.deepcopy(hltRecoEcalCandidate)
l1NonIsoRecoEcalCandidate.scHybridBarrelProducer = 'correctedHybridSuperClustersL1NonIsolated'
l1NonIsoRecoEcalCandidate.scIslandEndcapProducer = 'correctedEndcapSuperClustersWithPreshowerL1NonIsolated'

