#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
################################################################################
#
#    Copyright 2017 @pctripsesp (www.pctripsesp.com, info@pctripsesp.com)
#
#    You can redistribute this script it and/or modify it under
#    the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation.
#
#    This is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    See <http://www.gnu.org/licenses/>.
#
################################################################################


__author__ = "pctripsesp "


############################################################################################################################
# This script checks balance of random generated Ethereum wallets. If balance is positive returns the wallet's private key #
############################################################################################################################


#You first need to install geth. You can check how at https://github.com/ethereum/go-ethereum/wiki/Building-Ethereum
from subprocess import Popen, PIPE
import time

syncronized_flag = False


#This starts syncing with ethereum net
print ("Starting... please wait while checking database")
with Popen(["geth", "--light"], stderr=PIPE, bufsize=1, universal_newlines=True) as p1_sync:
    for line in p1_sync.stderr:
        if "Block synchronisation started" in line:
            print(line, end='')

            #Once the block is sync, checks if its updated. If check before being sync you will get a fake "false" status when execute "eth.syncing"
            while not syncronized_flag:
                with Popen(["geth", "--exec", "eth.syncing"], stdout=PIPE, bufsize=1, universal_newlines=True) as p2_check_block:
                    for line in p2_check_block.stdout:

                        if "false" in line:
                            print("SYNCHRONIZED")
                            syncronized_flag = True

                        else:
                            #Show % synchronized
                            percent_array = []  # [highestBlock-startingBlock, currentBlock-startingBlock]
                            with Popen(["geth", "--exec", "eth.syncing.highestBlock-eth.syncing.currentBlock"], stdout=PIPE, bufsize=1, universal_newlines=True) as p3_percent:
                                for line in p3_percent.stdout:

                                    print ("SYNCHRONIZED")
                                    time.sleep(10)
