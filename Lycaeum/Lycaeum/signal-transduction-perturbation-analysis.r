#!/usr/bin/env Rscript

library(CellNOptR)
library(igraph)

data("ToyModel", package="CellNOptR")
data("CNOlistToy", package="CellNOptR")
pknmodel = ToyModel
cnolist = CNOlist(CNOlistToy)

png("./prior-knowledge-network.png")
plotModel(model = pknmodel, CNOlist = cnolist)


model = preprocessing(cnolist, pknmodel)
res = gaBinaryT1(cnolist, model, verbose=FALSE)

png('./component-activities.png')
cutAndPlot(cnolist, model, list(res$bString))

png('./prior-knowledge-network-updated.png')
plotModel(model, cnolist, res$bString)
dev.off()