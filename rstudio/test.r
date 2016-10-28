require(graphics)
dotchart(precip[order(precip)], main = "precip data")
title(sub = "Average annual precipitation (in.)")
mean(precip)
which.max(precip)
which.min(precip)
precip['Phoenix']
precip['Albany']
state.abb
