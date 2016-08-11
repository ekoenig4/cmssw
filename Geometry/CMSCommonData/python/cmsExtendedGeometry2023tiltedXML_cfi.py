import FWCore.ParameterSet.Config as cms

## 2015 + new phase 1 pixel detector

XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/PhaseII/materials.xml',
        'Geometry/CMSCommonData/data/rotations.xml',
        'Geometry/CMSCommonData/data/extend/cmsextent.xml',
        'Geometry/CMSCommonData/data/PhaseI/cms.xml',
        'Geometry/CMSCommonData/data/eta3/etaMax.xml',        
        'Geometry/CMSCommonData/data/cmsMother.xml',
        'Geometry/CMSCommonData/data/cmsTracker.xml',
        'Geometry/CMSCommonData/data/PhaseII/caloBase.xml',
        'Geometry/CMSCommonData/data/cmsCalo.xml',
        'Geometry/CMSCommonData/data/PhaseII/muonBase.xml',
        'Geometry/CMSCommonData/data/cmsMuon.xml',
        'Geometry/CMSCommonData/data/mgnt.xml',
        'Geometry/CMSCommonData/data/PhaseII/beampipe.xml',
        'Geometry/CMSCommonData/data/cmsBeam.xml',
        'Geometry/CMSCommonData/data/muonMB.xml',
        'Geometry/CMSCommonData/data/muonMagnet.xml',
        'Geometry/CMSCommonData/data/cavern.xml',
        'Geometry/TrackerCommonData/data/PhaseII/trackerParameters.xml',
        'Geometry/TrackerCommonData/data/pixfwdCommon.xml',
	'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdMaterials.xml',
	'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdCylinder.xml', 
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwd.xml', 
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdDisks.xml', 
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdInnerDisk7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk8.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk9.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdOuterDisk10.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade1.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade2.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade3.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade4.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade5.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade6.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade7.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade8.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade9.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixfwdblade10.xml',
        'Geometry/TrackerCommonData/data/PhaseI/pixbarmaterial.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladder.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull0.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull1.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull2.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarladderfull3.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer0.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer1.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer2.xml', 
        'Geometry/TrackerCommonData/data/PhaseI/pixbarlayer3.xml', 
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/pixbar.xml', 
        'Geometry/TrackerCommonData/data/trackermaterial.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/tracker.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerbar.xml',
        'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerfwd.xml',
	'Geometry/TrackerCommonData/data/PhaseII/TiltedTracker/trackerStructureTopology.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker/trackersens.xml',
        'Geometry/TrackerRecoData/data/PhaseII/TiltedTracker/trackerRecoMaterial.xml',
        'Geometry/TrackerSimData/data/PhaseII/TiltedTracker/trackerProdCuts.xml',
        'Geometry/TrackerSimData/data/trackerProdCutsBEAM.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eregalgo.xml',
        'Geometry/EcalCommonData/data/ebalgo.xml',
        'Geometry/EcalCommonData/data/ebcon.xml',
        'Geometry/EcalCommonData/data/ebrot.xml',
        'Geometry/EcalCommonData/data/eecon.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eefixed.xml',
        'Geometry/EcalCommonData/data/PhaseII/ShortEE/eehier.xml',
        'Geometry/EcalCommonData/data/eealgo.xml',
        'Geometry/EcalCommonData/data/escon.xml',
        'Geometry/EcalCommonData/data/esalgo.xml',
        'Geometry/EcalCommonData/data/eeF.xml',
        'Geometry/EcalCommonData/data/eeB.xml',
        'Geometry/EcalCommonData/data/ectkcable.xml',
        'Geometry/HcalCommonData/data/hcalrotations.xml',
        'Geometry/HcalCommonData/data/PhaseII/hcalalgo.xml',
        'Geometry/HcalCommonData/data/hcalcablealgo.xml',
        'Geometry/HcalCommonData/data/hcalbarrelalgo.xml',
        'Geometry/HcalCommonData/data/PhaseII/hcalendcapalgo.xml',
        'Geometry/HcalCommonData/data/hcalouteralgo.xml',
        'Geometry/HcalCommonData/data/hcalforwardalgo.xml',
        'Geometry/HcalCommonData/data/Run2/hcalSimNumbering16a.xml',
        'Geometry/HcalCommonData/data/Run2/hcalRecNumbering16a.xml',
        'Geometry/HcalCommonData/data/average/hcalforwardmaterial.xml',
        'Geometry/MuonCommonData/data/v1/mbCommon.xml',
        'Geometry/MuonCommonData/data/v1/mb1.xml',
        'Geometry/MuonCommonData/data/v1/mb2.xml',
        'Geometry/MuonCommonData/data/v1/mb3.xml',
        'Geometry/MuonCommonData/data/v1/mb4.xml',
        'Geometry/MuonCommonData/data/design/muonYoke.xml',
        'Geometry/MuonCommonData/data/PhaseII/mf.xml',
        'Geometry/MuonCommonData/data/PhaseII/rpcf.xml',
        'Geometry/MuonCommonData/data/PhaseII/gemf.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem11.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/gem21.xml',
        'Geometry/MuonCommonData/data/v2/csc.xml',
        'Geometry/MuonCommonData/data/PhaseII/mfshield.xml',
        'Geometry/MuonCommonData/data/PhaseII/TDR_BaseLine/me0.xml',
        'Geometry/ForwardCommonData/data/forward.xml',
        'Geometry/ForwardCommonData/data/v2/forwardshield.xml',
        'Geometry/ForwardCommonData/data/brmrotations.xml',
        'Geometry/ForwardCommonData/data/brm.xml',
        'Geometry/ForwardCommonData/data/totemMaterials.xml',
        'Geometry/ForwardCommonData/data/totemRotations.xml',
        'Geometry/ForwardCommonData/data/totemt1.xml',
        'Geometry/ForwardCommonData/data/totemt2.xml',
        'Geometry/ForwardCommonData/data/ionpump.xml',
        'Geometry/ForwardCommonData/data/castor.xml',
        'Geometry/ForwardCommonData/data/zdcmaterials.xml',
        'Geometry/ForwardCommonData/data/lumimaterials.xml',
        'Geometry/ForwardCommonData/data/zdcrotations.xml',
        'Geometry/ForwardCommonData/data/lumirotations.xml',
        'Geometry/ForwardCommonData/data/zdc.xml',
        'Geometry/ForwardCommonData/data/zdclumi.xml',
        'Geometry/ForwardCommonData/data/cmszdc.xml')+cms.vstring(
        'Geometry/MuonCommonData/data/PhaseII/muonNumbering.xml',
        'Geometry/EcalSimData/data/ecalsens.xml',
        'Geometry/HcalCommonData/data/Phase0/hcalsenspmf.xml',
        'Geometry/HcalSimData/data/hf.xml',
        'Geometry/HcalSimData/data/hfpmt.xml',
        'Geometry/HcalSimData/data/hffibrebundle.xml',
        'Geometry/HcalSimData/data/CaloUtil.xml',
        'Geometry/MuonSimData/data/PhaseII/muonSens.xml',
        'Geometry/DTGeometryBuilder/data/dtSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecsFilter.xml',
        'Geometry/CSCGeometryBuilder/data/cscSpecs.xml',
        'Geometry/RPCGeometryBuilder/data/PhaseII/RPCSpecs.xml',
        'Geometry/GEMGeometryBuilder/data/GEMSpecsFilter.xml',
        'Geometry/GEMGeometryBuilder/data/v5/GEMSpecs.xml',
        'Geometry/ForwardCommonData/data/brmsens.xml',
        'Geometry/ForwardSimData/data/castorsens.xml',
        'Geometry/ForwardSimData/data/zdcsens.xml',
        'Geometry/HcalSimData/data/HcalProdCuts.xml',
        'Geometry/EcalSimData/data/EcalProdCuts.xml',
        'Geometry/EcalSimData/data/ESProdCuts.xml',
        'Geometry/MuonSimData/data/PhaseII/muonProdCuts.xml',
        'Geometry/ForwardSimData/data/CastorProdCuts.xml',
        'Geometry/ForwardSimData/data/zdcProdCuts.xml',
        'Geometry/ForwardSimData/data/ForwardShieldProdCuts.xml',
        'Geometry/CMSCommonData/data/FieldParameters.xml'),
    rootNodeName = cms.string('cms:OCMS')
)

