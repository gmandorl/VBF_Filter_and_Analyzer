import FWCore.ParameterSet.Config as cms

processName = "JetStudy"
process = cms.Process(processName)


process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_LO_MiniAOD.root"))
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_NLO_MiniAOD.root"))
    #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/DY_M-50_NLO_MiniAOD_2.root"))  # NLO
    fileNames = cms.untracked.vstring("/store/mc/RunIISummer15GS/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/GEN-SIM/MCRUN2_71_V1_ext1-v1/20008/1E146496-C6C5-E511-A00F-02163E0167D0.root"))
     #fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/g/gimandor/private/Hmumu/DY_check_MiniAOD/1E146496-C6C5-E511-A00F-02163E0167D0.root"))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))  



process.MyModule = cms.EDAnalyzer('GenJetAnalyzer',
)

process.MyFilter = cms.EDFilter('VBFGenJetFilter',
)

#process.out = cms.OutputModule("PoolOutputModule",
    #fileName = cms.untracked.string("test.root"),
    #closeFileFast = cms.untracked.bool(True)
#)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string('test.root') )

#process.path = cms.Path(process.MyModule)
process.path = cms.Path(process.MyFilter*process.MyModule)
