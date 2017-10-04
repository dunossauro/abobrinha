# -*- coding: utf-8 -*-
from radish import after


@after.each_feature
def after_feature(feature):
    pass
