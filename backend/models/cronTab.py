#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db
from utils.mango import *


# 类名定义 collection
#
class CronTab(Model):

    class Meta:
        database = db
        collection = 'apscheduler.cronTab'


    # 字段
    _id = StringField()
    projectId = ObjectIdField()
    name = StringField()
    description = StringField()
    isDeleted = BooleanField(field_name='isDeleted', default=False)
    isExecuteForbiddenedCase = BooleanField(field_name='isExecuteForbiddenedCase', default=False)
    testCaseSuiteIdList = ArrayField()
    testCaseIdList = ArrayField()
    testDomain = StringField()
    next_run_time = FloatField()
    triggerType = StringField()
    interval = FloatField()
    runDate = DateField()
    alarmMailList = ArrayField()
    status = StringField(field_name='status', default='CREATED')
    createAt = DateField()
    creatorNickName = StringField()
    lastUpdateTime = DateField()
    lastUpdatorNickName = StringField()

    def __str__(self):
        return "_id:{}"\
            .format(self._id)


if __name__ == '__main__':
    pass
