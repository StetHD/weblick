# The MIT License (MIT)
#
# Copyright (c) 2015 Leon Jacobs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from lib.Models.Base import db
from lib.Models.Url import Url
from lib.Models.Header import Header
from lib.Models.Cookie import Cookie
from lib.Models.History import History
from lib.Models.HistoryHeader import HistoryHeader
from lib.Models.Comment import Comment
from lib.Models.Certificate import Certificate

import logging
logger = logging.getLogger(__name__)

class DB():

    @staticmethod
    def setup():

        '''
            Setup Database Tables

            The primary purpose of this method is to prepare the tables
            needed in the database.
        '''

        # create the tables if they do not exist
        with db.execution_context() as ctx:

            logger.debug('Connected to database: %s' % db.database)
            db.create_tables(
                [
                    Url, Header, Cookie, History, HistoryHeader, Comment, Certificate
                ], True
            )
            logger.debug('Tables synced')

        return
