# Comparative Analysis: go-ethereum vs. quorum

An analysis of the differences between the project directories for go-ethereum and quorum. 

## Jaccard Similarity

To get a rough sense of the similarity between these two projects we use the Jaccard Similarity. 
It varies between 0 (when sets are completely different) and 1 (when sets are identical). 

We had to determine how to deal with "IN BOTH, BUT DIFFERENT", described in detail below. For simplicity we consider records in this class as being only in the intersection or only in the difference of the Quorum and Go-Ethereum sets, based on percentage of lines that differ. For "IN BOTH, BUT DIFFERENT" we have initially 490 files. Our line-by-line difference ratio gives us a number between 0 and 1, files with a similarity score of greater than 90% are treated as part of the "IDENTICAL FILES" set, there are 418 of such files, and we give them a weight of 0.9, i.e. (418 * 0.9), we add the result to our "IDENTICAL FILES" set, therefore "IDENTICAL FILES" is recalculated as 1710 + (418 * 0.9) = 2086.2

We're left with 72 files with a difference of greater than 0.10%. These are split evenly and partitioned between the "GO-ETHEREUM ONLY", and "QUORUM ONLY", with a weight of 0.10

So we have:


QUORUM ONLY: 95 + (36 * 0.1) = 98.6


GO-ETHEREUM ONLY: 124 + (36 * 0.1) = 127.6


INTERSECTION: 1710 + (418 * 0.9) = 2086.2


And therefore Jaccard similarity will be:

J = 2086.2 / (2086.2 + 98.6 + 127.6) = 0.90217

## How to interpret this document: 

### Files fall into one of four categories: 

* GO-ETHEREUM ONLY: files found exclusively within the go-ethereum directory, and it's sub-directories

* QUORUM ONLY: files found exclusively within the quorum directory, and it's sub-directories

* IDENTICAL FILES: files that are exactly the same in both projects

* IN BOTH, BUT DIFFERENT: files are found in both projects, but are *not* exactly the same, 
   for these files we provide an addendum entitled 'RELATIVE DIFFERENCE', which describes
   the degree to which the files are divergent between the two projects

### The following JSON-esque tree describes the directory structure of each project:

      {
         [ all of the files, by name, that fall into this respective category ]

         *from inside the root directory*

         "sub-directory name": {

            "files inside this sub-directory that correspond to the category"

            "additional sub-directories within this directory": {

               "files"

               "additional sub-directories (recursively defined)"
            }
         }

      }


------

GO-ETHEREUM ONLY: 124



      {

         [miner, ethstats, Dockerfile, .dockerignore, mobile, les, mailserver, keystore, usbwallet, errors.go, hd.go, hd_test.go, url.go, manager.go, accounts.go, type_test.go, example_scope_test.go, subscription.go, feed.go, example_feed_test.go, subscription_test.go, feed_test.go, example_subscription_test.go, FETCH_HEAD, release, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.idx, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.pack, release, server_test.go, guide, deps, azure.go, pgp.go, bootnodes.go, config.go, version.go, nsis.pathupdate.nsh, nsis.envvarupdate.nsh, nsis.simplefc.source.zip, mvn.pom, nsis.geth.nsi, nsis.uninstall.nsh, nsis.simplefc.dll, pod.podspec, mvn.settings, nsis.install.nsh, evm.go, dao_test.go, memory_table.go, gas_table.go, interface.go, noop.go, stack_table.go, transaction_signing.go, log_test.go, transaction_signing_test.go, log.go, ansible, EIP158, README.md, stChangedTests.json, README.md, README.md, EIP155, ttTransactionTestEip155VitaliksTests.json, EIP150, README.md, README.md, README.md, aristanetworks, maruel, Azure, karalabe, config.py, table.go, flag-types.json, flag_generated.go, generate-flag-types, .travis.yml, syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s, cast5, openpgp, netutil, discv5, vm_env.go, txpool_test.go, lightchain.go, odr_test.go, txpool.go, lightchain_test.go, odr_util.go, swarm, wnode, misccmd.go, dao_test.go, ext.h, sage, build-aux, contrib, scalar_low.h, asm, scalar_low_impl.h, tests_exhaustive.c, org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java, hexutil, mclock, exp.go, sync_test.go, gasprice]

         trie: {
            
         }
         whisper: {
            [mailserver]
            whisperv5: {
               
            }
            whisperv2: {
               
            }
            shhapi: {
               
            }
         }
         rpc: {
            
         }
         accounts: {
            [keystore, usbwallet, errors.go, hd.go, hd_test.go, url.go, manager.go, accounts.go, type_test.go]
            abi: {
               [type_test.go]
               bind: {
                  
                  backends: {
                     
                  }
               }
            }
         }
         errs: {
            
         }
         event: {
            [example_scope_test.go, subscription.go, feed.go, example_feed_test.go, subscription_test.go, feed_test.go, example_subscription_test.go]
            filter: {
               
            }
         }
         console: {
            
            testdata: {
               
            }
         }
         compression: {
            
            rle: {
               
            }
         }
         .github: {
            
         }
         rlp: {
            
         }
         swarm: {
            [server_test.go]
            services: {
               
               swap: {
                  
                  swap: {
                     
                  }
               }
            }
            api: {
               [server_test.go]
               http: {
                  [server_test.go]
               }
               testdata: {
                  
                  test0: {
                     
                     img: {
                        
                     }
                  }
               }
            }
            storage: {
               
            }
            network: {
               
               kademlia: {
                  
               }
            }
         }
         internal: {
            [guide, deps, azure.go, pgp.go]
            debug: {
               
            }
            web3ext: {
               
            }
            ethapi: {
               
            }
            jsre: {
               [deps]
            }
            build: {
               [azure.go, pgp.go]
            }
         }
         params: {
            [bootnodes.go, config.go, version.go]
         }
         build: {
            [nsis.pathupdate.nsh, nsis.envvarupdate.nsh, nsis.simplefc.source.zip, mvn.pom, nsis.geth.nsi, nsis.uninstall.nsh, nsis.simplefc.dll, pod.podspec, mvn.settings, nsis.install.nsh]
            _vendor: {
               
               src: {
                  
                  golang.org: {
                     
                     x: {
                        
                        net: {
                           
                           context: {
                              
                           }
                        }
                     }
                  }
               }
            }
         }
         pow: {
            
         }
         logger: {
            
            glog: {
               
            }
         }
         containers: {
            
            docker: {
               
               master-alpine: {
                  
               }
               develop-alpine: {
                  
               }
               develop-ubuntu: {
                  
               }
               master-ubuntu: {
                  
               }
            }
            vagrant: {
               
            }
         }
         node: {
            
         }
         core: {
            [evm.go, dao_test.go, memory_table.go, gas_table.go, interface.go, noop.go, stack_table.go, transaction_signing.go, log_test.go, transaction_signing_test.go, log.go]
            state: {
               
            }
            vm: {
               [memory_table.go, gas_table.go, interface.go, noop.go, stack_table.go]
               runtime: {
                  
               }
            }
            types: {
               [transaction_signing.go, log_test.go, transaction_signing_test.go, log.go]
            }
         }
         tests: {
            [ansible, EIP158, README.md, stChangedTests.json, README.md, README.md, EIP155, ttTransactionTestEip155VitaliksTests.json, EIP150, README.md, README.md, README.md]
            files: {
               [ansible, EIP158, README.md, stChangedTests.json, README.md, README.md, EIP155, ttTransactionTestEip155VitaliksTests.json, EIP150, README.md, README.md, README.md]
               VMTests: {
                  
                  RandomTests: {
                     
                  }
               }
               TrieTests: {
                  
               }
               StateTests: {
                  [EIP158, README.md, stChangedTests.json, README.md, README.md]
                  RandomTests: {
                     
                  }
                  EIP150: {
                     [stChangedTests.json, README.md]
                     Homestead: {
                        
                     }
                  }
                  Homestead: {
                     [README.md]
                  }
               }
               ABITests: {
                  
               }
               PoWTests: {
                  
               }
               RLPTests: {
                  
                  RandomRLPTests: {
                     
                  }
               }
               KeyStoreTests: {
                  
               }
               BasicTests: {
                  
               }
               GenesisTests: {
                  
               }
               TransactionTests: {
                  [EIP155, ttTransactionTestEip155VitaliksTests.json]
                  RandomTests: {
                     
                  }
                  Homestead: {
                     [ttTransactionTestEip155VitaliksTests.json]
                  }
               }
               BlockchainTests: {
                  [EIP150, README.md, README.md, README.md]
                  RandomTests: {
                     
                  }
                  TestNetwork: {
                     [README.md]
                  }
                  Homestead: {
                     [README.md]
                  }
               }
            }
         }
         vendor: {
            [aristanetworks, maruel, Azure, karalabe, config.py, table.go, flag-types.json, flag_generated.go, generate-flag-types, .travis.yml, syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s, cast5, openpgp]
            github.com: {
               [aristanetworks, maruel, Azure, karalabe, config.py, table.go]
               huin: {
                  
                  goupnp: {
                     
                     dcps: {
                        
                        internetgateway1: {
                           
                        }
                        internetgateway2: {
                           
                        }
                     }
                     httpu: {
                        
                     }
                     ssdp: {
                        
                     }
                     scpd: {
                        
                     }
                     soap: {
                        
                     }
                  }
               }
               robertkrimen: {
                  
                  otto: {
                     
                     ast: {
                        
                     }
                     parser: {
                        
                     }
                     dbg: {
                        
                     }
                     token: {
                        
                     }
                     registry: {
                        
                     }
                     file: {
                        
                     }
                  }
               }
               rcrowley: {
                  
                  go-metrics: {
                     
                     exp: {
                        
                     }
                  }
               }
               fatih: {
                  
                  color: {
                     
                  }
               }
               hashicorp: {
                  
                  golang-lru: {
                     
                     simplelru: {
                        
                     }
                  }
               }
               pborman: {
                  
                  uuid: {
                     
                  }
               }
               rs: {
                  
                  xhandler: {
                     
                  }
                  cors: {
                     
                  }
               }
               rjeczalik: {
                  
                  notify: {
                     
                  }
               }
               nsf: {
                  
                  termbox-go: {
                     
                  }
               }
               gizak: {
                  [config.py, table.go]
                  termui: {
                     [config.py, table.go]
                  }
               }
               golang: {
                  
                  snappy: {
                     
                  }
               }
               jackpal: {
                  
                  go-nat-pmp: {
                     
                  }
               }
               peterh: {
                  
                  liner: {
                     
                  }
               }
               syndtr: {
                  
                  goleveldb: {
                     
                     leveldb: {
                        
                        opt: {
                           
                        }
                        util: {
                           
                        }
                        errors: {
                           
                        }
                        iterator: {
                           
                        }
                        memdb: {
                           
                        }
                        journal: {
                           
                        }
                        cache: {
                           
                        }
                        storage: {
                           
                        }
                        filter: {
                           
                        }
                        comparer: {
                           
                        }
                        table: {
                           
                        }
                     }
                  }
               }
               ethereum: {
                  
                  ethash: {
                     
                     src: {
                        
                        libethash: {
                           
                        }
                     }
                  }
               }
               mattn: {
                  
                  go-colorable: {
                     
                  }
                  go-isatty: {
                     
                  }
                  go-runewidth: {
                     
                  }
               }
               cespare: {
                  
                  cp: {
                     
                  }
               }
               mitchellh: {
                  
                  go-wordwrap: {
                     
                  }
               }
               davecgh: {
                  
                  go-spew: {
                     
                     spew: {
                        
                     }
                  }
               }
            }
            gopkg.in: {
               [flag-types.json, flag_generated.go, generate-flag-types, .travis.yml]
               fatih: {
                  
                  set.v0: {
                     
                  }
               }
               karalabe: {
                  
                  cookiejar.v2: {
                     
                     collections: {
                        
                        prque: {
                           
                        }
                     }
                  }
               }
               urfave: {
                  [flag-types.json, flag_generated.go, generate-flag-types]
                  cli.v1: {
                     [flag-types.json, flag_generated.go, generate-flag-types]
                  }
               }
               check.v1: {
                  [.travis.yml]
               }
               sourcemap.v1: {
                  
                  base64vlq: {
                     
                  }
               }
               natefinch: {
                  
                  npipe.v2: {
                     
                  }
               }
            }
            golang.org: {
               [syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s, cast5, openpgp]
               x: {
                  [syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s, cast5, openpgp]
                  sys: {
                     [syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s]
                     unix: {
                        [syscall_linux_mipsx.go, zerrors_linux_mipsle.go, syscall_unix_gc.go, zsyscall_linux_mipsle.go, zsysnum_linux_mipsle.go, syscall_linux_amd64_gc.go, zerrors_linux_mips.go, zsysnum_linux_mips.go, ztypes_linux_mipsle.go, ztypes_linux_mips.go, zsyscall_linux_mips.go, asm_linux_mipsx.s]
                     }
                  }
                  text: {
                     
                     runes: {
                        
                     }
                     language: {
                        
                     }
                     encoding: {
                        
                        charmap: {
                           
                        }
                        japanese: {
                           
                        }
                        simplifiedchinese: {
                           
                        }
                        htmlindex: {
                           
                        }
                        internal: {
                           
                           identifier: {
                              
                           }
                        }
                        traditionalchinese: {
                           
                        }
                        unicode: {
                           
                        }
                        korean: {
                           
                        }
                     }
                     transform: {
                        
                     }
                     internal: {
                        
                        tag: {
                           
                        }
                        gen: {
                           
                        }
                        utf8internal: {
                           
                        }
                     }
                     unicode: {
                        
                        cldr: {
                           
                        }
                     }
                  }
                  net: {
                     
                     html: {
                        
                        charset: {
                           
                        }
                        atom: {
                           
                        }
                     }
                     websocket: {
                        
                     }
                  }
                  tools: {
                     
                     go: {
                        
                        ast: {
                           
                           astutil: {
                              
                           }
                        }
                     }
                     imports: {
                        
                     }
                  }
                  crypto: {
                     [cast5, openpgp]
                     pbkdf2: {
                        
                     }
                     ripemd160: {
                        
                     }
                     scrypt: {
                        
                     }
                  }
               }
            }
         }
         contracts: {
            
            chequebook: {
               
               contract: {
                  
               }
            }
            release: {
               
            }
            ens: {
               
               contract: {
                  
               }
            }
         }
         ethdb: {
            
         }
         metrics: {
            
         }
         p2p: {
            [netutil, discv5]
            discover: {
               
            }
            nat: {
               
            }
         }
         .git: {
            [FETCH_HEAD, release, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.idx, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.pack, release]
            info: {
               
            }
            hooks: {
               
            }
            refs: {
               [release]
               remotes: {
                  
                  origin: {
                     
                  }
               }
               heads: {
                  [release]
               }
            }
            objects: {
               [pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.idx, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.pack]
               info: {
                  
               }
               pack: {
                  [pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.idx, pack-930bede8f146646f44ba6f2140f12a0fc51cbc6f.pack]
               }
            }
            logs: {
               [release]
               refs: {
                  [release]
                  remotes: {
                     
                     origin: {
                        
                     }
                  }
                  heads: {
                     [release]
                  }
               }
            }
         }
         light: {
            [vm_env.go, txpool_test.go, lightchain.go, odr_test.go, txpool.go, lightchain_test.go, odr_util.go]
         }
         cmd: {
            [swarm, wnode, misccmd.go, dao_test.go]
            geth: {
               [misccmd.go, dao_test.go]
               testdata: {
                  
               }
            }
            abigen: {
               
            }
            bootnode: {
               
            }
            evm: {
               
            }
            utils: {
               
            }
            ethtest: {
               
            }
            disasm: {
               
            }
            rlpdump: {
               
            }
            gethrpctest: {
               
            }
         }
         crypto: {
            [ext.h, sage, build-aux, contrib, scalar_low.h, asm, scalar_low_impl.h, tests_exhaustive.c, org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
            ecies: {
               
            }
            sha3: {
               
               testdata: {
                  
               }
            }
            secp256k1: {
               [ext.h, sage, build-aux, contrib, scalar_low.h, asm, scalar_low_impl.h, tests_exhaustive.c, org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
               libsecp256k1: {
                  [sage, build-aux, contrib, scalar_low.h, asm, scalar_low_impl.h, tests_exhaustive.c, org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
                  src: {
                     [scalar_low.h, asm, scalar_low_impl.h, tests_exhaustive.c, org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
                     java: {
                        [org_bitcoin_Secp256k1Context.c, org_bitcoin_Secp256k1Context.h, Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
                        org: {
                           [Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
                           bitcoin: {
                              [Secp256k1Context.java, NativeSecp256k1Util.java, NativeSecp256k1Test.java]
                           }
                        }
                     }
                     modules: {
                        
                        ecdh: {
                           
                        }
                        recovery: {
                           
                        }
                     }
                  }
                  include: {
                     
                  }
                  obj: {
                     
                  }
               }
            }
            randentropy: {
               
            }
         }
         common: {
            [hexutil, mclock, exp.go]
            number: {
               
            }
            math: {
               [exp.go]
            }
            compiler: {
               
            }
         }
         eth: {
            [sync_test.go, gasprice]
            fetcher: {
               
            }
            filters: {
               
            }
            downloader: {
               
            }
         }
         ethclient: {
            
         }
      }

------

QUORUM ONLY: 95

      {
         [private, permissioned-nodes-sample.json, permissioned-nodes.json, BUILDING.md, generators, docs, raft, _data, types_test.go, watch_fallback.go, addrcache.go, key_store_plain.go, testdata, key_store_passphrase_test.go, account_manager.go, key.go, accounts_test.go, watch.go, key_store_test.go, presale.go, addrcache_test.go, key_store_passphrase.go, pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.idx, pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.pack, bignumber_js.go, ethereum_js.go, quorum.go, ezp, dagger, example_test.go, loggers.go, types.go, logsystem.go, loggers_test.go, log_raft_checkpoint.go, log.go, sys.go, config.go, vm_env.go, dual_state_test.go, private_state_test.go, quorum, execution.go, call_helper.go, jit_optimiser.go, segments.go, jit.go, jump_table_test.go, log_test.go, util_test.go, jit_test.go, jit_util.go, log.go, jit_util_test.go, json.go, json_test.go, stDelegatecallTest.json, eapache, BurntSushi, beorn7, xiang90, matttproud, prometheus, coreos, tv42, patrickmn, protobuf, config, signal_legacy.go, signal.go, oleiade, permissions.go, udp_windows.go, udp_notwindows.go, library.go, library.c, info_test.json, library_android.go, code.txt, input.txt, bootnodes.go, version.go, .jshintrc, .gitignore, .npmignore, .bowerrc, .editorconfig, .travis.yml, pubkey_scalar_mul.h, notes.go, schnorr, secp256k1_schnorr.h, httpclient, registrar, block_voting.go]
         trie: {
            
         }
         whisper: {
            
            whisperv5: {
               
            }
            whisperv2: {
               
            }
            shhapi: {
               
            }
         }
         rpc: {
            [types_test.go]
         }
         accounts: {
            [watch_fallback.go, addrcache.go, key_store_plain.go, testdata, key_store_passphrase_test.go, account_manager.go, key.go, accounts_test.go, watch.go, key_store_test.go, presale.go, addrcache_test.go, key_store_passphrase.go]
            abi: {
               
               bind: {
                  
                  backends: {
                     
                  }
               }
            }
         }
         errs: {
            
         }
         event: {
            
            filter: {
               
            }
         }
         console: {
            
            testdata: {
               
            }
         }
         compression: {
            
            rle: {
               
            }
         }
         .github: {
            
         }
         rlp: {
            
         }
         swarm: {
            
            services: {
               
               swap: {
                  
                  swap: {
                     
                  }
               }
            }
            api: {
               
               http: {
                  
               }
               testdata: {
                  
                  test0: {
                     
                     img: {
                        
                     }
                  }
               }
            }
            storage: {
               
            }
            network: {
               
               kademlia: {
                  
               }
            }
         }
         internal: {
            [bignumber_js.go, ethereum_js.go]
            debug: {
               
            }
            web3ext: {
               
            }
            ethapi: {
               
            }
            jsre: {
               [bignumber_js.go, ethereum_js.go]
            }
            build: {
               
            }
         }
         params: {
            [quorum.go]
         }
         build: {
            
            _vendor: {
               
               src: {
                  
                  golang.org: {
                     
                     x: {
                        
                        net: {
                           
                           context: {
                              
                           }
                        }
                     }
                  }
               }
            }
         }
         pow: {
            [ezp, dagger]
         }
         logger: {
            [example_test.go, loggers.go, types.go, logsystem.go, loggers_test.go, log_raft_checkpoint.go, log.go, sys.go]
            glog: {
               
            }
         }
         containers: {
            
            docker: {
               
               master-alpine: {
                  
               }
               develop-alpine: {
                  
               }
               develop-ubuntu: {
                  
               }
               master-ubuntu: {
                  
               }
            }
            vagrant: {
               
            }
         }
         node: {
            
         }
         core: {
            [config.go, vm_env.go, dual_state_test.go, private_state_test.go, quorum, execution.go, call_helper.go, jit_optimiser.go, segments.go, jit.go, jump_table_test.go, log_test.go, util_test.go, jit_test.go, jit_util.go, log.go, jit_util_test.go, json.go, json_test.go]
            state: {
               
            }
            vm: {
               [jit_optimiser.go, segments.go, jit.go, jump_table_test.go, log_test.go, util_test.go, jit_test.go, jit_util.go, log.go, jit_util_test.go]
               runtime: {
                  
               }
            }
            types: {
               [json.go, json_test.go]
            }
         }
         tests: {
            [stDelegatecallTest.json]
            files: {
               [stDelegatecallTest.json]
               VMTests: {
                  
                  RandomTests: {
                     
                  }
               }
               TrieTests: {
                  
               }
               StateTests: {
                  [stDelegatecallTest.json]
                  RandomTests: {
                     
                  }
                  EIP150: {
                     
                     Homestead: {
                        
                     }
                  }
                  Homestead: {
                     
                  }
               }
               ABITests: {
                  
               }
               PoWTests: {
                  
               }
               RLPTests: {
                  
                  RandomRLPTests: {
                     
                  }
               }
               KeyStoreTests: {
                  
               }
               BasicTests: {
                  
               }
               GenesisTests: {
                  
               }
               TransactionTests: {
                  
                  RandomTests: {
                     
                  }
                  Homestead: {
                     
                  }
               }
               BlockchainTests: {
                  
                  RandomTests: {
                     
                  }
                  TestNetwork: {
                     
                  }
                  Homestead: {
                     
                  }
               }
            }
         }
         vendor: {
            [eapache, BurntSushi, beorn7, xiang90, matttproud, prometheus, coreos, tv42, patrickmn, protobuf, config, signal_legacy.go, signal.go, oleiade]
            github.com: {
               [eapache, BurntSushi, beorn7, xiang90, matttproud, prometheus, coreos, tv42, patrickmn, protobuf, config, signal_legacy.go, signal.go]
               huin: {
                  
                  goupnp: {
                     
                     dcps: {
                        
                        internetgateway1: {
                           
                        }
                        internetgateway2: {
                           
                        }
                     }
                     httpu: {
                        
                     }
                     ssdp: {
                        
                     }
                     scpd: {
                        
                     }
                     soap: {
                        
                     }
                  }
               }
               robertkrimen: {
                  
                  otto: {
                     
                     ast: {
                        
                     }
                     parser: {
                        
                     }
                     dbg: {
                        
                     }
                     token: {
                        
                     }
                     registry: {
                        
                     }
                     file: {
                        
                     }
                  }
               }
               rcrowley: {
                  
                  go-metrics: {
                     
                     exp: {
                        
                     }
                  }
               }
               fatih: {
                  
                  color: {
                     
                  }
               }
               hashicorp: {
                  
                  golang-lru: {
                     
                     simplelru: {
                        
                     }
                  }
               }
               pborman: {
                  
                  uuid: {
                     
                  }
               }
               rs: {
                  
                  xhandler: {
                     
                  }
                  cors: {
                     
                  }
               }
               rjeczalik: {
                  
                  notify: {
                     
                  }
               }
               nsf: {
                  
                  termbox-go: {
                     
                  }
               }
               gizak: {
                  [config]
                  termui: {
                     [config]
                  }
               }
               golang: {
                  [protobuf]
                  snappy: {
                     
                  }
               }
               jackpal: {
                  
                  go-nat-pmp: {
                     
                  }
               }
               peterh: {
                  [signal_legacy.go, signal.go]
                  liner: {
                     [signal_legacy.go, signal.go]
                  }
               }
               syndtr: {
                  
                  goleveldb: {
                     
                     leveldb: {
                        
                        opt: {
                           
                        }
                        util: {
                           
                        }
                        errors: {
                           
                        }
                        iterator: {
                           
                        }
                        memdb: {
                           
                        }
                        journal: {
                           
                        }
                        cache: {
                           
                        }
                        storage: {
                           
                        }
                        filter: {
                           
                        }
                        comparer: {
                           
                        }
                        table: {
                           
                        }
                     }
                  }
               }
               ethereum: {
                  
                  ethash: {
                     
                     src: {
                        
                        libethash: {
                           
                        }
                     }
                  }
               }
               mattn: {
                  
                  go-colorable: {
                     
                  }
                  go-isatty: {
                     
                  }
                  go-runewidth: {
                     
                  }
               }
               cespare: {
                  
                  cp: {
                     
                  }
               }
               mitchellh: {
                  
                  go-wordwrap: {
                     
                  }
               }
               davecgh: {
                  
                  go-spew: {
                     
                     spew: {
                        
                     }
                  }
               }
            }
            gopkg.in: {
               [oleiade]
               fatih: {
                  
                  set.v0: {
                     
                  }
               }
               karalabe: {
                  
                  cookiejar.v2: {
                     
                     collections: {
                        
                        prque: {
                           
                        }
                     }
                  }
               }
               urfave: {
                  
                  cli.v1: {
                     
                  }
               }
               check.v1: {
                  
               }
               sourcemap.v1: {
                  
                  base64vlq: {
                     
                  }
               }
               natefinch: {
                  
                  npipe.v2: {
                     
                  }
               }
            }
            golang.org: {
               
               x: {
                  
                  sys: {
                     
                     unix: {
                        
                     }
                  }
                  text: {
                     
                     runes: {
                        
                     }
                     language: {
                        
                     }
                     encoding: {
                        
                        charmap: {
                           
                        }
                        japanese: {
                           
                        }
                        simplifiedchinese: {
                           
                        }
                        htmlindex: {
                           
                        }
                        internal: {
                           
                           identifier: {
                              
                           }
                        }
                        traditionalchinese: {
                           
                        }
                        unicode: {
                           
                        }
                        korean: {
                           
                        }
                     }
                     transform: {
                        
                     }
                     internal: {
                        
                        tag: {
                           
                        }
                        gen: {
                           
                        }
                        utf8internal: {
                           
                        }
                     }
                     unicode: {
                        
                        cldr: {
                           
                        }
                     }
                  }
                  net: {
                     
                     html: {
                        
                        charset: {
                           
                        }
                        atom: {
                           
                        }
                     }
                     websocket: {
                        
                     }
                  }
                  tools: {
                     
                     go: {
                        
                        ast: {
                           
                           astutil: {
                              
                           }
                        }
                     }
                     imports: {
                        
                     }
                  }
                  crypto: {
                     
                     pbkdf2: {
                        
                     }
                     ripemd160: {
                        
                     }
                     scrypt: {
                        
                     }
                  }
               }
            }
         }
         contracts: {
            
            chequebook: {
               
               contract: {
                  
               }
            }
            release: {
               
            }
            ens: {
               
               contract: {
                  
               }
            }
         }
         ethdb: {
            
         }
         metrics: {
            
         }
         p2p: {
            [permissions.go, udp_windows.go, udp_notwindows.go]
            discover: {
               [udp_windows.go, udp_notwindows.go]
            }
            nat: {
               
            }
         }
         .git: {
            [pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.idx, pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.pack]
            info: {
               
            }
            hooks: {
               
            }
            refs: {
               
               remotes: {
                  
                  origin: {
                     
                  }
               }
               heads: {
                  
               }
            }
            objects: {
               [pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.idx, pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.pack]
               info: {
                  
               }
               pack: {
                  [pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.idx, pack-8e592620716e79ae65ba799fb710f2ac0a1a58b2.pack]
               }
            }
            logs: {
               
               refs: {
                  
                  remotes: {
                     
                     origin: {
                        
                     }
                  }
                  heads: {
                     
                  }
               }
            }
         }
         light: {
            
         }
         cmd: {
            [library.go, library.c, info_test.json, library_android.go, code.txt, input.txt, bootnodes.go, version.go, .jshintrc, .gitignore, .npmignore, .bowerrc, .editorconfig, .travis.yml]
            geth: {
               [library.go, library.c, info_test.json, library_android.go]
               testdata: {
                  
               }
            }
            abigen: {
               
            }
            bootnode: {
               
            }
            evm: {
               [code.txt, input.txt]
            }
            utils: {
               [bootnodes.go, version.go]
            }
            ethtest: {
               [.jshintrc, .gitignore, .npmignore, .bowerrc, .editorconfig, .travis.yml]
            }
            disasm: {
               
            }
            rlpdump: {
               
            }
            gethrpctest: {
               
            }
         }
         crypto: {
            [pubkey_scalar_mul.h, notes.go, schnorr, secp256k1_schnorr.h]
            ecies: {
               
            }
            sha3: {
               
               testdata: {
                  
               }
            }
            secp256k1: {
               [pubkey_scalar_mul.h, notes.go, schnorr, secp256k1_schnorr.h]
               libsecp256k1: {
                  [schnorr, secp256k1_schnorr.h]
                  src: {
                     [schnorr]
                     java: {
                        
                        org: {
                           
                           bitcoin: {
                              
                           }
                        }
                     }
                     modules: {
                        [schnorr]
                        ecdh: {
                           
                        }
                        recovery: {
                           
                        }
                     }
                  }
                  include: {
                     [secp256k1_schnorr.h]
                  }
                  obj: {
                     
                  }
               }
            }
            randentropy: {
               
            }
         }
         common: {
            [httpclient, registrar]
            number: {
               
            }
            math: {
               
            }
            compiler: {
               
            }
         }
         eth: {
            [block_voting.go]
            fetcher: {
               
            }
            filters: {
               
            }
            downloader: {
               
            }
         }
         ethclient: {
            
         }
      }

------

IDENTICAL FILES: 1710

      {
         [COPYING, COPYING.LESSER, .gitattributes, circle.yml, secure_trie.go, iterator.go, proof_test.go, encoding_test.go, node.go, node_test.go, proof.go, secure_trie_test.go, errors.go, topic.go, whisper.go, envelope.go, whisper_test.go, doc.go, main.go, message.go, errors.go, client_context_go1.6.go, websocket.go, client_context_go1.4.go, client_test.go, client_context_go1.7.go, doc.go, utils.go, http.go, inproc.go, client_example_test.go, client_context_go1.5.go, ipc_windows.go, server_test.go, ipc_unix.go, json_test.go, ipc.go, utils_test.go, event_test.go, error.go, doc.go, method.go, numbers_test.go, numbers.go, util.go, example_test.go, filter_test.go, filter.go, preload.js, exec.js, read_write_test.go, description, exclude, pre-rebase.sample, prepare-commit-msg.sample, post-update.sample, applypatch-msg.sample, update.sample, pre-receive.sample, pre-applypatch.sample, commit-msg.sample, pre-push.sample, pre-commit.sample, HEAD, swap.go, swap.go, swap_test.go, storage_test.go, testapi.go, manifest_test.go, api_test.go, storage.go, index.html, index.css, logo.png, pyramid.go, memstore_test.go, database.go, chunker_test.go, messages.go, forwarding.go, syncdb.go, address.go, kademlia.go, address_test.go, kaddb.go, loudpanic.go, trace_fallback.go, trace.go, loudpanic_fallback.go, flags.go, api.go, solc.go, jsre_test.go, completion_test.go, completion.go, dao.go, deb.docs, deb.copyright, deb.rules, deb.control, deb.changelog, deb.install, LICENSE, pre_go17.go, context.go, go17.go, block.go, pow.go, verbosity.go, README, glog_file.go, glog_test.go, LICENSE, Vagrantfile, service_test.go, errors.go, doc.go, defaults.go, utils_test.go, service.go, error.go, asm.go, fees.go, gaspool.go, helper_test.go, .gitignore, filter_test.go, chain_pow.go, main_test.go, dump.go, managed_state.go, asm.go, memory.go, doc.go, analysis.go, disasm.go, virtual_machine.go, common.go, doc.go, runtime_example_test.go, bloom9_test.go, derive_sha.go, rlp_test_util.go, rlp_test.go, .gitignore, README.md, TODO, vmInputLimits.json, vmBitwiseLogicOperationTest.json, vmtests.json, vmLogTest.json, vmBlockInfoTest.json, vmArithmeticTest.json, vmSha3Test.json, vmInputLimitsLight.json, 201503120525PYTHON.json, 201503110206PYTHON.json, 201503112218PYTHON.json, 201503110526PYTHON.json, 201503102320PYTHON.json, 201503111844PYTHON.json, 201503120317PYTHON.json, 201503110050PYTHON.json, 201503102300PYTHON.json, 201503102148PYTHON.json, 201503120909PYTHON.json, randomTest.json, 201503110226PYTHON_DUP6.json, 201503120547PYTHON.json, 201503102037PYTHON.json, 201503110219PYTHON.json, 201503110346PYTHON_PUSH24.json, hex_encoded_securetrie_test.json, trieanyorder_secureTrie.json, trieanyorder.json, trietest.json, trietestnextprev.json, trietest_secureTrie.json, stInitCodeTest.json, stRefundTest.json, stMemoryStressTest.json, stTransitionTest.json, stMemoryTest.json, stTransactionTest.json, stCallCodes.json, stWalletTest.json, stBlockHashTest.json, stQuadraticComplexityTest.json, stSolidityTest.json, stCallCreateCallCodeTest.json, stExample.json, stRecursiveCreate.json, stLogTests.json, stSpecialTest.json, st201503181543GO.json, st201503181647CPPJIT.json, st201503130733CPPJIT.json, st201504100125CPPJIT.json, st201504230729CPPJIT.json, st201503181342CPPJIT.json, st201504071905CPPJIT.json, st201503181406CPPJIT.json, st201503140756PYTHON.json, st201504202124CPPJIT.json, st201503181922GO.json, st201503181749GO.json, st201503181441GO.json, st201503181800GO.json, st201503181740GO.json, st201503181241CPPJIT.json, st201503181322GO.json, st201506091836GO.json, st201503181931GO.json, st201503181329CPPJIT.json, st201503122159GO.json, st201503181740CPPJIT.json, st201503132127PYTHON.json, st201503181544CPPJIT.json, st201504240817CPPJIT.json, st201503151450PYTHON.json, st201503181341CPPJIT.json, st201503181410GO.json, st201503181850GO.json, st201504070746JS.json, st201503181723GO.json, st201503181250CPPJIT.json, st201503181656GO.json, st201503181848GO.json, st201503130405GO.json, st201504140818CPPJIT.json, st201503181821GO.json, st201503181239GO.json, st201503181318CPPJIT.json, st201503181630GO.json, st201503181559GO.json, st201503181225GO.json, st201503170523PYTHON.json, st201504210245CPPJIT.json, st201503191646GO.json, st201503181620GO.json, st201504062314CPPJIT.json, st201503181735GO.json, st201504240220CPPJIT.json, st201503181311GO.json, st201503181354CPPJIT.json, st201503181223GO.json, st201503181506CPPJIT.json, st201503181834GO.json, st201503302210JS.json, st201503181634CPPJIT.json, st201503181723CPPJIT.json, st201503181849GO.json, st201504061134CPPJIT.json, st201504080840CPPJIT.json, st201503181854GO.json, st201503181714GO.json, st201503122238GO.json, st201503181315GO.json, st201503181226CPPJIT.json, st201503181500GO.json, st201503181750CPPJIT.json, st201505052242PYTHON.json, st201503181847GO.json, st201504011916JS.json, st201503181248GO.json, st201503140240PYTHON.json, st201504130653JS.json, st201503181702GO.json, st201503181548CPPJIT.json, st201503130332GO.json, st201503181355GO.json, st201504022003CPPJIT.json, st201504060057CPPJIT.json, st201504020305JS.json, st201504021237JS.json, st201504090657CPPJIT.json, st201504101338CPPJIT.json, st201503181626CPPJIT.json, st201504011535GO.json, st201503181358CPPJIT.json, st201504101150CPPJIT.json, st201503181237GO.json, st201503181252CPPJIT.json, st201503181347CPPJIT.json, st201506040034GO.json, st201503151753PYTHON.json, st201503181227CPPJIT.json, st201504030709JS.json, st201503122128PYTHON.json, st201503181629GO.json, st201503181538GO.json, st201503181450GO.json, st201505052343PYTHON.json, st201504051944CPPJIT.json, st201505051249GO.json, st201506092032GO.json, st201503181641GO.json, st201504090553CPPJIT.json, st201503181759GO.json, st201503181339CPPJIT.json, st201503181423CPPJIT.json, st201503181815GO.json, st201503130450GO.json, st201503181437CPPJIT.json, st201503181553GO.json, st201503240609JS.json, st201503181812GO.json, st201504011536GO.json, st201503181232CPPJIT.json, st201503181756GO.json, st201503181803GO.json, st201504020538JS.json, st201503181619GO.json, st201503130117GO.json, st201503181406GO.json, st201503132001CPPJIT.json, st201503181519GO.json, st201503132202PYTHON.json, st201503181608GO.json, st201503181904GO.json, st201504081134CPPJIT.json, st201503181308GO.json, st201503181359GO.json, st201503181536CPPJIT.json, st201503122252GO.json, st201503181354GO.json, st201503130156PYTHON.json, st201503181533GO.json, st201503121850GO.json, st201503171108PYTHON.json, st201503181435GO.json, st201504211739CPPJIT.json, st201503181338GO.json, st201503140002PYTHON.json, st201504052014GO.json, st201503181929GO.json, st201504082002JAVA.json, st201504081841JAVA.json, st201503181734CPPJIT.json, st201503200841JS.json, st201504212038CPPJIT.json, st201503181907GO.json, st201503181447GO.json, st201503160733PYTHON.json, st201506080721GO.json, st201503181833GO.json, st201504020431JS.json, st201503181527GO.json, st201503181417GO.json, st201503181455GO.json, st201503181834CPPJIT.json, st201503181246GO.json, st201504101223CPPJIT.json, st201503181843GO.json, st201504071041CPPJIT.json, st201503181424GO.json, st201503130751GO.json, st201504030646JS.json, st201503181728GO.json, st201503122358GO.json, st201503181822GO.json, st201503181519CPPJIT.json, st201503181757GO.json, st201503130219GO.json, st201503181757CPPJIT.json, st201503181241GO.json, st201503130122GO.json, st201503181430CPPJIT.json, st201504071056CPPJIT.json, st201503181753CPPJIT.json, st201503181233GO.json, st201503181803CPPJIT.json, st201503140522PYTHON.json, st201505050942PYTHON.json, st201503181326GO.json, st201504140359CPPJIT.json, st201505052102JS.json, st201503130757PYTHON.json, st201505252314CPPJIT.json, st201504100226PYTHON.json, st201503200838JS.json, st201505060121GO.json, st201503181245CPPJIT.json, st201503181458GO.json, st201503181823GO.json, st201503181920GO.json, st201503131739GO.json, st201503181747GO.json, st201503181307GO.json, st201503181657GO.json, st201503181816CPPJIT.json, st201503302202JS.json, st201503302206JS.json, st201503181840GO.json, st201504042226CPPJIT.json, st201504052031CPPJIT.json, st201503181438GO.json, st201503181626GO.json, st201503181817CPPJIT.json, st201507030359GO.json, st201503181742CPPJIT.json, st201503122054GO.json, st201503181446GO.json, st201503130322GO.json, st201503181235CPPJIT.json, st201503181522GO.json, st201503181428GO.json, st201503122231GO.json, st201503181251GO.json, st201503181552CPPJIT.json, st201503141510PYTHON.json, st201503181245GO.json, st201503121848GO.json, st201503181356CPPJIT.json, st201504021237PYTHON.json, st201504031446JS.json, st201503152057PYTHON.json, st201503181845GO.json, st201503181342GO.json, st201503181611CPPJIT.json, st201503181618GO.json, st201503122115CPPJIT.json, st201504031133JS.json, st201505051648JS.json, st201503181309GO.json, st201503181608CPPJIT.json, st201503181650GO.json, st201503181627GO.json, st201503181436GO.json, st201504111554CPPJIT.json, st201503181230GO.json, st201505051611PYTHON.json, st201503181919CPPJIT.json, st201503181602GO.json, st201503181610GO.json, st201504020400JS.json, st201503130207GO.json, st201504052008CPPJIT.json, st201505051238GO.json, st201504100337CPPJIT.json, st201503181504GO.json, st201503181503GO.json, st201503181612GO.json, st201503181606GO.json, st201503181336CPPJIT.json, st201503181323CPPJIT.json, st201503181731CPPJIT.json, st201503181453GO.json, st201503181620CPPJIT.json, st201503181347GO.json, st201503181819GO.json, st201503181537GO.json, st201503181317GO.json, st201503122204GO.json, st201503181451CPPJIT.json, st201503181416GO.json, st201503181415GO.json, st201504232350CPPJIT.json, st201504060418CPPJIT.json, st201503181804GO.json, st201503181903GO.json, st201503181417CPPJIT.json, st201503181711GO.json, st201503181526GO.json, st201503122023GO.json, st201503181403GO.json, st201504100215CPPJIT.json, st201503181246CPPJIT.json, st201503181852CPPJIT.json, st201503181632GO.json, st201503181350CPPJIT.json, st201503122115GO.json, st201503181730GO.json, st201503181906GO.json, st201504081955JAVA.json, st201503181303GO.json, st201503181509CPPJIT.json, st201503181829GO.json, st201503181258CPPJIT.json, st201503181639CPPJIT.json, st201503181601GO.json, st201503130005GO.json, st201503181319GO.json, st201503181307CPPJIT.json, st201503181737GO.json, st201503181304GO.json, st201503131755GO.json, st201503181501GO.json, st201503130512CPPJIT.json, st201503181255GO.json, st201503181621GO.json, st201503150716PYTHON.json, st201503181316PYTHON.json, st201505060646JS.json, st201503181842GO.json, st201503181438CPPJIT.json, st201503132201GO.json, st201503181604GO.json, st201503181725GO.json, st201503181645GO.json, st201506062331GO.json, st201503181931CPPJIT.json, st201503181329GO.json, st201503181655CPPJIT.json, st201504020639JS.json, st201503181649CPPJIT.json, st201503181235GO.json, st201503181412CPPJIT.json, st201503181724CPPJIT.json, st201503181426CPPJIT.json, st201503152241PYTHON.json, st201503121806PYTHON.json, st201504070816CPPJIT.json, st201503181544GO.json, st201503181514GO.json, st201503181439PYTHON.json, st201504231710CPPJIT.json, st201504080650CPPJIT.json, st201503121803PYTHON.json, st201504092303CPPJIT.json, st201503181724GO.json, st201504020836JS.json, st201503181255CPPJIT.json, st201503181658GO.json, st201503302208JS.json, st201503181603GO.json, st201503181402CPPJIT.json, st201503181513CPPJIT.json, st201503121851GO.json, st201503181557GO.json, st201505052238JS.json, st201504081956JAVA.json, st201503181229GO.json, st201503130219CPPJIT.json, st201506061255GO.json, st201503181635GO.json, st201503181628GO.json, st201504061106CPPJIT.json, st201504231742CPPJIT.json, st201503181234GO.json, st201504031841JS.json, st201503181704GO.json, st201504082001JAVA.json, st201503181607GO.json, st201503181540CPPJIT.json, st201503130431GO.json, st201504101009CPPJIT.json, st201503181636GO.json, st201503181808GO.json, st201503181511GO.json, st201503181717GO.json, st201504131821CPPJIT.json, st201504081100CPPJIT.json, st201503181910GO.json, st201503181524GO.json, st201503181529GO.json, st201503181743GO.json, st201503160014PYTHON.json, st201503181340GO.json, st201503181617GO.json, st201504101754PYTHON.json, st201503181534GO.json, st201504021057JS.json, st201503181625GO.json, st201504070836CPPJIT.json, st201503181457GO.json, st201503181534CPPJIT.json, st201503181851GO.json, st201503181851CPPJIT.json, st201503181548GO.json, st201503181716GO.json, st201503181611GO.json, st201504012259JS.json, st201503181547GO.json, st201503181614CPPJIT.json, st201504020444JS.json, st201503181413GO.json, st201503131755CPPJIT.json, st201503181931PYTHON.json, st201503130002GO.json, st201503181528CPPJIT.json, st201506071819GO.json, st201503181715GO.json, st201503130059GO.json, st201503302200JS.json, st201503181520GO.json, st201503181243GO.json, st201503181754GO.json, st201503181555CPPJIT.json, st201503181846GO.json, st201503181327GO.json, st201503181512GO.json, st201503181353GO.json, st201505021810CPPJIT.json, st201504051540JS.json, st201506072007GO.json, st201503181744GO.json, st201503181610CPPJIT.json, st201504021237CPPJIT.json, st201503181926GO.json, st201503181919PYTHON.json, st201503181806GO.json, st201503181739GO.json, st201504011547GO.json, st201505051114GO.json, st201504021104JS.json, st201503181456CPPJIT.json, st201503181352GO.json, st201505060120GO.json, st201503130109GO.json, st201503181507GO.json, st201504042355CPPJIT.json, st201503181510GO.json, st201503130512GO.json, st201503181232GO.json, st201504050733JS.json, st201503181824GO.json, st201504071750CPPJIT.json, st201503181844GO.json, st201503181517GO.json, st201503181720CPPJIT.json, st201504070839CPPJIT.json, st201503181630PYTHON.json, st201505050929GO.json, st201504140900CPPJIT.json, st201503181234CPPJIT.json, st201504100308CPPJIT.json, st201503181520CPPJIT.json, st201503122023PYTHON.json, st201503130246GO.json, st201503181616GO.json, st201503181703CPPJIT.json, st201503181752GO.json, st201503181754CPPJIT.json, st201504030138JS.json, st201504151057CPPJIT.json, st201503181253GO.json, st201504071621CPPJIT.json, st201504081954JAVA.json, st201503181437GO.json, st201503181315CPPJIT.json, st201504100341CPPJIT.json, st201503200848JS.json, st201503130359GO.json, st201503122123GO.json, st201503181713CPPJIT.json, st201503181521GO.json, st201503181230CPPJIT.json, st201503181750GO.json, st201505050557JS.json, st201505051558PYTHON.json, st201503181357CPPJIT.json, st201503181422GO.json, st201503181746GO.json, st201503181426GO.json, st201504020910JS.json, st201503181729GO.json, st201506070548GO.json, st201506071624GO.json, st201503181244GO.json, st201503181748GO.json, st201503181345GO.json, st201504042052JS.json, st201503181755GO.json, st201503181700GO.json, st201504091403CPPJIT.json, st201504081843JAVA.json, st201504081138CPPJIT.json, st201503181247GO.json, st201503181324GO.json, st201503130733GO.json, st201503121849GO.json, st201503122055GO.json, st201503130705GO.json, st201503181258GO.json, st201503181332GO.json, st201503181555GO.json, st201503181734GO.json, st201504081928CPPJIT.json, st201503181855CPPJIT.json, st201503181755CPPJIT.json, st201503181231GO.json, st201504012130JS.json, st201503181236GO.json, st201503181738CPPJIT.json, st201504082000JAVA.json, st201505060136PYTHON.json, st201504062046CPPJIT.json, st201503181513GO.json, st201503181442GO.json, st201503181551GO.json, st201503181305GO.json, st201503181732GO.json, st201504241118CPPJIT.json, st201503181737CPPJIT.json, st201503181459GO.json, st201503130615GO.json, st201504140750CPPJIT.json, st201503130243GO.json, st201503130411GO.json, st201503122316GO.json, st201504240140CPPJIT.json, st201503181306GO.json, st201503170433PYTHON.json, st201505051004PYTHON.json, st201504020428JS.json, st201503130747GO.json, st201503181439GO.json, st201504062033CPPJIT.json, st201503181722GO.json, st201505051016PYTHON.json, st201503181653GO.json, st201503181638GO.json, st201503181655GO.json, st201506071050GO.json, st201506101359JS.json, st201504012359JS.json, st201504081957JAVA.json, st201504080457CPPJIT.json, st201503181531CPPJIT.json, st201503131658GO.json, st201503181605GO.json, st201503181540PYTHON.json, st201504021237GO.json, st201503181837GO.json, st201503181358GO.json, st201503181706GO.json, st201503181802GO.json, st201503181709GO.json, st201503130101GO.json, st201503181539GO.json, st201503181536GO.json, st201503181316CPPJIT.json, st201503181330GO.json, st201503181347PYTHON.json, st201503181801GO.json, st201503181609GO.json, st201503181630CPPJIT.json, st201503130752PYTHON.json, st201503181227GO.json, st201503181738GO.json, st201503130437GO.json, st201503181440GO.json, st201503151516PYTHON.json, st201503181517CPPJIT.json, st201503130408GO.json, st201503200837JS.json, st201505051710GO.json, st201504140236CPPJIT.json, st201503181319PYTHON.json, st201504081611CPPJIT.json, st201503181652CPPJIT.json, st201503181445CPPJIT.json, st201503181614GO.json, st201503181334GO.json, st201503181656CPPJIT.json, st201504041605JS.json, st201503181337GO.json, st201503170051PYTHON.json, st201503181528PYTHON.json, st201503122124GO.json, st201503181825GO.json, st201504150854CPPJIT.json, st201503181711CPPJIT.json, st201503130010GO.json, st201503181703GO.json, st201503181318GO.json, st201503130156GO.json, st201503181301GO.json, st201503181339GO.json, st201503181900GO.json, st201503122324GO.json, st201506040157GO.json, st201504081953JAVA.json, st201503122140GO.json, st201503181333GO.json, st201504071653CPPJIT.json, st201503181310GO.json, st201503121953GO.json, st201504080948CPPJIT.json, st201505272131CPPJIT.json, st201503181505GO.json, st201503181514CPPJIT.json, st201506080556GO.json, st201503181859GO.json, st201504022124JS.json, st201503181314GO.json, st201503181418CPPJIT.json, st201503150427PYTHON.json, st201503181713GO.json, st201503181323GO.json, st201503181301CPPJIT.json, st201503181257GO.json, st201503130023PYTHON.json, st201504050059JS.json, st201503181250GO.json, st201504080454CPPJIT.json, st201503141144PYTHON.json, st201503181830CPPJIT.json, st201503302211JS.json, st201503181616CPPJIT.json, st201503181915GO.json, st201504231639CPPJIT.json, st201503181528GO.json, st201503181325GO.json, st201504081842JAVA.json, st201503181857PYTHON.json, st201503130007GO.json, st201506060929GO.json, st201503130321GO.json, st201503181524CPPJIT.json, st201503181646GO.json, st201503181654GO.json, st201503181715CPPJIT.json, st201504021949JS.json, st201503181745CPPJIT.json, st201503181509GO.json, st201503181439CPPJIT.json, st201503181326CPPJIT.json, st201503132201CPPJIT.json, st201504140229CPPJIT.json, st201503181809CPPJIT.json, st201506052130GO.json, st201505052235GO.json, st201503122027GO.json, st201503181812CPPJIT.json, st201503181814CPPJIT.json, st201504210957CPPJIT.json, st201503181601CPPJIT.json, st201504091641CPPJIT.json, st201503181346GO.json, st201504240351CPPJIT.json, st201503181313GO.json, st201503181249GO.json, st201503122212GO.json, st201505052013GO.json, stBoundsTest.json, stMemoryStressTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stQuadraticComplexityTest.json, stInitCodeTest.json, stWalletTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, basic_abi_tests.json, ethash_tests.json, invalidRLPTest.json, rlptest.json, example.json, basic_tests.json, keyaddrtest.json, difficulty.json, difficultyHomestead.json, difficultyOlimpic.json, hexencodetest.json, difficultyMorden.json, crypto.json, genesishashestest.json, blockgenesistest.json, difficultyCustomHomestead.json, txtest.json, difficultyFrontier.json, basic_genesis_tests.json, tt10mbDataField.json, ttWrongRLPTransaction.json, tr201506052141PYTHON.json, ttWrongRLPTransaction.json, tt10mbDataField.json, bcUncleHeaderValiditiy.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcForkBlockTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcForkStressTest.json, bcValidBlockTest.json, bcForkUncle.json, bl10251623GO.json, bl201507071825GO.json, bcSimpleTransitionTest.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcValidBlockTest.json, bcUncleHeaderValiditiy.json, bcExploitTest.json, bcForkStressTest.json, LICENSE, .gitignore, goupnp.go, service_client.go, device.go, internetgateway1.go, internetgateway2.go, httpu.go, serve.go, ssdp.go, scpd.go, soap.go, types.go, result.go, cmpl_parse.go, builtin_regexp.go, type_date.go, LICENSE, builtin_string.go, value_primitive.go, cmpl_evaluate_expression.go, Makefile, cmpl_evaluate_statement.go, builtin_error.go, builtin_math.go, object_class.go, evaluate.go, dbg.go, cmpl_evaluate.go, otto.go, builtin_number.go, type_go_slice.go, value_number.go, type_string.go, DESIGN.markdown, type_arguments.go, .gitignore, type_array.go, type_go_map.go, builtin_function.go, runtime.go, type_number.go, builtin.go, inline.go, error.go, inline.pl, type_go_array.go, global.go, builtin_array.go, README.markdown, type_error.go, builtin_object.go, type_boolean.go, builtin_boolean.go, otto_.go, value_string.go, object.go, cmpl.go, type_function.go, scope.go, value.go, property.go, script.go, builtin_json.go, stash.go, type_regexp.go, clone.go, type_reference.go, console.go, type_go_struct.go, value_boolean.go, builtin_date.go, README.markdown, node.go, comments.go, lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go, dbg.go, README.markdown, tokenfmt, token_const.go, Makefile, token.go, README.markdown, registry.go, README.markdown, file.go, decode_other.go, encode_amd64.s, CONTRIBUTORS, LICENSE, encode_other.go, encode.go, decode_amd64.go, .gitignore, decode.go, decode_amd64.s, encode_amd64.go, AUTHORS, README, snappy.go, runtime_no_gccpufraction.go, LICENSE, syslog.go, .gitignore, timer.go, histogram.go, runtime.go, graphite.go, debug.go, ewma.go, counter.go, writer.go, meter.go, healthcheck.go, runtime_gccpufraction.go, validate.sh, opentsdb.go, metrics.go, README.md, json.go, memory.md, gauge_float64.go, runtime_cgo.go, log.go, runtime_no_cgo.go, .travis.yml, exp.go, LICENSE.md, .travis.yml, notify.go, watchpoint_other.go, watcher_fsevents.go, event_fen.go, watcher_inotify.go, tree_recursive.go, event_trigger.go, watcher_kqueue.go, util.go, event_readdcw.go, watchpoint.go, debug.go, LICENSE, doc.go, .gitignore, watcher_readdcw.go, tree_nonrecursive.go, event_inotify.go, watcher_trigger.go, tree.go, watchpoint_readdcw.go, appveyor.yml, watcher_fsevents_cgo.go, watcher_stub.go, event_fsevents.go, event.go, debug_debug.go, README.md, event_stub.go, event_kqueue.go, node.go, watcher_fen.go, AUTHORS, watcher_fen_cgo.go, .travis.yml, watcher.go, middleware.go, LICENSE, xhandler.go, chain.go, .travis.yml, README.md, cors.go, .travis.yml, README.md, LICENSE, utils.go, LICENSE, 2q.go, .gitignore, arc.go, lru.go, README.md, lru.go, api_common.go, LICENSE, collect_terminfo.py, termbox_common.go, syscalls_netbsd.go, syscalls_darwin.go, syscalls_darwin_amd64.go, terminfo_builtin.go, terminfo.go, syscalls_linux.go, syscalls_dragonfly.go, termbox_windows.go, AUTHORS, api_windows.go, syscalls_windows.go, syscalls_openbsd.go, syscalls_freebsd.go, syscalls.go, LICENSE, mkdocs.yml, .gitignore, README.md, .travis.yml, json.go, CONTRIBUTING.md, version4.go, CONTRIBUTORS, LICENSE, uuid.go, node.go, doc.go, time.go, hash.go, version1.go, .travis.yml, util.go, sql.go, dce.go, LICENSE, recorder.go, natpmp.go, network.go, .travis.yml, README.md, output_windows.go, input_linux.go, output.go, input_darwin.go, fallbackinput.go, bsdinput.go, COPYING, unixmode.go, README.md, .travis.yml, README.md, LICENSE, errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go, ethashc.go, Vagrantfile, ethash.go, Makefile, MANIFEST.in, .gitignore, appveyor.yml, CMakeLists.txt, .travis.yml, setup.py, README.md, sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h, LICENSE, .travis.yml, README.md, LICENSE, isatty_linux.go, doc.go, isatty_solaris.go, isatty_windows.go, isatty_bsd.go, README.md, isatty_appengine.go, runewidth.go, LICENSE, README.mkd, runewidth_posix.go, runewidth_windows.go, .travis.yml, runewidth_js.go, cp.go, LICENSE.txt, README.md, LICENSE.md, README.md, wordwrap.go, test_coverage.txt, cov_report.sh, .gitignore, .travis.yml, set_ts.go, set.go, LICENSE.md, set_nots.go, .travis.yml, README.md, README.md, LICENSE, prque.go, sstack.go, category.go, LICENSE, .gitignore, funcs.go, helpers.go, printer.go, LICENSE, run.go, .gitignore, benchmark.go, reporter.go, TODO, README.md, LICENSE, Makefile, consumer.go, .travis.yml, README.md, base64_vlq.go, znpipe_windows_amd64.go, doc.go, .gitignore, npipe_windows.go, znpipe_windows_386.go, LICENSE.txt, README.md, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, runes.go, cond.go, common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go, encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go, transform.go, tag.go, gen.go, utf8internal.go, makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go, dial.go, client.go, hybi.go, server.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, enclosing.go, util.go, imports.go, zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, pbkdf2.go, ripemd160.go, ripemd160block.go, scrypt.go, api.go, gencode.go, chequebook.sol, code.go, chequebook.go, contract.go, contract_test.go, ens.go, README.md, ens.go, ens.sol, database_test.go, interface.go, .gitignore, disk_nop.go, disk.go, rlpx_test.go, message.go, message_test.go, peer.go, peer_error.go, server_test.go, metrics.go, protocol.go, ntp.go, node_test.go, natupnp_test.go, nat.go, natupnp.go, raw.go, encoder_example_test.go, encode.go, doc.go, decode.go, decode_test.go, encode_test.go, raw_test.go, decode_tail_test.go, typecache.go, genesis_test.go, run_test.go, guswallet.json, wrong-passwords.txt, passwords.txt, empty.js, fdlimit_windows.go, fdlimit_freebsd.go, customflags_test.go, fdlimit_unix.go, fdlimit_test.go, main.go, encrypt_decrypt_test.go, LICENSE, params.go, .gitignore, README, xor_unaligned.go, sha3.go, LICENSE, shake.go, xor.go, doc.go, xor_generic.go, register.go, keccakf_amd64.s, keccakf.go, keccakf_amd64.go, hashes.go, PATENTS, keccakKats.json.deflate, rand_entropy.go, curve_test.go, .gitignore, panic_cb.go, autogen.sh, COPYING, TODO, scalar_8x32.h, scalar_4x64.h, field_5x52_asm_impl.h, ecmult_const.h, gen_context.c, bench.h, ecmult_gen.h, num_impl.h, bench_sign.c, num_gmp.h, bench_recover.c, basic-config.h, ecmult.h, scalar_8x32_impl.h, field_5x52.h, bench_schnorr_verify.c, field_10x26.h, .gitignore, path.go, debug.go, size.go, .gitignore, icap_test.go, test_utils.go, list.go, big.go, size_test.go, README.md, main_test.go, types_template.go, icap.go, .travis.yml, uint_test.go, int.go, dist.go, peer.go, metrics.go, fetcher.go, metrics.go, modes.go, events.go, types.go, metrics.go, api.go]
         trie: {
            [secure_trie.go, iterator.go, proof_test.go, encoding_test.go, node.go, node_test.go, proof.go, secure_trie_test.go, errors.go]
         }
         whisper: {
            [topic.go, whisper.go, envelope.go, whisper_test.go, doc.go, main.go, message.go]
            whisperv5: {
               
            }
            whisperv2: {
               [topic.go, whisper.go, envelope.go, whisper_test.go, doc.go, main.go, message.go]
            }
            shhapi: {
               
            }
         }
         rpc: {
            [errors.go, client_context_go1.6.go, websocket.go, client_context_go1.4.go, client_test.go, client_context_go1.7.go, doc.go, utils.go, http.go, inproc.go, client_example_test.go, client_context_go1.5.go, ipc_windows.go, server_test.go, ipc_unix.go, json_test.go, ipc.go, utils_test.go]
         }
         accounts: {
            [event_test.go, error.go, doc.go, method.go, numbers_test.go, numbers.go, util.go]
            abi: {
               [event_test.go, error.go, doc.go, method.go, numbers_test.go, numbers.go, util.go]
               bind: {
                  [util.go]
                  backends: {
                     
                  }
               }
            }
         }
         errs: {
            
         }
         event: {
            [example_test.go, filter_test.go, filter.go]
            filter: {
               [filter_test.go, filter.go]
            }
         }
         console: {
            [preload.js, exec.js]
            testdata: {
               [preload.js, exec.js]
            }
         }
         compression: {
            [read_write_test.go]
            rle: {
               [read_write_test.go]
            }
         }
         .github: {
            
         }
         rlp: {
            [raw.go, encoder_example_test.go, encode.go, doc.go, decode.go, decode_test.go, encode_test.go, raw_test.go, decode_tail_test.go, typecache.go]
         }
         swarm: {
            [swap.go, swap.go, swap_test.go, storage_test.go, testapi.go, manifest_test.go, api_test.go, storage.go, index.html, index.css, logo.png, pyramid.go, memstore_test.go, database.go, chunker_test.go, messages.go, forwarding.go, syncdb.go, address.go, kademlia.go, address_test.go, kaddb.go]
            services: {
               [swap.go, swap.go, swap_test.go]
               swap: {
                  [swap.go, swap.go, swap_test.go]
                  swap: {
                     [swap.go, swap_test.go]
                  }
               }
            }
            api: {
               [storage_test.go, testapi.go, manifest_test.go, api_test.go, storage.go, index.html, index.css, logo.png]
               http: {
                  
               }
               testdata: {
                  [index.html, index.css, logo.png]
                  test0: {
                     [index.html, index.css, logo.png]
                     img: {
                        [logo.png]
                     }
                  }
               }
            }
            storage: {
               [pyramid.go, memstore_test.go, database.go, chunker_test.go]
            }
            network: {
               [messages.go, forwarding.go, syncdb.go, address.go, kademlia.go, address_test.go, kaddb.go]
               kademlia: {
                  [address.go, kademlia.go, address_test.go, kaddb.go]
               }
            }
         }
         internal: {
            [loudpanic.go, trace_fallback.go, trace.go, loudpanic_fallback.go, flags.go, api.go, solc.go, jsre_test.go, completion_test.go, completion.go]
            debug: {
               [loudpanic.go, trace_fallback.go, trace.go, loudpanic_fallback.go, flags.go, api.go]
            }
            web3ext: {
               
            }
            ethapi: {
               [solc.go]
            }
            jsre: {
               [jsre_test.go, completion_test.go, completion.go]
            }
            build: {
               
            }
         }
         params: {
            [dao.go]
         }
         build: {
            [deb.docs, deb.copyright, deb.rules, deb.control, deb.changelog, deb.install, LICENSE, pre_go17.go, context.go, go17.go]
            _vendor: {
               [LICENSE, pre_go17.go, context.go, go17.go]
               src: {
                  [LICENSE, pre_go17.go, context.go, go17.go]
                  golang.org: {
                     [LICENSE, pre_go17.go, context.go, go17.go]
                     x: {
                        [LICENSE, pre_go17.go, context.go, go17.go]
                        net: {
                           [LICENSE, pre_go17.go, context.go, go17.go]
                           context: {
                              [pre_go17.go, context.go, go17.go]
                           }
                        }
                     }
                  }
               }
            }
         }
         pow: {
            [block.go, pow.go]
         }
         logger: {
            [verbosity.go, README, glog_file.go, glog_test.go, LICENSE]
            glog: {
               [README, glog_file.go, glog_test.go, LICENSE]
            }
         }
         containers: {
            [Vagrantfile]
            docker: {
               
               master-alpine: {
                  
               }
               develop-alpine: {
                  
               }
               develop-ubuntu: {
                  
               }
               master-ubuntu: {
                  
               }
            }
            vagrant: {
               [Vagrantfile]
            }
         }
         node: {
            [service_test.go, errors.go, doc.go, defaults.go, utils_test.go, service.go]
         }
         core: {
            [error.go, asm.go, fees.go, gaspool.go, helper_test.go, .gitignore, filter_test.go, chain_pow.go, main_test.go, dump.go, managed_state.go, asm.go, memory.go, doc.go, analysis.go, disasm.go, virtual_machine.go, common.go, doc.go, runtime_example_test.go, bloom9_test.go, derive_sha.go]
            state: {
               [main_test.go, dump.go, managed_state.go]
            }
            vm: {
               [asm.go, memory.go, doc.go, analysis.go, disasm.go, virtual_machine.go, common.go, doc.go, runtime_example_test.go]
               runtime: {
                  [doc.go, runtime_example_test.go]
               }
            }
            types: {
               [bloom9_test.go, derive_sha.go]
            }
         }
         tests: {
            [rlp_test_util.go, rlp_test.go, .gitignore, README.md, TODO, vmInputLimits.json, vmBitwiseLogicOperationTest.json, vmtests.json, vmLogTest.json, vmBlockInfoTest.json, vmArithmeticTest.json, vmSha3Test.json, vmInputLimitsLight.json, 201503120525PYTHON.json, 201503110206PYTHON.json, 201503112218PYTHON.json, 201503110526PYTHON.json, 201503102320PYTHON.json, 201503111844PYTHON.json, 201503120317PYTHON.json, 201503110050PYTHON.json, 201503102300PYTHON.json, 201503102148PYTHON.json, 201503120909PYTHON.json, randomTest.json, 201503110226PYTHON_DUP6.json, 201503120547PYTHON.json, 201503102037PYTHON.json, 201503110219PYTHON.json, 201503110346PYTHON_PUSH24.json, hex_encoded_securetrie_test.json, trieanyorder_secureTrie.json, trieanyorder.json, trietest.json, trietestnextprev.json, trietest_secureTrie.json, stInitCodeTest.json, stRefundTest.json, stMemoryStressTest.json, stTransitionTest.json, stMemoryTest.json, stTransactionTest.json, stCallCodes.json, stWalletTest.json, stBlockHashTest.json, stQuadraticComplexityTest.json, stSolidityTest.json, stCallCreateCallCodeTest.json, stExample.json, stRecursiveCreate.json, stLogTests.json, stSpecialTest.json, st201503181543GO.json, st201503181647CPPJIT.json, st201503130733CPPJIT.json, st201504100125CPPJIT.json, st201504230729CPPJIT.json, st201503181342CPPJIT.json, st201504071905CPPJIT.json, st201503181406CPPJIT.json, st201503140756PYTHON.json, st201504202124CPPJIT.json, st201503181922GO.json, st201503181749GO.json, st201503181441GO.json, st201503181800GO.json, st201503181740GO.json, st201503181241CPPJIT.json, st201503181322GO.json, st201506091836GO.json, st201503181931GO.json, st201503181329CPPJIT.json, st201503122159GO.json, st201503181740CPPJIT.json, st201503132127PYTHON.json, st201503181544CPPJIT.json, st201504240817CPPJIT.json, st201503151450PYTHON.json, st201503181341CPPJIT.json, st201503181410GO.json, st201503181850GO.json, st201504070746JS.json, st201503181723GO.json, st201503181250CPPJIT.json, st201503181656GO.json, st201503181848GO.json, st201503130405GO.json, st201504140818CPPJIT.json, st201503181821GO.json, st201503181239GO.json, st201503181318CPPJIT.json, st201503181630GO.json, st201503181559GO.json, st201503181225GO.json, st201503170523PYTHON.json, st201504210245CPPJIT.json, st201503191646GO.json, st201503181620GO.json, st201504062314CPPJIT.json, st201503181735GO.json, st201504240220CPPJIT.json, st201503181311GO.json, st201503181354CPPJIT.json, st201503181223GO.json, st201503181506CPPJIT.json, st201503181834GO.json, st201503302210JS.json, st201503181634CPPJIT.json, st201503181723CPPJIT.json, st201503181849GO.json, st201504061134CPPJIT.json, st201504080840CPPJIT.json, st201503181854GO.json, st201503181714GO.json, st201503122238GO.json, st201503181315GO.json, st201503181226CPPJIT.json, st201503181500GO.json, st201503181750CPPJIT.json, st201505052242PYTHON.json, st201503181847GO.json, st201504011916JS.json, st201503181248GO.json, st201503140240PYTHON.json, st201504130653JS.json, st201503181702GO.json, st201503181548CPPJIT.json, st201503130332GO.json, st201503181355GO.json, st201504022003CPPJIT.json, st201504060057CPPJIT.json, st201504020305JS.json, st201504021237JS.json, st201504090657CPPJIT.json, st201504101338CPPJIT.json, st201503181626CPPJIT.json, st201504011535GO.json, st201503181358CPPJIT.json, st201504101150CPPJIT.json, st201503181237GO.json, st201503181252CPPJIT.json, st201503181347CPPJIT.json, st201506040034GO.json, st201503151753PYTHON.json, st201503181227CPPJIT.json, st201504030709JS.json, st201503122128PYTHON.json, st201503181629GO.json, st201503181538GO.json, st201503181450GO.json, st201505052343PYTHON.json, st201504051944CPPJIT.json, st201505051249GO.json, st201506092032GO.json, st201503181641GO.json, st201504090553CPPJIT.json, st201503181759GO.json, st201503181339CPPJIT.json, st201503181423CPPJIT.json, st201503181815GO.json, st201503130450GO.json, st201503181437CPPJIT.json, st201503181553GO.json, st201503240609JS.json, st201503181812GO.json, st201504011536GO.json, st201503181232CPPJIT.json, st201503181756GO.json, st201503181803GO.json, st201504020538JS.json, st201503181619GO.json, st201503130117GO.json, st201503181406GO.json, st201503132001CPPJIT.json, st201503181519GO.json, st201503132202PYTHON.json, st201503181608GO.json, st201503181904GO.json, st201504081134CPPJIT.json, st201503181308GO.json, st201503181359GO.json, st201503181536CPPJIT.json, st201503122252GO.json, st201503181354GO.json, st201503130156PYTHON.json, st201503181533GO.json, st201503121850GO.json, st201503171108PYTHON.json, st201503181435GO.json, st201504211739CPPJIT.json, st201503181338GO.json, st201503140002PYTHON.json, st201504052014GO.json, st201503181929GO.json, st201504082002JAVA.json, st201504081841JAVA.json, st201503181734CPPJIT.json, st201503200841JS.json, st201504212038CPPJIT.json, st201503181907GO.json, st201503181447GO.json, st201503160733PYTHON.json, st201506080721GO.json, st201503181833GO.json, st201504020431JS.json, st201503181527GO.json, st201503181417GO.json, st201503181455GO.json, st201503181834CPPJIT.json, st201503181246GO.json, st201504101223CPPJIT.json, st201503181843GO.json, st201504071041CPPJIT.json, st201503181424GO.json, st201503130751GO.json, st201504030646JS.json, st201503181728GO.json, st201503122358GO.json, st201503181822GO.json, st201503181519CPPJIT.json, st201503181757GO.json, st201503130219GO.json, st201503181757CPPJIT.json, st201503181241GO.json, st201503130122GO.json, st201503181430CPPJIT.json, st201504071056CPPJIT.json, st201503181753CPPJIT.json, st201503181233GO.json, st201503181803CPPJIT.json, st201503140522PYTHON.json, st201505050942PYTHON.json, st201503181326GO.json, st201504140359CPPJIT.json, st201505052102JS.json, st201503130757PYTHON.json, st201505252314CPPJIT.json, st201504100226PYTHON.json, st201503200838JS.json, st201505060121GO.json, st201503181245CPPJIT.json, st201503181458GO.json, st201503181823GO.json, st201503181920GO.json, st201503131739GO.json, st201503181747GO.json, st201503181307GO.json, st201503181657GO.json, st201503181816CPPJIT.json, st201503302202JS.json, st201503302206JS.json, st201503181840GO.json, st201504042226CPPJIT.json, st201504052031CPPJIT.json, st201503181438GO.json, st201503181626GO.json, st201503181817CPPJIT.json, st201507030359GO.json, st201503181742CPPJIT.json, st201503122054GO.json, st201503181446GO.json, st201503130322GO.json, st201503181235CPPJIT.json, st201503181522GO.json, st201503181428GO.json, st201503122231GO.json, st201503181251GO.json, st201503181552CPPJIT.json, st201503141510PYTHON.json, st201503181245GO.json, st201503121848GO.json, st201503181356CPPJIT.json, st201504021237PYTHON.json, st201504031446JS.json, st201503152057PYTHON.json, st201503181845GO.json, st201503181342GO.json, st201503181611CPPJIT.json, st201503181618GO.json, st201503122115CPPJIT.json, st201504031133JS.json, st201505051648JS.json, st201503181309GO.json, st201503181608CPPJIT.json, st201503181650GO.json, st201503181627GO.json, st201503181436GO.json, st201504111554CPPJIT.json, st201503181230GO.json, st201505051611PYTHON.json, st201503181919CPPJIT.json, st201503181602GO.json, st201503181610GO.json, st201504020400JS.json, st201503130207GO.json, st201504052008CPPJIT.json, st201505051238GO.json, st201504100337CPPJIT.json, st201503181504GO.json, st201503181503GO.json, st201503181612GO.json, st201503181606GO.json, st201503181336CPPJIT.json, st201503181323CPPJIT.json, st201503181731CPPJIT.json, st201503181453GO.json, st201503181620CPPJIT.json, st201503181347GO.json, st201503181819GO.json, st201503181537GO.json, st201503181317GO.json, st201503122204GO.json, st201503181451CPPJIT.json, st201503181416GO.json, st201503181415GO.json, st201504232350CPPJIT.json, st201504060418CPPJIT.json, st201503181804GO.json, st201503181903GO.json, st201503181417CPPJIT.json, st201503181711GO.json, st201503181526GO.json, st201503122023GO.json, st201503181403GO.json, st201504100215CPPJIT.json, st201503181246CPPJIT.json, st201503181852CPPJIT.json, st201503181632GO.json, st201503181350CPPJIT.json, st201503122115GO.json, st201503181730GO.json, st201503181906GO.json, st201504081955JAVA.json, st201503181303GO.json, st201503181509CPPJIT.json, st201503181829GO.json, st201503181258CPPJIT.json, st201503181639CPPJIT.json, st201503181601GO.json, st201503130005GO.json, st201503181319GO.json, st201503181307CPPJIT.json, st201503181737GO.json, st201503181304GO.json, st201503131755GO.json, st201503181501GO.json, st201503130512CPPJIT.json, st201503181255GO.json, st201503181621GO.json, st201503150716PYTHON.json, st201503181316PYTHON.json, st201505060646JS.json, st201503181842GO.json, st201503181438CPPJIT.json, st201503132201GO.json, st201503181604GO.json, st201503181725GO.json, st201503181645GO.json, st201506062331GO.json, st201503181931CPPJIT.json, st201503181329GO.json, st201503181655CPPJIT.json, st201504020639JS.json, st201503181649CPPJIT.json, st201503181235GO.json, st201503181412CPPJIT.json, st201503181724CPPJIT.json, st201503181426CPPJIT.json, st201503152241PYTHON.json, st201503121806PYTHON.json, st201504070816CPPJIT.json, st201503181544GO.json, st201503181514GO.json, st201503181439PYTHON.json, st201504231710CPPJIT.json, st201504080650CPPJIT.json, st201503121803PYTHON.json, st201504092303CPPJIT.json, st201503181724GO.json, st201504020836JS.json, st201503181255CPPJIT.json, st201503181658GO.json, st201503302208JS.json, st201503181603GO.json, st201503181402CPPJIT.json, st201503181513CPPJIT.json, st201503121851GO.json, st201503181557GO.json, st201505052238JS.json, st201504081956JAVA.json, st201503181229GO.json, st201503130219CPPJIT.json, st201506061255GO.json, st201503181635GO.json, st201503181628GO.json, st201504061106CPPJIT.json, st201504231742CPPJIT.json, st201503181234GO.json, st201504031841JS.json, st201503181704GO.json, st201504082001JAVA.json, st201503181607GO.json, st201503181540CPPJIT.json, st201503130431GO.json, st201504101009CPPJIT.json, st201503181636GO.json, st201503181808GO.json, st201503181511GO.json, st201503181717GO.json, st201504131821CPPJIT.json, st201504081100CPPJIT.json, st201503181910GO.json, st201503181524GO.json, st201503181529GO.json, st201503181743GO.json, st201503160014PYTHON.json, st201503181340GO.json, st201503181617GO.json, st201504101754PYTHON.json, st201503181534GO.json, st201504021057JS.json, st201503181625GO.json, st201504070836CPPJIT.json, st201503181457GO.json, st201503181534CPPJIT.json, st201503181851GO.json, st201503181851CPPJIT.json, st201503181548GO.json, st201503181716GO.json, st201503181611GO.json, st201504012259JS.json, st201503181547GO.json, st201503181614CPPJIT.json, st201504020444JS.json, st201503181413GO.json, st201503131755CPPJIT.json, st201503181931PYTHON.json, st201503130002GO.json, st201503181528CPPJIT.json, st201506071819GO.json, st201503181715GO.json, st201503130059GO.json, st201503302200JS.json, st201503181520GO.json, st201503181243GO.json, st201503181754GO.json, st201503181555CPPJIT.json, st201503181846GO.json, st201503181327GO.json, st201503181512GO.json, st201503181353GO.json, st201505021810CPPJIT.json, st201504051540JS.json, st201506072007GO.json, st201503181744GO.json, st201503181610CPPJIT.json, st201504021237CPPJIT.json, st201503181926GO.json, st201503181919PYTHON.json, st201503181806GO.json, st201503181739GO.json, st201504011547GO.json, st201505051114GO.json, st201504021104JS.json, st201503181456CPPJIT.json, st201503181352GO.json, st201505060120GO.json, st201503130109GO.json, st201503181507GO.json, st201504042355CPPJIT.json, st201503181510GO.json, st201503130512GO.json, st201503181232GO.json, st201504050733JS.json, st201503181824GO.json, st201504071750CPPJIT.json, st201503181844GO.json, st201503181517GO.json, st201503181720CPPJIT.json, st201504070839CPPJIT.json, st201503181630PYTHON.json, st201505050929GO.json, st201504140900CPPJIT.json, st201503181234CPPJIT.json, st201504100308CPPJIT.json, st201503181520CPPJIT.json, st201503122023PYTHON.json, st201503130246GO.json, st201503181616GO.json, st201503181703CPPJIT.json, st201503181752GO.json, st201503181754CPPJIT.json, st201504030138JS.json, st201504151057CPPJIT.json, st201503181253GO.json, st201504071621CPPJIT.json, st201504081954JAVA.json, st201503181437GO.json, st201503181315CPPJIT.json, st201504100341CPPJIT.json, st201503200848JS.json, st201503130359GO.json, st201503122123GO.json, st201503181713CPPJIT.json, st201503181521GO.json, st201503181230CPPJIT.json, st201503181750GO.json, st201505050557JS.json, st201505051558PYTHON.json, st201503181357CPPJIT.json, st201503181422GO.json, st201503181746GO.json, st201503181426GO.json, st201504020910JS.json, st201503181729GO.json, st201506070548GO.json, st201506071624GO.json, st201503181244GO.json, st201503181748GO.json, st201503181345GO.json, st201504042052JS.json, st201503181755GO.json, st201503181700GO.json, st201504091403CPPJIT.json, st201504081843JAVA.json, st201504081138CPPJIT.json, st201503181247GO.json, st201503181324GO.json, st201503130733GO.json, st201503121849GO.json, st201503122055GO.json, st201503130705GO.json, st201503181258GO.json, st201503181332GO.json, st201503181555GO.json, st201503181734GO.json, st201504081928CPPJIT.json, st201503181855CPPJIT.json, st201503181755CPPJIT.json, st201503181231GO.json, st201504012130JS.json, st201503181236GO.json, st201503181738CPPJIT.json, st201504082000JAVA.json, st201505060136PYTHON.json, st201504062046CPPJIT.json, st201503181513GO.json, st201503181442GO.json, st201503181551GO.json, st201503181305GO.json, st201503181732GO.json, st201504241118CPPJIT.json, st201503181737CPPJIT.json, st201503181459GO.json, st201503130615GO.json, st201504140750CPPJIT.json, st201503130243GO.json, st201503130411GO.json, st201503122316GO.json, st201504240140CPPJIT.json, st201503181306GO.json, st201503170433PYTHON.json, st201505051004PYTHON.json, st201504020428JS.json, st201503130747GO.json, st201503181439GO.json, st201504062033CPPJIT.json, st201503181722GO.json, st201505051016PYTHON.json, st201503181653GO.json, st201503181638GO.json, st201503181655GO.json, st201506071050GO.json, st201506101359JS.json, st201504012359JS.json, st201504081957JAVA.json, st201504080457CPPJIT.json, st201503181531CPPJIT.json, st201503131658GO.json, st201503181605GO.json, st201503181540PYTHON.json, st201504021237GO.json, st201503181837GO.json, st201503181358GO.json, st201503181706GO.json, st201503181802GO.json, st201503181709GO.json, st201503130101GO.json, st201503181539GO.json, st201503181536GO.json, st201503181316CPPJIT.json, st201503181330GO.json, st201503181347PYTHON.json, st201503181801GO.json, st201503181609GO.json, st201503181630CPPJIT.json, st201503130752PYTHON.json, st201503181227GO.json, st201503181738GO.json, st201503130437GO.json, st201503181440GO.json, st201503151516PYTHON.json, st201503181517CPPJIT.json, st201503130408GO.json, st201503200837JS.json, st201505051710GO.json, st201504140236CPPJIT.json, st201503181319PYTHON.json, st201504081611CPPJIT.json, st201503181652CPPJIT.json, st201503181445CPPJIT.json, st201503181614GO.json, st201503181334GO.json, st201503181656CPPJIT.json, st201504041605JS.json, st201503181337GO.json, st201503170051PYTHON.json, st201503181528PYTHON.json, st201503122124GO.json, st201503181825GO.json, st201504150854CPPJIT.json, st201503181711CPPJIT.json, st201503130010GO.json, st201503181703GO.json, st201503181318GO.json, st201503130156GO.json, st201503181301GO.json, st201503181339GO.json, st201503181900GO.json, st201503122324GO.json, st201506040157GO.json, st201504081953JAVA.json, st201503122140GO.json, st201503181333GO.json, st201504071653CPPJIT.json, st201503181310GO.json, st201503121953GO.json, st201504080948CPPJIT.json, st201505272131CPPJIT.json, st201503181505GO.json, st201503181514CPPJIT.json, st201506080556GO.json, st201503181859GO.json, st201504022124JS.json, st201503181314GO.json, st201503181418CPPJIT.json, st201503150427PYTHON.json, st201503181713GO.json, st201503181323GO.json, st201503181301CPPJIT.json, st201503181257GO.json, st201503130023PYTHON.json, st201504050059JS.json, st201503181250GO.json, st201504080454CPPJIT.json, st201503141144PYTHON.json, st201503181830CPPJIT.json, st201503302211JS.json, st201503181616CPPJIT.json, st201503181915GO.json, st201504231639CPPJIT.json, st201503181528GO.json, st201503181325GO.json, st201504081842JAVA.json, st201503181857PYTHON.json, st201503130007GO.json, st201506060929GO.json, st201503130321GO.json, st201503181524CPPJIT.json, st201503181646GO.json, st201503181654GO.json, st201503181715CPPJIT.json, st201504021949JS.json, st201503181745CPPJIT.json, st201503181509GO.json, st201503181439CPPJIT.json, st201503181326CPPJIT.json, st201503132201CPPJIT.json, st201504140229CPPJIT.json, st201503181809CPPJIT.json, st201506052130GO.json, st201505052235GO.json, st201503122027GO.json, st201503181812CPPJIT.json, st201503181814CPPJIT.json, st201504210957CPPJIT.json, st201503181601CPPJIT.json, st201504091641CPPJIT.json, st201503181346GO.json, st201504240351CPPJIT.json, st201503181313GO.json, st201503181249GO.json, st201503122212GO.json, st201505052013GO.json, stBoundsTest.json, stMemoryStressTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stQuadraticComplexityTest.json, stInitCodeTest.json, stWalletTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, basic_abi_tests.json, ethash_tests.json, invalidRLPTest.json, rlptest.json, example.json, basic_tests.json, keyaddrtest.json, difficulty.json, difficultyHomestead.json, difficultyOlimpic.json, hexencodetest.json, difficultyMorden.json, crypto.json, genesishashestest.json, blockgenesistest.json, difficultyCustomHomestead.json, txtest.json, difficultyFrontier.json, basic_genesis_tests.json, tt10mbDataField.json, ttWrongRLPTransaction.json, tr201506052141PYTHON.json, ttWrongRLPTransaction.json, tt10mbDataField.json, bcUncleHeaderValiditiy.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcForkBlockTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcForkStressTest.json, bcValidBlockTest.json, bcForkUncle.json, bl10251623GO.json, bl201507071825GO.json, bcSimpleTransitionTest.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcValidBlockTest.json, bcUncleHeaderValiditiy.json, bcExploitTest.json, bcForkStressTest.json]
            files: {
               [.gitignore, README.md, TODO, vmInputLimits.json, vmBitwiseLogicOperationTest.json, vmtests.json, vmLogTest.json, vmBlockInfoTest.json, vmArithmeticTest.json, vmSha3Test.json, vmInputLimitsLight.json, 201503120525PYTHON.json, 201503110206PYTHON.json, 201503112218PYTHON.json, 201503110526PYTHON.json, 201503102320PYTHON.json, 201503111844PYTHON.json, 201503120317PYTHON.json, 201503110050PYTHON.json, 201503102300PYTHON.json, 201503102148PYTHON.json, 201503120909PYTHON.json, randomTest.json, 201503110226PYTHON_DUP6.json, 201503120547PYTHON.json, 201503102037PYTHON.json, 201503110219PYTHON.json, 201503110346PYTHON_PUSH24.json, hex_encoded_securetrie_test.json, trieanyorder_secureTrie.json, trieanyorder.json, trietest.json, trietestnextprev.json, trietest_secureTrie.json, stInitCodeTest.json, stRefundTest.json, stMemoryStressTest.json, stTransitionTest.json, stMemoryTest.json, stTransactionTest.json, stCallCodes.json, stWalletTest.json, stBlockHashTest.json, stQuadraticComplexityTest.json, stSolidityTest.json, stCallCreateCallCodeTest.json, stExample.json, stRecursiveCreate.json, stLogTests.json, stSpecialTest.json, st201503181543GO.json, st201503181647CPPJIT.json, st201503130733CPPJIT.json, st201504100125CPPJIT.json, st201504230729CPPJIT.json, st201503181342CPPJIT.json, st201504071905CPPJIT.json, st201503181406CPPJIT.json, st201503140756PYTHON.json, st201504202124CPPJIT.json, st201503181922GO.json, st201503181749GO.json, st201503181441GO.json, st201503181800GO.json, st201503181740GO.json, st201503181241CPPJIT.json, st201503181322GO.json, st201506091836GO.json, st201503181931GO.json, st201503181329CPPJIT.json, st201503122159GO.json, st201503181740CPPJIT.json, st201503132127PYTHON.json, st201503181544CPPJIT.json, st201504240817CPPJIT.json, st201503151450PYTHON.json, st201503181341CPPJIT.json, st201503181410GO.json, st201503181850GO.json, st201504070746JS.json, st201503181723GO.json, st201503181250CPPJIT.json, st201503181656GO.json, st201503181848GO.json, st201503130405GO.json, st201504140818CPPJIT.json, st201503181821GO.json, st201503181239GO.json, st201503181318CPPJIT.json, st201503181630GO.json, st201503181559GO.json, st201503181225GO.json, st201503170523PYTHON.json, st201504210245CPPJIT.json, st201503191646GO.json, st201503181620GO.json, st201504062314CPPJIT.json, st201503181735GO.json, st201504240220CPPJIT.json, st201503181311GO.json, st201503181354CPPJIT.json, st201503181223GO.json, st201503181506CPPJIT.json, st201503181834GO.json, st201503302210JS.json, st201503181634CPPJIT.json, st201503181723CPPJIT.json, st201503181849GO.json, st201504061134CPPJIT.json, st201504080840CPPJIT.json, st201503181854GO.json, st201503181714GO.json, st201503122238GO.json, st201503181315GO.json, st201503181226CPPJIT.json, st201503181500GO.json, st201503181750CPPJIT.json, st201505052242PYTHON.json, st201503181847GO.json, st201504011916JS.json, st201503181248GO.json, st201503140240PYTHON.json, st201504130653JS.json, st201503181702GO.json, st201503181548CPPJIT.json, st201503130332GO.json, st201503181355GO.json, st201504022003CPPJIT.json, st201504060057CPPJIT.json, st201504020305JS.json, st201504021237JS.json, st201504090657CPPJIT.json, st201504101338CPPJIT.json, st201503181626CPPJIT.json, st201504011535GO.json, st201503181358CPPJIT.json, st201504101150CPPJIT.json, st201503181237GO.json, st201503181252CPPJIT.json, st201503181347CPPJIT.json, st201506040034GO.json, st201503151753PYTHON.json, st201503181227CPPJIT.json, st201504030709JS.json, st201503122128PYTHON.json, st201503181629GO.json, st201503181538GO.json, st201503181450GO.json, st201505052343PYTHON.json, st201504051944CPPJIT.json, st201505051249GO.json, st201506092032GO.json, st201503181641GO.json, st201504090553CPPJIT.json, st201503181759GO.json, st201503181339CPPJIT.json, st201503181423CPPJIT.json, st201503181815GO.json, st201503130450GO.json, st201503181437CPPJIT.json, st201503181553GO.json, st201503240609JS.json, st201503181812GO.json, st201504011536GO.json, st201503181232CPPJIT.json, st201503181756GO.json, st201503181803GO.json, st201504020538JS.json, st201503181619GO.json, st201503130117GO.json, st201503181406GO.json, st201503132001CPPJIT.json, st201503181519GO.json, st201503132202PYTHON.json, st201503181608GO.json, st201503181904GO.json, st201504081134CPPJIT.json, st201503181308GO.json, st201503181359GO.json, st201503181536CPPJIT.json, st201503122252GO.json, st201503181354GO.json, st201503130156PYTHON.json, st201503181533GO.json, st201503121850GO.json, st201503171108PYTHON.json, st201503181435GO.json, st201504211739CPPJIT.json, st201503181338GO.json, st201503140002PYTHON.json, st201504052014GO.json, st201503181929GO.json, st201504082002JAVA.json, st201504081841JAVA.json, st201503181734CPPJIT.json, st201503200841JS.json, st201504212038CPPJIT.json, st201503181907GO.json, st201503181447GO.json, st201503160733PYTHON.json, st201506080721GO.json, st201503181833GO.json, st201504020431JS.json, st201503181527GO.json, st201503181417GO.json, st201503181455GO.json, st201503181834CPPJIT.json, st201503181246GO.json, st201504101223CPPJIT.json, st201503181843GO.json, st201504071041CPPJIT.json, st201503181424GO.json, st201503130751GO.json, st201504030646JS.json, st201503181728GO.json, st201503122358GO.json, st201503181822GO.json, st201503181519CPPJIT.json, st201503181757GO.json, st201503130219GO.json, st201503181757CPPJIT.json, st201503181241GO.json, st201503130122GO.json, st201503181430CPPJIT.json, st201504071056CPPJIT.json, st201503181753CPPJIT.json, st201503181233GO.json, st201503181803CPPJIT.json, st201503140522PYTHON.json, st201505050942PYTHON.json, st201503181326GO.json, st201504140359CPPJIT.json, st201505052102JS.json, st201503130757PYTHON.json, st201505252314CPPJIT.json, st201504100226PYTHON.json, st201503200838JS.json, st201505060121GO.json, st201503181245CPPJIT.json, st201503181458GO.json, st201503181823GO.json, st201503181920GO.json, st201503131739GO.json, st201503181747GO.json, st201503181307GO.json, st201503181657GO.json, st201503181816CPPJIT.json, st201503302202JS.json, st201503302206JS.json, st201503181840GO.json, st201504042226CPPJIT.json, st201504052031CPPJIT.json, st201503181438GO.json, st201503181626GO.json, st201503181817CPPJIT.json, st201507030359GO.json, st201503181742CPPJIT.json, st201503122054GO.json, st201503181446GO.json, st201503130322GO.json, st201503181235CPPJIT.json, st201503181522GO.json, st201503181428GO.json, st201503122231GO.json, st201503181251GO.json, st201503181552CPPJIT.json, st201503141510PYTHON.json, st201503181245GO.json, st201503121848GO.json, st201503181356CPPJIT.json, st201504021237PYTHON.json, st201504031446JS.json, st201503152057PYTHON.json, st201503181845GO.json, st201503181342GO.json, st201503181611CPPJIT.json, st201503181618GO.json, st201503122115CPPJIT.json, st201504031133JS.json, st201505051648JS.json, st201503181309GO.json, st201503181608CPPJIT.json, st201503181650GO.json, st201503181627GO.json, st201503181436GO.json, st201504111554CPPJIT.json, st201503181230GO.json, st201505051611PYTHON.json, st201503181919CPPJIT.json, st201503181602GO.json, st201503181610GO.json, st201504020400JS.json, st201503130207GO.json, st201504052008CPPJIT.json, st201505051238GO.json, st201504100337CPPJIT.json, st201503181504GO.json, st201503181503GO.json, st201503181612GO.json, st201503181606GO.json, st201503181336CPPJIT.json, st201503181323CPPJIT.json, st201503181731CPPJIT.json, st201503181453GO.json, st201503181620CPPJIT.json, st201503181347GO.json, st201503181819GO.json, st201503181537GO.json, st201503181317GO.json, st201503122204GO.json, st201503181451CPPJIT.json, st201503181416GO.json, st201503181415GO.json, st201504232350CPPJIT.json, st201504060418CPPJIT.json, st201503181804GO.json, st201503181903GO.json, st201503181417CPPJIT.json, st201503181711GO.json, st201503181526GO.json, st201503122023GO.json, st201503181403GO.json, st201504100215CPPJIT.json, st201503181246CPPJIT.json, st201503181852CPPJIT.json, st201503181632GO.json, st201503181350CPPJIT.json, st201503122115GO.json, st201503181730GO.json, st201503181906GO.json, st201504081955JAVA.json, st201503181303GO.json, st201503181509CPPJIT.json, st201503181829GO.json, st201503181258CPPJIT.json, st201503181639CPPJIT.json, st201503181601GO.json, st201503130005GO.json, st201503181319GO.json, st201503181307CPPJIT.json, st201503181737GO.json, st201503181304GO.json, st201503131755GO.json, st201503181501GO.json, st201503130512CPPJIT.json, st201503181255GO.json, st201503181621GO.json, st201503150716PYTHON.json, st201503181316PYTHON.json, st201505060646JS.json, st201503181842GO.json, st201503181438CPPJIT.json, st201503132201GO.json, st201503181604GO.json, st201503181725GO.json, st201503181645GO.json, st201506062331GO.json, st201503181931CPPJIT.json, st201503181329GO.json, st201503181655CPPJIT.json, st201504020639JS.json, st201503181649CPPJIT.json, st201503181235GO.json, st201503181412CPPJIT.json, st201503181724CPPJIT.json, st201503181426CPPJIT.json, st201503152241PYTHON.json, st201503121806PYTHON.json, st201504070816CPPJIT.json, st201503181544GO.json, st201503181514GO.json, st201503181439PYTHON.json, st201504231710CPPJIT.json, st201504080650CPPJIT.json, st201503121803PYTHON.json, st201504092303CPPJIT.json, st201503181724GO.json, st201504020836JS.json, st201503181255CPPJIT.json, st201503181658GO.json, st201503302208JS.json, st201503181603GO.json, st201503181402CPPJIT.json, st201503181513CPPJIT.json, st201503121851GO.json, st201503181557GO.json, st201505052238JS.json, st201504081956JAVA.json, st201503181229GO.json, st201503130219CPPJIT.json, st201506061255GO.json, st201503181635GO.json, st201503181628GO.json, st201504061106CPPJIT.json, st201504231742CPPJIT.json, st201503181234GO.json, st201504031841JS.json, st201503181704GO.json, st201504082001JAVA.json, st201503181607GO.json, st201503181540CPPJIT.json, st201503130431GO.json, st201504101009CPPJIT.json, st201503181636GO.json, st201503181808GO.json, st201503181511GO.json, st201503181717GO.json, st201504131821CPPJIT.json, st201504081100CPPJIT.json, st201503181910GO.json, st201503181524GO.json, st201503181529GO.json, st201503181743GO.json, st201503160014PYTHON.json, st201503181340GO.json, st201503181617GO.json, st201504101754PYTHON.json, st201503181534GO.json, st201504021057JS.json, st201503181625GO.json, st201504070836CPPJIT.json, st201503181457GO.json, st201503181534CPPJIT.json, st201503181851GO.json, st201503181851CPPJIT.json, st201503181548GO.json, st201503181716GO.json, st201503181611GO.json, st201504012259JS.json, st201503181547GO.json, st201503181614CPPJIT.json, st201504020444JS.json, st201503181413GO.json, st201503131755CPPJIT.json, st201503181931PYTHON.json, st201503130002GO.json, st201503181528CPPJIT.json, st201506071819GO.json, st201503181715GO.json, st201503130059GO.json, st201503302200JS.json, st201503181520GO.json, st201503181243GO.json, st201503181754GO.json, st201503181555CPPJIT.json, st201503181846GO.json, st201503181327GO.json, st201503181512GO.json, st201503181353GO.json, st201505021810CPPJIT.json, st201504051540JS.json, st201506072007GO.json, st201503181744GO.json, st201503181610CPPJIT.json, st201504021237CPPJIT.json, st201503181926GO.json, st201503181919PYTHON.json, st201503181806GO.json, st201503181739GO.json, st201504011547GO.json, st201505051114GO.json, st201504021104JS.json, st201503181456CPPJIT.json, st201503181352GO.json, st201505060120GO.json, st201503130109GO.json, st201503181507GO.json, st201504042355CPPJIT.json, st201503181510GO.json, st201503130512GO.json, st201503181232GO.json, st201504050733JS.json, st201503181824GO.json, st201504071750CPPJIT.json, st201503181844GO.json, st201503181517GO.json, st201503181720CPPJIT.json, st201504070839CPPJIT.json, st201503181630PYTHON.json, st201505050929GO.json, st201504140900CPPJIT.json, st201503181234CPPJIT.json, st201504100308CPPJIT.json, st201503181520CPPJIT.json, st201503122023PYTHON.json, st201503130246GO.json, st201503181616GO.json, st201503181703CPPJIT.json, st201503181752GO.json, st201503181754CPPJIT.json, st201504030138JS.json, st201504151057CPPJIT.json, st201503181253GO.json, st201504071621CPPJIT.json, st201504081954JAVA.json, st201503181437GO.json, st201503181315CPPJIT.json, st201504100341CPPJIT.json, st201503200848JS.json, st201503130359GO.json, st201503122123GO.json, st201503181713CPPJIT.json, st201503181521GO.json, st201503181230CPPJIT.json, st201503181750GO.json, st201505050557JS.json, st201505051558PYTHON.json, st201503181357CPPJIT.json, st201503181422GO.json, st201503181746GO.json, st201503181426GO.json, st201504020910JS.json, st201503181729GO.json, st201506070548GO.json, st201506071624GO.json, st201503181244GO.json, st201503181748GO.json, st201503181345GO.json, st201504042052JS.json, st201503181755GO.json, st201503181700GO.json, st201504091403CPPJIT.json, st201504081843JAVA.json, st201504081138CPPJIT.json, st201503181247GO.json, st201503181324GO.json, st201503130733GO.json, st201503121849GO.json, st201503122055GO.json, st201503130705GO.json, st201503181258GO.json, st201503181332GO.json, st201503181555GO.json, st201503181734GO.json, st201504081928CPPJIT.json, st201503181855CPPJIT.json, st201503181755CPPJIT.json, st201503181231GO.json, st201504012130JS.json, st201503181236GO.json, st201503181738CPPJIT.json, st201504082000JAVA.json, st201505060136PYTHON.json, st201504062046CPPJIT.json, st201503181513GO.json, st201503181442GO.json, st201503181551GO.json, st201503181305GO.json, st201503181732GO.json, st201504241118CPPJIT.json, st201503181737CPPJIT.json, st201503181459GO.json, st201503130615GO.json, st201504140750CPPJIT.json, st201503130243GO.json, st201503130411GO.json, st201503122316GO.json, st201504240140CPPJIT.json, st201503181306GO.json, st201503170433PYTHON.json, st201505051004PYTHON.json, st201504020428JS.json, st201503130747GO.json, st201503181439GO.json, st201504062033CPPJIT.json, st201503181722GO.json, st201505051016PYTHON.json, st201503181653GO.json, st201503181638GO.json, st201503181655GO.json, st201506071050GO.json, st201506101359JS.json, st201504012359JS.json, st201504081957JAVA.json, st201504080457CPPJIT.json, st201503181531CPPJIT.json, st201503131658GO.json, st201503181605GO.json, st201503181540PYTHON.json, st201504021237GO.json, st201503181837GO.json, st201503181358GO.json, st201503181706GO.json, st201503181802GO.json, st201503181709GO.json, st201503130101GO.json, st201503181539GO.json, st201503181536GO.json, st201503181316CPPJIT.json, st201503181330GO.json, st201503181347PYTHON.json, st201503181801GO.json, st201503181609GO.json, st201503181630CPPJIT.json, st201503130752PYTHON.json, st201503181227GO.json, st201503181738GO.json, st201503130437GO.json, st201503181440GO.json, st201503151516PYTHON.json, st201503181517CPPJIT.json, st201503130408GO.json, st201503200837JS.json, st201505051710GO.json, st201504140236CPPJIT.json, st201503181319PYTHON.json, st201504081611CPPJIT.json, st201503181652CPPJIT.json, st201503181445CPPJIT.json, st201503181614GO.json, st201503181334GO.json, st201503181656CPPJIT.json, st201504041605JS.json, st201503181337GO.json, st201503170051PYTHON.json, st201503181528PYTHON.json, st201503122124GO.json, st201503181825GO.json, st201504150854CPPJIT.json, st201503181711CPPJIT.json, st201503130010GO.json, st201503181703GO.json, st201503181318GO.json, st201503130156GO.json, st201503181301GO.json, st201503181339GO.json, st201503181900GO.json, st201503122324GO.json, st201506040157GO.json, st201504081953JAVA.json, st201503122140GO.json, st201503181333GO.json, st201504071653CPPJIT.json, st201503181310GO.json, st201503121953GO.json, st201504080948CPPJIT.json, st201505272131CPPJIT.json, st201503181505GO.json, st201503181514CPPJIT.json, st201506080556GO.json, st201503181859GO.json, st201504022124JS.json, st201503181314GO.json, st201503181418CPPJIT.json, st201503150427PYTHON.json, st201503181713GO.json, st201503181323GO.json, st201503181301CPPJIT.json, st201503181257GO.json, st201503130023PYTHON.json, st201504050059JS.json, st201503181250GO.json, st201504080454CPPJIT.json, st201503141144PYTHON.json, st201503181830CPPJIT.json, st201503302211JS.json, st201503181616CPPJIT.json, st201503181915GO.json, st201504231639CPPJIT.json, st201503181528GO.json, st201503181325GO.json, st201504081842JAVA.json, st201503181857PYTHON.json, st201503130007GO.json, st201506060929GO.json, st201503130321GO.json, st201503181524CPPJIT.json, st201503181646GO.json, st201503181654GO.json, st201503181715CPPJIT.json, st201504021949JS.json, st201503181745CPPJIT.json, st201503181509GO.json, st201503181439CPPJIT.json, st201503181326CPPJIT.json, st201503132201CPPJIT.json, st201504140229CPPJIT.json, st201503181809CPPJIT.json, st201506052130GO.json, st201505052235GO.json, st201503122027GO.json, st201503181812CPPJIT.json, st201503181814CPPJIT.json, st201504210957CPPJIT.json, st201503181601CPPJIT.json, st201504091641CPPJIT.json, st201503181346GO.json, st201504240351CPPJIT.json, st201503181313GO.json, st201503181249GO.json, st201503122212GO.json, st201505052013GO.json, stBoundsTest.json, stMemoryStressTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stQuadraticComplexityTest.json, stInitCodeTest.json, stWalletTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, basic_abi_tests.json, ethash_tests.json, invalidRLPTest.json, rlptest.json, example.json, basic_tests.json, keyaddrtest.json, difficulty.json, difficultyHomestead.json, difficultyOlimpic.json, hexencodetest.json, difficultyMorden.json, crypto.json, genesishashestest.json, blockgenesistest.json, difficultyCustomHomestead.json, txtest.json, difficultyFrontier.json, basic_genesis_tests.json, tt10mbDataField.json, ttWrongRLPTransaction.json, tr201506052141PYTHON.json, ttWrongRLPTransaction.json, tt10mbDataField.json, bcUncleHeaderValiditiy.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcForkBlockTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcForkStressTest.json, bcValidBlockTest.json, bcForkUncle.json, bl10251623GO.json, bl201507071825GO.json, bcSimpleTransitionTest.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcValidBlockTest.json, bcUncleHeaderValiditiy.json, bcExploitTest.json, bcForkStressTest.json]
               VMTests: {
                  [vmInputLimits.json, vmBitwiseLogicOperationTest.json, vmtests.json, vmLogTest.json, vmBlockInfoTest.json, vmArithmeticTest.json, vmSha3Test.json, vmInputLimitsLight.json, 201503120525PYTHON.json, 201503110206PYTHON.json, 201503112218PYTHON.json, 201503110526PYTHON.json, 201503102320PYTHON.json, 201503111844PYTHON.json, 201503120317PYTHON.json, 201503110050PYTHON.json, 201503102300PYTHON.json, 201503102148PYTHON.json, 201503120909PYTHON.json, randomTest.json, 201503110226PYTHON_DUP6.json, 201503120547PYTHON.json, 201503102037PYTHON.json, 201503110219PYTHON.json, 201503110346PYTHON_PUSH24.json]
                  RandomTests: {
                     [201503120525PYTHON.json, 201503110206PYTHON.json, 201503112218PYTHON.json, 201503110526PYTHON.json, 201503102320PYTHON.json, 201503111844PYTHON.json, 201503120317PYTHON.json, 201503110050PYTHON.json, 201503102300PYTHON.json, 201503102148PYTHON.json, 201503120909PYTHON.json, randomTest.json, 201503110226PYTHON_DUP6.json, 201503120547PYTHON.json, 201503102037PYTHON.json, 201503110219PYTHON.json, 201503110346PYTHON_PUSH24.json]
                  }
               }
               TrieTests: {
                  [hex_encoded_securetrie_test.json, trieanyorder_secureTrie.json, trieanyorder.json, trietest.json, trietestnextprev.json, trietest_secureTrie.json]
               }
               StateTests: {
                  [stInitCodeTest.json, stRefundTest.json, stMemoryStressTest.json, stTransitionTest.json, stMemoryTest.json, stTransactionTest.json, stCallCodes.json, stWalletTest.json, stBlockHashTest.json, stQuadraticComplexityTest.json, stSolidityTest.json, stCallCreateCallCodeTest.json, stExample.json, stRecursiveCreate.json, stLogTests.json, stSpecialTest.json, st201503181543GO.json, st201503181647CPPJIT.json, st201503130733CPPJIT.json, st201504100125CPPJIT.json, st201504230729CPPJIT.json, st201503181342CPPJIT.json, st201504071905CPPJIT.json, st201503181406CPPJIT.json, st201503140756PYTHON.json, st201504202124CPPJIT.json, st201503181922GO.json, st201503181749GO.json, st201503181441GO.json, st201503181800GO.json, st201503181740GO.json, st201503181241CPPJIT.json, st201503181322GO.json, st201506091836GO.json, st201503181931GO.json, st201503181329CPPJIT.json, st201503122159GO.json, st201503181740CPPJIT.json, st201503132127PYTHON.json, st201503181544CPPJIT.json, st201504240817CPPJIT.json, st201503151450PYTHON.json, st201503181341CPPJIT.json, st201503181410GO.json, st201503181850GO.json, st201504070746JS.json, st201503181723GO.json, st201503181250CPPJIT.json, st201503181656GO.json, st201503181848GO.json, st201503130405GO.json, st201504140818CPPJIT.json, st201503181821GO.json, st201503181239GO.json, st201503181318CPPJIT.json, st201503181630GO.json, st201503181559GO.json, st201503181225GO.json, st201503170523PYTHON.json, st201504210245CPPJIT.json, st201503191646GO.json, st201503181620GO.json, st201504062314CPPJIT.json, st201503181735GO.json, st201504240220CPPJIT.json, st201503181311GO.json, st201503181354CPPJIT.json, st201503181223GO.json, st201503181506CPPJIT.json, st201503181834GO.json, st201503302210JS.json, st201503181634CPPJIT.json, st201503181723CPPJIT.json, st201503181849GO.json, st201504061134CPPJIT.json, st201504080840CPPJIT.json, st201503181854GO.json, st201503181714GO.json, st201503122238GO.json, st201503181315GO.json, st201503181226CPPJIT.json, st201503181500GO.json, st201503181750CPPJIT.json, st201505052242PYTHON.json, st201503181847GO.json, st201504011916JS.json, st201503181248GO.json, st201503140240PYTHON.json, st201504130653JS.json, st201503181702GO.json, st201503181548CPPJIT.json, st201503130332GO.json, st201503181355GO.json, st201504022003CPPJIT.json, st201504060057CPPJIT.json, st201504020305JS.json, st201504021237JS.json, st201504090657CPPJIT.json, st201504101338CPPJIT.json, st201503181626CPPJIT.json, st201504011535GO.json, st201503181358CPPJIT.json, st201504101150CPPJIT.json, st201503181237GO.json, st201503181252CPPJIT.json, st201503181347CPPJIT.json, st201506040034GO.json, st201503151753PYTHON.json, st201503181227CPPJIT.json, st201504030709JS.json, st201503122128PYTHON.json, st201503181629GO.json, st201503181538GO.json, st201503181450GO.json, st201505052343PYTHON.json, st201504051944CPPJIT.json, st201505051249GO.json, st201506092032GO.json, st201503181641GO.json, st201504090553CPPJIT.json, st201503181759GO.json, st201503181339CPPJIT.json, st201503181423CPPJIT.json, st201503181815GO.json, st201503130450GO.json, st201503181437CPPJIT.json, st201503181553GO.json, st201503240609JS.json, st201503181812GO.json, st201504011536GO.json, st201503181232CPPJIT.json, st201503181756GO.json, st201503181803GO.json, st201504020538JS.json, st201503181619GO.json, st201503130117GO.json, st201503181406GO.json, st201503132001CPPJIT.json, st201503181519GO.json, st201503132202PYTHON.json, st201503181608GO.json, st201503181904GO.json, st201504081134CPPJIT.json, st201503181308GO.json, st201503181359GO.json, st201503181536CPPJIT.json, st201503122252GO.json, st201503181354GO.json, st201503130156PYTHON.json, st201503181533GO.json, st201503121850GO.json, st201503171108PYTHON.json, st201503181435GO.json, st201504211739CPPJIT.json, st201503181338GO.json, st201503140002PYTHON.json, st201504052014GO.json, st201503181929GO.json, st201504082002JAVA.json, st201504081841JAVA.json, st201503181734CPPJIT.json, st201503200841JS.json, st201504212038CPPJIT.json, st201503181907GO.json, st201503181447GO.json, st201503160733PYTHON.json, st201506080721GO.json, st201503181833GO.json, st201504020431JS.json, st201503181527GO.json, st201503181417GO.json, st201503181455GO.json, st201503181834CPPJIT.json, st201503181246GO.json, st201504101223CPPJIT.json, st201503181843GO.json, st201504071041CPPJIT.json, st201503181424GO.json, st201503130751GO.json, st201504030646JS.json, st201503181728GO.json, st201503122358GO.json, st201503181822GO.json, st201503181519CPPJIT.json, st201503181757GO.json, st201503130219GO.json, st201503181757CPPJIT.json, st201503181241GO.json, st201503130122GO.json, st201503181430CPPJIT.json, st201504071056CPPJIT.json, st201503181753CPPJIT.json, st201503181233GO.json, st201503181803CPPJIT.json, st201503140522PYTHON.json, st201505050942PYTHON.json, st201503181326GO.json, st201504140359CPPJIT.json, st201505052102JS.json, st201503130757PYTHON.json, st201505252314CPPJIT.json, st201504100226PYTHON.json, st201503200838JS.json, st201505060121GO.json, st201503181245CPPJIT.json, st201503181458GO.json, st201503181823GO.json, st201503181920GO.json, st201503131739GO.json, st201503181747GO.json, st201503181307GO.json, st201503181657GO.json, st201503181816CPPJIT.json, st201503302202JS.json, st201503302206JS.json, st201503181840GO.json, st201504042226CPPJIT.json, st201504052031CPPJIT.json, st201503181438GO.json, st201503181626GO.json, st201503181817CPPJIT.json, st201507030359GO.json, st201503181742CPPJIT.json, st201503122054GO.json, st201503181446GO.json, st201503130322GO.json, st201503181235CPPJIT.json, st201503181522GO.json, st201503181428GO.json, st201503122231GO.json, st201503181251GO.json, st201503181552CPPJIT.json, st201503141510PYTHON.json, st201503181245GO.json, st201503121848GO.json, st201503181356CPPJIT.json, st201504021237PYTHON.json, st201504031446JS.json, st201503152057PYTHON.json, st201503181845GO.json, st201503181342GO.json, st201503181611CPPJIT.json, st201503181618GO.json, st201503122115CPPJIT.json, st201504031133JS.json, st201505051648JS.json, st201503181309GO.json, st201503181608CPPJIT.json, st201503181650GO.json, st201503181627GO.json, st201503181436GO.json, st201504111554CPPJIT.json, st201503181230GO.json, st201505051611PYTHON.json, st201503181919CPPJIT.json, st201503181602GO.json, st201503181610GO.json, st201504020400JS.json, st201503130207GO.json, st201504052008CPPJIT.json, st201505051238GO.json, st201504100337CPPJIT.json, st201503181504GO.json, st201503181503GO.json, st201503181612GO.json, st201503181606GO.json, st201503181336CPPJIT.json, st201503181323CPPJIT.json, st201503181731CPPJIT.json, st201503181453GO.json, st201503181620CPPJIT.json, st201503181347GO.json, st201503181819GO.json, st201503181537GO.json, st201503181317GO.json, st201503122204GO.json, st201503181451CPPJIT.json, st201503181416GO.json, st201503181415GO.json, st201504232350CPPJIT.json, st201504060418CPPJIT.json, st201503181804GO.json, st201503181903GO.json, st201503181417CPPJIT.json, st201503181711GO.json, st201503181526GO.json, st201503122023GO.json, st201503181403GO.json, st201504100215CPPJIT.json, st201503181246CPPJIT.json, st201503181852CPPJIT.json, st201503181632GO.json, st201503181350CPPJIT.json, st201503122115GO.json, st201503181730GO.json, st201503181906GO.json, st201504081955JAVA.json, st201503181303GO.json, st201503181509CPPJIT.json, st201503181829GO.json, st201503181258CPPJIT.json, st201503181639CPPJIT.json, st201503181601GO.json, st201503130005GO.json, st201503181319GO.json, st201503181307CPPJIT.json, st201503181737GO.json, st201503181304GO.json, st201503131755GO.json, st201503181501GO.json, st201503130512CPPJIT.json, st201503181255GO.json, st201503181621GO.json, st201503150716PYTHON.json, st201503181316PYTHON.json, st201505060646JS.json, st201503181842GO.json, st201503181438CPPJIT.json, st201503132201GO.json, st201503181604GO.json, st201503181725GO.json, st201503181645GO.json, st201506062331GO.json, st201503181931CPPJIT.json, st201503181329GO.json, st201503181655CPPJIT.json, st201504020639JS.json, st201503181649CPPJIT.json, st201503181235GO.json, st201503181412CPPJIT.json, st201503181724CPPJIT.json, st201503181426CPPJIT.json, st201503152241PYTHON.json, st201503121806PYTHON.json, st201504070816CPPJIT.json, st201503181544GO.json, st201503181514GO.json, st201503181439PYTHON.json, st201504231710CPPJIT.json, st201504080650CPPJIT.json, st201503121803PYTHON.json, st201504092303CPPJIT.json, st201503181724GO.json, st201504020836JS.json, st201503181255CPPJIT.json, st201503181658GO.json, st201503302208JS.json, st201503181603GO.json, st201503181402CPPJIT.json, st201503181513CPPJIT.json, st201503121851GO.json, st201503181557GO.json, st201505052238JS.json, st201504081956JAVA.json, st201503181229GO.json, st201503130219CPPJIT.json, st201506061255GO.json, st201503181635GO.json, st201503181628GO.json, st201504061106CPPJIT.json, st201504231742CPPJIT.json, st201503181234GO.json, st201504031841JS.json, st201503181704GO.json, st201504082001JAVA.json, st201503181607GO.json, st201503181540CPPJIT.json, st201503130431GO.json, st201504101009CPPJIT.json, st201503181636GO.json, st201503181808GO.json, st201503181511GO.json, st201503181717GO.json, st201504131821CPPJIT.json, st201504081100CPPJIT.json, st201503181910GO.json, st201503181524GO.json, st201503181529GO.json, st201503181743GO.json, st201503160014PYTHON.json, st201503181340GO.json, st201503181617GO.json, st201504101754PYTHON.json, st201503181534GO.json, st201504021057JS.json, st201503181625GO.json, st201504070836CPPJIT.json, st201503181457GO.json, st201503181534CPPJIT.json, st201503181851GO.json, st201503181851CPPJIT.json, st201503181548GO.json, st201503181716GO.json, st201503181611GO.json, st201504012259JS.json, st201503181547GO.json, st201503181614CPPJIT.json, st201504020444JS.json, st201503181413GO.json, st201503131755CPPJIT.json, st201503181931PYTHON.json, st201503130002GO.json, st201503181528CPPJIT.json, st201506071819GO.json, st201503181715GO.json, st201503130059GO.json, st201503302200JS.json, st201503181520GO.json, st201503181243GO.json, st201503181754GO.json, st201503181555CPPJIT.json, st201503181846GO.json, st201503181327GO.json, st201503181512GO.json, st201503181353GO.json, st201505021810CPPJIT.json, st201504051540JS.json, st201506072007GO.json, st201503181744GO.json, st201503181610CPPJIT.json, st201504021237CPPJIT.json, st201503181926GO.json, st201503181919PYTHON.json, st201503181806GO.json, st201503181739GO.json, st201504011547GO.json, st201505051114GO.json, st201504021104JS.json, st201503181456CPPJIT.json, st201503181352GO.json, st201505060120GO.json, st201503130109GO.json, st201503181507GO.json, st201504042355CPPJIT.json, st201503181510GO.json, st201503130512GO.json, st201503181232GO.json, st201504050733JS.json, st201503181824GO.json, st201504071750CPPJIT.json, st201503181844GO.json, st201503181517GO.json, st201503181720CPPJIT.json, st201504070839CPPJIT.json, st201503181630PYTHON.json, st201505050929GO.json, st201504140900CPPJIT.json, st201503181234CPPJIT.json, st201504100308CPPJIT.json, st201503181520CPPJIT.json, st201503122023PYTHON.json, st201503130246GO.json, st201503181616GO.json, st201503181703CPPJIT.json, st201503181752GO.json, st201503181754CPPJIT.json, st201504030138JS.json, st201504151057CPPJIT.json, st201503181253GO.json, st201504071621CPPJIT.json, st201504081954JAVA.json, st201503181437GO.json, st201503181315CPPJIT.json, st201504100341CPPJIT.json, st201503200848JS.json, st201503130359GO.json, st201503122123GO.json, st201503181713CPPJIT.json, st201503181521GO.json, st201503181230CPPJIT.json, st201503181750GO.json, st201505050557JS.json, st201505051558PYTHON.json, st201503181357CPPJIT.json, st201503181422GO.json, st201503181746GO.json, st201503181426GO.json, st201504020910JS.json, st201503181729GO.json, st201506070548GO.json, st201506071624GO.json, st201503181244GO.json, st201503181748GO.json, st201503181345GO.json, st201504042052JS.json, st201503181755GO.json, st201503181700GO.json, st201504091403CPPJIT.json, st201504081843JAVA.json, st201504081138CPPJIT.json, st201503181247GO.json, st201503181324GO.json, st201503130733GO.json, st201503121849GO.json, st201503122055GO.json, st201503130705GO.json, st201503181258GO.json, st201503181332GO.json, st201503181555GO.json, st201503181734GO.json, st201504081928CPPJIT.json, st201503181855CPPJIT.json, st201503181755CPPJIT.json, st201503181231GO.json, st201504012130JS.json, st201503181236GO.json, st201503181738CPPJIT.json, st201504082000JAVA.json, st201505060136PYTHON.json, st201504062046CPPJIT.json, st201503181513GO.json, st201503181442GO.json, st201503181551GO.json, st201503181305GO.json, st201503181732GO.json, st201504241118CPPJIT.json, st201503181737CPPJIT.json, st201503181459GO.json, st201503130615GO.json, st201504140750CPPJIT.json, st201503130243GO.json, st201503130411GO.json, st201503122316GO.json, st201504240140CPPJIT.json, st201503181306GO.json, st201503170433PYTHON.json, st201505051004PYTHON.json, st201504020428JS.json, st201503130747GO.json, st201503181439GO.json, st201504062033CPPJIT.json, st201503181722GO.json, st201505051016PYTHON.json, st201503181653GO.json, st201503181638GO.json, st201503181655GO.json, st201506071050GO.json, st201506101359JS.json, st201504012359JS.json, st201504081957JAVA.json, st201504080457CPPJIT.json, st201503181531CPPJIT.json, st201503131658GO.json, st201503181605GO.json, st201503181540PYTHON.json, st201504021237GO.json, st201503181837GO.json, st201503181358GO.json, st201503181706GO.json, st201503181802GO.json, st201503181709GO.json, st201503130101GO.json, st201503181539GO.json, st201503181536GO.json, st201503181316CPPJIT.json, st201503181330GO.json, st201503181347PYTHON.json, st201503181801GO.json, st201503181609GO.json, st201503181630CPPJIT.json, st201503130752PYTHON.json, st201503181227GO.json, st201503181738GO.json, st201503130437GO.json, st201503181440GO.json, st201503151516PYTHON.json, st201503181517CPPJIT.json, st201503130408GO.json, st201503200837JS.json, st201505051710GO.json, st201504140236CPPJIT.json, st201503181319PYTHON.json, st201504081611CPPJIT.json, st201503181652CPPJIT.json, st201503181445CPPJIT.json, st201503181614GO.json, st201503181334GO.json, st201503181656CPPJIT.json, st201504041605JS.json, st201503181337GO.json, st201503170051PYTHON.json, st201503181528PYTHON.json, st201503122124GO.json, st201503181825GO.json, st201504150854CPPJIT.json, st201503181711CPPJIT.json, st201503130010GO.json, st201503181703GO.json, st201503181318GO.json, st201503130156GO.json, st201503181301GO.json, st201503181339GO.json, st201503181900GO.json, st201503122324GO.json, st201506040157GO.json, st201504081953JAVA.json, st201503122140GO.json, st201503181333GO.json, st201504071653CPPJIT.json, st201503181310GO.json, st201503121953GO.json, st201504080948CPPJIT.json, st201505272131CPPJIT.json, st201503181505GO.json, st201503181514CPPJIT.json, st201506080556GO.json, st201503181859GO.json, st201504022124JS.json, st201503181314GO.json, st201503181418CPPJIT.json, st201503150427PYTHON.json, st201503181713GO.json, st201503181323GO.json, st201503181301CPPJIT.json, st201503181257GO.json, st201503130023PYTHON.json, st201504050059JS.json, st201503181250GO.json, st201504080454CPPJIT.json, st201503141144PYTHON.json, st201503181830CPPJIT.json, st201503302211JS.json, st201503181616CPPJIT.json, st201503181915GO.json, st201504231639CPPJIT.json, st201503181528GO.json, st201503181325GO.json, st201504081842JAVA.json, st201503181857PYTHON.json, st201503130007GO.json, st201506060929GO.json, st201503130321GO.json, st201503181524CPPJIT.json, st201503181646GO.json, st201503181654GO.json, st201503181715CPPJIT.json, st201504021949JS.json, st201503181745CPPJIT.json, st201503181509GO.json, st201503181439CPPJIT.json, st201503181326CPPJIT.json, st201503132201CPPJIT.json, st201504140229CPPJIT.json, st201503181809CPPJIT.json, st201506052130GO.json, st201505052235GO.json, st201503122027GO.json, st201503181812CPPJIT.json, st201503181814CPPJIT.json, st201504210957CPPJIT.json, st201503181601CPPJIT.json, st201504091641CPPJIT.json, st201503181346GO.json, st201504240351CPPJIT.json, st201503181313GO.json, st201503181249GO.json, st201503122212GO.json, st201505052013GO.json, stBoundsTest.json, stMemoryStressTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stQuadraticComplexityTest.json, stInitCodeTest.json, stWalletTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json]
                  RandomTests: {
                     [st201503181543GO.json, st201503181647CPPJIT.json, st201503130733CPPJIT.json, st201504100125CPPJIT.json, st201504230729CPPJIT.json, st201503181342CPPJIT.json, st201504071905CPPJIT.json, st201503181406CPPJIT.json, st201503140756PYTHON.json, st201504202124CPPJIT.json, st201503181922GO.json, st201503181749GO.json, st201503181441GO.json, st201503181800GO.json, st201503181740GO.json, st201503181241CPPJIT.json, st201503181322GO.json, st201506091836GO.json, st201503181931GO.json, st201503181329CPPJIT.json, st201503122159GO.json, st201503181740CPPJIT.json, st201503132127PYTHON.json, st201503181544CPPJIT.json, st201504240817CPPJIT.json, st201503151450PYTHON.json, st201503181341CPPJIT.json, st201503181410GO.json, st201503181850GO.json, st201504070746JS.json, st201503181723GO.json, st201503181250CPPJIT.json, st201503181656GO.json, st201503181848GO.json, st201503130405GO.json, st201504140818CPPJIT.json, st201503181821GO.json, st201503181239GO.json, st201503181318CPPJIT.json, st201503181630GO.json, st201503181559GO.json, st201503181225GO.json, st201503170523PYTHON.json, st201504210245CPPJIT.json, st201503191646GO.json, st201503181620GO.json, st201504062314CPPJIT.json, st201503181735GO.json, st201504240220CPPJIT.json, st201503181311GO.json, st201503181354CPPJIT.json, st201503181223GO.json, st201503181506CPPJIT.json, st201503181834GO.json, st201503302210JS.json, st201503181634CPPJIT.json, st201503181723CPPJIT.json, st201503181849GO.json, st201504061134CPPJIT.json, st201504080840CPPJIT.json, st201503181854GO.json, st201503181714GO.json, st201503122238GO.json, st201503181315GO.json, st201503181226CPPJIT.json, st201503181500GO.json, st201503181750CPPJIT.json, st201505052242PYTHON.json, st201503181847GO.json, st201504011916JS.json, st201503181248GO.json, st201503140240PYTHON.json, st201504130653JS.json, st201503181702GO.json, st201503181548CPPJIT.json, st201503130332GO.json, st201503181355GO.json, st201504022003CPPJIT.json, st201504060057CPPJIT.json, st201504020305JS.json, st201504021237JS.json, st201504090657CPPJIT.json, st201504101338CPPJIT.json, st201503181626CPPJIT.json, st201504011535GO.json, st201503181358CPPJIT.json, st201504101150CPPJIT.json, st201503181237GO.json, st201503181252CPPJIT.json, st201503181347CPPJIT.json, st201506040034GO.json, st201503151753PYTHON.json, st201503181227CPPJIT.json, st201504030709JS.json, st201503122128PYTHON.json, st201503181629GO.json, st201503181538GO.json, st201503181450GO.json, st201505052343PYTHON.json, st201504051944CPPJIT.json, st201505051249GO.json, st201506092032GO.json, st201503181641GO.json, st201504090553CPPJIT.json, st201503181759GO.json, st201503181339CPPJIT.json, st201503181423CPPJIT.json, st201503181815GO.json, st201503130450GO.json, st201503181437CPPJIT.json, st201503181553GO.json, st201503240609JS.json, st201503181812GO.json, st201504011536GO.json, st201503181232CPPJIT.json, st201503181756GO.json, st201503181803GO.json, st201504020538JS.json, st201503181619GO.json, st201503130117GO.json, st201503181406GO.json, st201503132001CPPJIT.json, st201503181519GO.json, st201503132202PYTHON.json, st201503181608GO.json, st201503181904GO.json, st201504081134CPPJIT.json, st201503181308GO.json, st201503181359GO.json, st201503181536CPPJIT.json, st201503122252GO.json, st201503181354GO.json, st201503130156PYTHON.json, st201503181533GO.json, st201503121850GO.json, st201503171108PYTHON.json, st201503181435GO.json, st201504211739CPPJIT.json, st201503181338GO.json, st201503140002PYTHON.json, st201504052014GO.json, st201503181929GO.json, st201504082002JAVA.json, st201504081841JAVA.json, st201503181734CPPJIT.json, st201503200841JS.json, st201504212038CPPJIT.json, st201503181907GO.json, st201503181447GO.json, st201503160733PYTHON.json, st201506080721GO.json, st201503181833GO.json, st201504020431JS.json, st201503181527GO.json, st201503181417GO.json, st201503181455GO.json, st201503181834CPPJIT.json, st201503181246GO.json, st201504101223CPPJIT.json, st201503181843GO.json, st201504071041CPPJIT.json, st201503181424GO.json, st201503130751GO.json, st201504030646JS.json, st201503181728GO.json, st201503122358GO.json, st201503181822GO.json, st201503181519CPPJIT.json, st201503181757GO.json, st201503130219GO.json, st201503181757CPPJIT.json, st201503181241GO.json, st201503130122GO.json, st201503181430CPPJIT.json, st201504071056CPPJIT.json, st201503181753CPPJIT.json, st201503181233GO.json, st201503181803CPPJIT.json, st201503140522PYTHON.json, st201505050942PYTHON.json, st201503181326GO.json, st201504140359CPPJIT.json, st201505052102JS.json, st201503130757PYTHON.json, st201505252314CPPJIT.json, st201504100226PYTHON.json, st201503200838JS.json, st201505060121GO.json, st201503181245CPPJIT.json, st201503181458GO.json, st201503181823GO.json, st201503181920GO.json, st201503131739GO.json, st201503181747GO.json, st201503181307GO.json, st201503181657GO.json, st201503181816CPPJIT.json, st201503302202JS.json, st201503302206JS.json, st201503181840GO.json, st201504042226CPPJIT.json, st201504052031CPPJIT.json, st201503181438GO.json, st201503181626GO.json, st201503181817CPPJIT.json, st201507030359GO.json, st201503181742CPPJIT.json, st201503122054GO.json, st201503181446GO.json, st201503130322GO.json, st201503181235CPPJIT.json, st201503181522GO.json, st201503181428GO.json, st201503122231GO.json, st201503181251GO.json, st201503181552CPPJIT.json, st201503141510PYTHON.json, st201503181245GO.json, st201503121848GO.json, st201503181356CPPJIT.json, st201504021237PYTHON.json, st201504031446JS.json, st201503152057PYTHON.json, st201503181845GO.json, st201503181342GO.json, st201503181611CPPJIT.json, st201503181618GO.json, st201503122115CPPJIT.json, st201504031133JS.json, st201505051648JS.json, st201503181309GO.json, st201503181608CPPJIT.json, st201503181650GO.json, st201503181627GO.json, st201503181436GO.json, st201504111554CPPJIT.json, st201503181230GO.json, st201505051611PYTHON.json, st201503181919CPPJIT.json, st201503181602GO.json, st201503181610GO.json, st201504020400JS.json, st201503130207GO.json, st201504052008CPPJIT.json, st201505051238GO.json, st201504100337CPPJIT.json, st201503181504GO.json, st201503181503GO.json, st201503181612GO.json, st201503181606GO.json, st201503181336CPPJIT.json, st201503181323CPPJIT.json, st201503181731CPPJIT.json, st201503181453GO.json, st201503181620CPPJIT.json, st201503181347GO.json, st201503181819GO.json, st201503181537GO.json, st201503181317GO.json, st201503122204GO.json, st201503181451CPPJIT.json, st201503181416GO.json, st201503181415GO.json, st201504232350CPPJIT.json, st201504060418CPPJIT.json, st201503181804GO.json, st201503181903GO.json, st201503181417CPPJIT.json, st201503181711GO.json, st201503181526GO.json, st201503122023GO.json, st201503181403GO.json, st201504100215CPPJIT.json, st201503181246CPPJIT.json, st201503181852CPPJIT.json, st201503181632GO.json, st201503181350CPPJIT.json, st201503122115GO.json, st201503181730GO.json, st201503181906GO.json, st201504081955JAVA.json, st201503181303GO.json, st201503181509CPPJIT.json, st201503181829GO.json, st201503181258CPPJIT.json, st201503181639CPPJIT.json, st201503181601GO.json, st201503130005GO.json, st201503181319GO.json, st201503181307CPPJIT.json, st201503181737GO.json, st201503181304GO.json, st201503131755GO.json, st201503181501GO.json, st201503130512CPPJIT.json, st201503181255GO.json, st201503181621GO.json, st201503150716PYTHON.json, st201503181316PYTHON.json, st201505060646JS.json, st201503181842GO.json, st201503181438CPPJIT.json, st201503132201GO.json, st201503181604GO.json, st201503181725GO.json, st201503181645GO.json, st201506062331GO.json, st201503181931CPPJIT.json, st201503181329GO.json, st201503181655CPPJIT.json, st201504020639JS.json, st201503181649CPPJIT.json, st201503181235GO.json, st201503181412CPPJIT.json, st201503181724CPPJIT.json, st201503181426CPPJIT.json, st201503152241PYTHON.json, st201503121806PYTHON.json, st201504070816CPPJIT.json, st201503181544GO.json, st201503181514GO.json, st201503181439PYTHON.json, st201504231710CPPJIT.json, st201504080650CPPJIT.json, st201503121803PYTHON.json, st201504092303CPPJIT.json, st201503181724GO.json, st201504020836JS.json, st201503181255CPPJIT.json, st201503181658GO.json, st201503302208JS.json, st201503181603GO.json, st201503181402CPPJIT.json, st201503181513CPPJIT.json, st201503121851GO.json, st201503181557GO.json, st201505052238JS.json, st201504081956JAVA.json, st201503181229GO.json, st201503130219CPPJIT.json, st201506061255GO.json, st201503181635GO.json, st201503181628GO.json, st201504061106CPPJIT.json, st201504231742CPPJIT.json, st201503181234GO.json, st201504031841JS.json, st201503181704GO.json, st201504082001JAVA.json, st201503181607GO.json, st201503181540CPPJIT.json, st201503130431GO.json, st201504101009CPPJIT.json, st201503181636GO.json, st201503181808GO.json, st201503181511GO.json, st201503181717GO.json, st201504131821CPPJIT.json, st201504081100CPPJIT.json, st201503181910GO.json, st201503181524GO.json, st201503181529GO.json, st201503181743GO.json, st201503160014PYTHON.json, st201503181340GO.json, st201503181617GO.json, st201504101754PYTHON.json, st201503181534GO.json, st201504021057JS.json, st201503181625GO.json, st201504070836CPPJIT.json, st201503181457GO.json, st201503181534CPPJIT.json, st201503181851GO.json, st201503181851CPPJIT.json, st201503181548GO.json, st201503181716GO.json, st201503181611GO.json, st201504012259JS.json, st201503181547GO.json, st201503181614CPPJIT.json, st201504020444JS.json, st201503181413GO.json, st201503131755CPPJIT.json, st201503181931PYTHON.json, st201503130002GO.json, st201503181528CPPJIT.json, st201506071819GO.json, st201503181715GO.json, st201503130059GO.json, st201503302200JS.json, st201503181520GO.json, st201503181243GO.json, st201503181754GO.json, st201503181555CPPJIT.json, st201503181846GO.json, st201503181327GO.json, st201503181512GO.json, st201503181353GO.json, st201505021810CPPJIT.json, st201504051540JS.json, st201506072007GO.json, st201503181744GO.json, st201503181610CPPJIT.json, st201504021237CPPJIT.json, st201503181926GO.json, st201503181919PYTHON.json, st201503181806GO.json, st201503181739GO.json, st201504011547GO.json, st201505051114GO.json, st201504021104JS.json, st201503181456CPPJIT.json, st201503181352GO.json, st201505060120GO.json, st201503130109GO.json, st201503181507GO.json, st201504042355CPPJIT.json, st201503181510GO.json, st201503130512GO.json, st201503181232GO.json, st201504050733JS.json, st201503181824GO.json, st201504071750CPPJIT.json, st201503181844GO.json, st201503181517GO.json, st201503181720CPPJIT.json, st201504070839CPPJIT.json, st201503181630PYTHON.json, st201505050929GO.json, st201504140900CPPJIT.json, st201503181234CPPJIT.json, st201504100308CPPJIT.json, st201503181520CPPJIT.json, st201503122023PYTHON.json, st201503130246GO.json, st201503181616GO.json, st201503181703CPPJIT.json, st201503181752GO.json, st201503181754CPPJIT.json, st201504030138JS.json, st201504151057CPPJIT.json, st201503181253GO.json, st201504071621CPPJIT.json, st201504081954JAVA.json, st201503181437GO.json, st201503181315CPPJIT.json, st201504100341CPPJIT.json, st201503200848JS.json, st201503130359GO.json, st201503122123GO.json, st201503181713CPPJIT.json, st201503181521GO.json, st201503181230CPPJIT.json, st201503181750GO.json, st201505050557JS.json, st201505051558PYTHON.json, st201503181357CPPJIT.json, st201503181422GO.json, st201503181746GO.json, st201503181426GO.json, st201504020910JS.json, st201503181729GO.json, st201506070548GO.json, st201506071624GO.json, st201503181244GO.json, st201503181748GO.json, st201503181345GO.json, st201504042052JS.json, st201503181755GO.json, st201503181700GO.json, st201504091403CPPJIT.json, st201504081843JAVA.json, st201504081138CPPJIT.json, st201503181247GO.json, st201503181324GO.json, st201503130733GO.json, st201503121849GO.json, st201503122055GO.json, st201503130705GO.json, st201503181258GO.json, st201503181332GO.json, st201503181555GO.json, st201503181734GO.json, st201504081928CPPJIT.json, st201503181855CPPJIT.json, st201503181755CPPJIT.json, st201503181231GO.json, st201504012130JS.json, st201503181236GO.json, st201503181738CPPJIT.json, st201504082000JAVA.json, st201505060136PYTHON.json, st201504062046CPPJIT.json, st201503181513GO.json, st201503181442GO.json, st201503181551GO.json, st201503181305GO.json, st201503181732GO.json, st201504241118CPPJIT.json, st201503181737CPPJIT.json, st201503181459GO.json, st201503130615GO.json, st201504140750CPPJIT.json, st201503130243GO.json, st201503130411GO.json, st201503122316GO.json, st201504240140CPPJIT.json, st201503181306GO.json, st201503170433PYTHON.json, st201505051004PYTHON.json, st201504020428JS.json, st201503130747GO.json, st201503181439GO.json, st201504062033CPPJIT.json, st201503181722GO.json, st201505051016PYTHON.json, st201503181653GO.json, st201503181638GO.json, st201503181655GO.json, st201506071050GO.json, st201506101359JS.json, st201504012359JS.json, st201504081957JAVA.json, st201504080457CPPJIT.json, st201503181531CPPJIT.json, st201503131658GO.json, st201503181605GO.json, st201503181540PYTHON.json, st201504021237GO.json, st201503181837GO.json, st201503181358GO.json, st201503181706GO.json, st201503181802GO.json, st201503181709GO.json, st201503130101GO.json, st201503181539GO.json, st201503181536GO.json, st201503181316CPPJIT.json, st201503181330GO.json, st201503181347PYTHON.json, st201503181801GO.json, st201503181609GO.json, st201503181630CPPJIT.json, st201503130752PYTHON.json, st201503181227GO.json, st201503181738GO.json, st201503130437GO.json, st201503181440GO.json, st201503151516PYTHON.json, st201503181517CPPJIT.json, st201503130408GO.json, st201503200837JS.json, st201505051710GO.json, st201504140236CPPJIT.json, st201503181319PYTHON.json, st201504081611CPPJIT.json, st201503181652CPPJIT.json, st201503181445CPPJIT.json, st201503181614GO.json, st201503181334GO.json, st201503181656CPPJIT.json, st201504041605JS.json, st201503181337GO.json, st201503170051PYTHON.json, st201503181528PYTHON.json, st201503122124GO.json, st201503181825GO.json, st201504150854CPPJIT.json, st201503181711CPPJIT.json, st201503130010GO.json, st201503181703GO.json, st201503181318GO.json, st201503130156GO.json, st201503181301GO.json, st201503181339GO.json, st201503181900GO.json, st201503122324GO.json, st201506040157GO.json, st201504081953JAVA.json, st201503122140GO.json, st201503181333GO.json, st201504071653CPPJIT.json, st201503181310GO.json, st201503121953GO.json, st201504080948CPPJIT.json, st201505272131CPPJIT.json, st201503181505GO.json, st201503181514CPPJIT.json, st201506080556GO.json, st201503181859GO.json, st201504022124JS.json, st201503181314GO.json, st201503181418CPPJIT.json, st201503150427PYTHON.json, st201503181713GO.json, st201503181323GO.json, st201503181301CPPJIT.json, st201503181257GO.json, st201503130023PYTHON.json, st201504050059JS.json, st201503181250GO.json, st201504080454CPPJIT.json, st201503141144PYTHON.json, st201503181830CPPJIT.json, st201503302211JS.json, st201503181616CPPJIT.json, st201503181915GO.json, st201504231639CPPJIT.json, st201503181528GO.json, st201503181325GO.json, st201504081842JAVA.json, st201503181857PYTHON.json, st201503130007GO.json, st201506060929GO.json, st201503130321GO.json, st201503181524CPPJIT.json, st201503181646GO.json, st201503181654GO.json, st201503181715CPPJIT.json, st201504021949JS.json, st201503181745CPPJIT.json, st201503181509GO.json, st201503181439CPPJIT.json, st201503181326CPPJIT.json, st201503132201CPPJIT.json, st201504140229CPPJIT.json, st201503181809CPPJIT.json, st201506052130GO.json, st201505052235GO.json, st201503122027GO.json, st201503181812CPPJIT.json, st201503181814CPPJIT.json, st201504210957CPPJIT.json, st201503181601CPPJIT.json, st201504091641CPPJIT.json, st201503181346GO.json, st201504240351CPPJIT.json, st201503181313GO.json, st201503181249GO.json, st201503122212GO.json, st201505052013GO.json]
                  }
                  EIP150: {
                     
                     Homestead: {
                        
                     }
                  }
                  Homestead: {
                     [stBoundsTest.json, stMemoryStressTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stQuadraticComplexityTest.json, stInitCodeTest.json, stWalletTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json]
                  }
               }
               ABITests: {
                  [basic_abi_tests.json]
               }
               PoWTests: {
                  [ethash_tests.json]
               }
               RLPTests: {
                  [invalidRLPTest.json, rlptest.json, example.json]
                  RandomRLPTests: {
                     [example.json]
                  }
               }
               KeyStoreTests: {
                  [basic_tests.json]
               }
               BasicTests: {
                  [keyaddrtest.json, difficulty.json, difficultyHomestead.json, difficultyOlimpic.json, hexencodetest.json, difficultyMorden.json, crypto.json, genesishashestest.json, blockgenesistest.json, difficultyCustomHomestead.json, txtest.json, difficultyFrontier.json]
               }
               GenesisTests: {
                  [basic_genesis_tests.json]
               }
               TransactionTests: {
                  [tt10mbDataField.json, ttWrongRLPTransaction.json, tr201506052141PYTHON.json, ttWrongRLPTransaction.json, tt10mbDataField.json]
                  RandomTests: {
                     [tr201506052141PYTHON.json]
                  }
                  Homestead: {
                     [ttWrongRLPTransaction.json, tt10mbDataField.json]
                  }
               }
               BlockchainTests: {
                  [bcUncleHeaderValiditiy.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcForkBlockTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcForkStressTest.json, bcValidBlockTest.json, bcForkUncle.json, bl10251623GO.json, bl201507071825GO.json, bcSimpleTransitionTest.json, bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcValidBlockTest.json, bcUncleHeaderValiditiy.json, bcExploitTest.json, bcForkStressTest.json]
                  RandomTests: {
                     [bl10251623GO.json, bl201507071825GO.json]
                  }
                  TestNetwork: {
                     [bcSimpleTransitionTest.json]
                  }
                  Homestead: {
                     [bcRPC_API_Test.json, bcStateTest.json, bcTotalDifficultyTest.json, bcWalletTest.json, bcBlockGasLimitTest.json, bcInvalidRLPTest.json, bcUncleTest.json, bcGasPricerTest.json, bcMultiChainTest.json, bcValidBlockTest.json, bcUncleHeaderValiditiy.json, bcExploitTest.json, bcForkStressTest.json]
                  }
               }
            }
         }
         vendor: {
            [LICENSE, .gitignore, goupnp.go, service_client.go, device.go, internetgateway1.go, internetgateway2.go, httpu.go, serve.go, ssdp.go, scpd.go, soap.go, types.go, result.go, cmpl_parse.go, builtin_regexp.go, type_date.go, LICENSE, builtin_string.go, value_primitive.go, cmpl_evaluate_expression.go, Makefile, cmpl_evaluate_statement.go, builtin_error.go, builtin_math.go, object_class.go, evaluate.go, dbg.go, cmpl_evaluate.go, otto.go, builtin_number.go, type_go_slice.go, value_number.go, type_string.go, DESIGN.markdown, type_arguments.go, .gitignore, type_array.go, type_go_map.go, builtin_function.go, runtime.go, type_number.go, builtin.go, inline.go, error.go, inline.pl, type_go_array.go, global.go, builtin_array.go, README.markdown, type_error.go, builtin_object.go, type_boolean.go, builtin_boolean.go, otto_.go, value_string.go, object.go, cmpl.go, type_function.go, scope.go, value.go, property.go, script.go, builtin_json.go, stash.go, type_regexp.go, clone.go, type_reference.go, console.go, type_go_struct.go, value_boolean.go, builtin_date.go, README.markdown, node.go, comments.go, lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go, dbg.go, README.markdown, tokenfmt, token_const.go, Makefile, token.go, README.markdown, registry.go, README.markdown, file.go, decode_other.go, encode_amd64.s, CONTRIBUTORS, LICENSE, encode_other.go, encode.go, decode_amd64.go, .gitignore, decode.go, decode_amd64.s, encode_amd64.go, AUTHORS, README, snappy.go, runtime_no_gccpufraction.go, LICENSE, syslog.go, .gitignore, timer.go, histogram.go, runtime.go, graphite.go, debug.go, ewma.go, counter.go, writer.go, meter.go, healthcheck.go, runtime_gccpufraction.go, validate.sh, opentsdb.go, metrics.go, README.md, json.go, memory.md, gauge_float64.go, runtime_cgo.go, log.go, runtime_no_cgo.go, .travis.yml, exp.go, LICENSE.md, .travis.yml, notify.go, watchpoint_other.go, watcher_fsevents.go, event_fen.go, watcher_inotify.go, tree_recursive.go, event_trigger.go, watcher_kqueue.go, util.go, event_readdcw.go, watchpoint.go, debug.go, LICENSE, doc.go, .gitignore, watcher_readdcw.go, tree_nonrecursive.go, event_inotify.go, watcher_trigger.go, tree.go, watchpoint_readdcw.go, appveyor.yml, watcher_fsevents_cgo.go, watcher_stub.go, event_fsevents.go, event.go, debug_debug.go, README.md, event_stub.go, event_kqueue.go, node.go, watcher_fen.go, AUTHORS, watcher_fen_cgo.go, .travis.yml, watcher.go, middleware.go, LICENSE, xhandler.go, chain.go, .travis.yml, README.md, cors.go, .travis.yml, README.md, LICENSE, utils.go, LICENSE, 2q.go, .gitignore, arc.go, lru.go, README.md, lru.go, api_common.go, LICENSE, collect_terminfo.py, termbox_common.go, syscalls_netbsd.go, syscalls_darwin.go, syscalls_darwin_amd64.go, terminfo_builtin.go, terminfo.go, syscalls_linux.go, syscalls_dragonfly.go, termbox_windows.go, AUTHORS, api_windows.go, syscalls_windows.go, syscalls_openbsd.go, syscalls_freebsd.go, syscalls.go, LICENSE, mkdocs.yml, .gitignore, README.md, .travis.yml, json.go, CONTRIBUTING.md, version4.go, CONTRIBUTORS, LICENSE, uuid.go, node.go, doc.go, time.go, hash.go, version1.go, .travis.yml, util.go, sql.go, dce.go, LICENSE, recorder.go, natpmp.go, network.go, .travis.yml, README.md, output_windows.go, input_linux.go, output.go, input_darwin.go, fallbackinput.go, bsdinput.go, COPYING, unixmode.go, README.md, .travis.yml, README.md, LICENSE, errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go, ethashc.go, Vagrantfile, ethash.go, Makefile, MANIFEST.in, .gitignore, appveyor.yml, CMakeLists.txt, .travis.yml, setup.py, README.md, sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h, LICENSE, .travis.yml, README.md, LICENSE, isatty_linux.go, doc.go, isatty_solaris.go, isatty_windows.go, isatty_bsd.go, README.md, isatty_appengine.go, runewidth.go, LICENSE, README.mkd, runewidth_posix.go, runewidth_windows.go, .travis.yml, runewidth_js.go, cp.go, LICENSE.txt, README.md, LICENSE.md, README.md, wordwrap.go, test_coverage.txt, cov_report.sh, .gitignore, .travis.yml, set_ts.go, set.go, LICENSE.md, set_nots.go, .travis.yml, README.md, README.md, LICENSE, prque.go, sstack.go, category.go, LICENSE, .gitignore, funcs.go, helpers.go, printer.go, LICENSE, run.go, .gitignore, benchmark.go, reporter.go, TODO, README.md, LICENSE, Makefile, consumer.go, .travis.yml, README.md, base64_vlq.go, znpipe_windows_amd64.go, doc.go, .gitignore, npipe_windows.go, znpipe_windows_386.go, LICENSE.txt, README.md, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, runes.go, cond.go, common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go, encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go, transform.go, tag.go, gen.go, utf8internal.go, makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go, dial.go, client.go, hybi.go, server.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, enclosing.go, util.go, imports.go, zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, pbkdf2.go, ripemd160.go, ripemd160block.go, scrypt.go]
            github.com: {
               [LICENSE, .gitignore, goupnp.go, service_client.go, device.go, internetgateway1.go, internetgateway2.go, httpu.go, serve.go, ssdp.go, scpd.go, soap.go, types.go, result.go, cmpl_parse.go, builtin_regexp.go, type_date.go, LICENSE, builtin_string.go, value_primitive.go, cmpl_evaluate_expression.go, Makefile, cmpl_evaluate_statement.go, builtin_error.go, builtin_math.go, object_class.go, evaluate.go, dbg.go, cmpl_evaluate.go, otto.go, builtin_number.go, type_go_slice.go, value_number.go, type_string.go, DESIGN.markdown, type_arguments.go, .gitignore, type_array.go, type_go_map.go, builtin_function.go, runtime.go, type_number.go, builtin.go, inline.go, error.go, inline.pl, type_go_array.go, global.go, builtin_array.go, README.markdown, type_error.go, builtin_object.go, type_boolean.go, builtin_boolean.go, otto_.go, value_string.go, object.go, cmpl.go, type_function.go, scope.go, value.go, property.go, script.go, builtin_json.go, stash.go, type_regexp.go, clone.go, type_reference.go, console.go, type_go_struct.go, value_boolean.go, builtin_date.go, README.markdown, node.go, comments.go, lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go, dbg.go, README.markdown, tokenfmt, token_const.go, Makefile, token.go, README.markdown, registry.go, README.markdown, file.go, decode_other.go, encode_amd64.s, CONTRIBUTORS, LICENSE, encode_other.go, encode.go, decode_amd64.go, .gitignore, decode.go, decode_amd64.s, encode_amd64.go, AUTHORS, README, snappy.go, runtime_no_gccpufraction.go, LICENSE, syslog.go, .gitignore, timer.go, histogram.go, runtime.go, graphite.go, debug.go, ewma.go, counter.go, writer.go, meter.go, healthcheck.go, runtime_gccpufraction.go, validate.sh, opentsdb.go, metrics.go, README.md, json.go, memory.md, gauge_float64.go, runtime_cgo.go, log.go, runtime_no_cgo.go, .travis.yml, exp.go, LICENSE.md, .travis.yml, notify.go, watchpoint_other.go, watcher_fsevents.go, event_fen.go, watcher_inotify.go, tree_recursive.go, event_trigger.go, watcher_kqueue.go, util.go, event_readdcw.go, watchpoint.go, debug.go, LICENSE, doc.go, .gitignore, watcher_readdcw.go, tree_nonrecursive.go, event_inotify.go, watcher_trigger.go, tree.go, watchpoint_readdcw.go, appveyor.yml, watcher_fsevents_cgo.go, watcher_stub.go, event_fsevents.go, event.go, debug_debug.go, README.md, event_stub.go, event_kqueue.go, node.go, watcher_fen.go, AUTHORS, watcher_fen_cgo.go, .travis.yml, watcher.go, middleware.go, LICENSE, xhandler.go, chain.go, .travis.yml, README.md, cors.go, .travis.yml, README.md, LICENSE, utils.go, LICENSE, 2q.go, .gitignore, arc.go, lru.go, README.md, lru.go, api_common.go, LICENSE, collect_terminfo.py, termbox_common.go, syscalls_netbsd.go, syscalls_darwin.go, syscalls_darwin_amd64.go, terminfo_builtin.go, terminfo.go, syscalls_linux.go, syscalls_dragonfly.go, termbox_windows.go, AUTHORS, api_windows.go, syscalls_windows.go, syscalls_openbsd.go, syscalls_freebsd.go, syscalls.go, LICENSE, mkdocs.yml, .gitignore, README.md, .travis.yml, json.go, CONTRIBUTING.md, version4.go, CONTRIBUTORS, LICENSE, uuid.go, node.go, doc.go, time.go, hash.go, version1.go, .travis.yml, util.go, sql.go, dce.go, LICENSE, recorder.go, natpmp.go, network.go, .travis.yml, README.md, output_windows.go, input_linux.go, output.go, input_darwin.go, fallbackinput.go, bsdinput.go, COPYING, unixmode.go, README.md, .travis.yml, README.md, LICENSE, errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go, ethashc.go, Vagrantfile, ethash.go, Makefile, MANIFEST.in, .gitignore, appveyor.yml, CMakeLists.txt, .travis.yml, setup.py, README.md, sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h, LICENSE, .travis.yml, README.md, LICENSE, isatty_linux.go, doc.go, isatty_solaris.go, isatty_windows.go, isatty_bsd.go, README.md, isatty_appengine.go, runewidth.go, LICENSE, README.mkd, runewidth_posix.go, runewidth_windows.go, .travis.yml, runewidth_js.go, cp.go, LICENSE.txt, README.md, LICENSE.md, README.md, wordwrap.go, test_coverage.txt, cov_report.sh, .gitignore, .travis.yml]
               huin: {
                  [LICENSE, .gitignore, goupnp.go, service_client.go, device.go, internetgateway1.go, internetgateway2.go, httpu.go, serve.go, ssdp.go, scpd.go, soap.go, types.go]
                  goupnp: {
                     [LICENSE, .gitignore, goupnp.go, service_client.go, device.go, internetgateway1.go, internetgateway2.go, httpu.go, serve.go, ssdp.go, scpd.go, soap.go, types.go]
                     dcps: {
                        [internetgateway1.go, internetgateway2.go]
                        internetgateway1: {
                           [internetgateway1.go]
                        }
                        internetgateway2: {
                           [internetgateway2.go]
                        }
                     }
                     httpu: {
                        [httpu.go, serve.go]
                     }
                     ssdp: {
                        [ssdp.go]
                     }
                     scpd: {
                        [scpd.go]
                     }
                     soap: {
                        [soap.go, types.go]
                     }
                  }
               }
               robertkrimen: {
                  [result.go, cmpl_parse.go, builtin_regexp.go, type_date.go, LICENSE, builtin_string.go, value_primitive.go, cmpl_evaluate_expression.go, Makefile, cmpl_evaluate_statement.go, builtin_error.go, builtin_math.go, object_class.go, evaluate.go, dbg.go, cmpl_evaluate.go, otto.go, builtin_number.go, type_go_slice.go, value_number.go, type_string.go, DESIGN.markdown, type_arguments.go, .gitignore, type_array.go, type_go_map.go, builtin_function.go, runtime.go, type_number.go, builtin.go, inline.go, error.go, inline.pl, type_go_array.go, global.go, builtin_array.go, README.markdown, type_error.go, builtin_object.go, type_boolean.go, builtin_boolean.go, otto_.go, value_string.go, object.go, cmpl.go, type_function.go, scope.go, value.go, property.go, script.go, builtin_json.go, stash.go, type_regexp.go, clone.go, type_reference.go, console.go, type_go_struct.go, value_boolean.go, builtin_date.go, README.markdown, node.go, comments.go, lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go, dbg.go, README.markdown, tokenfmt, token_const.go, Makefile, token.go, README.markdown, registry.go, README.markdown, file.go]
                  otto: {
                     [result.go, cmpl_parse.go, builtin_regexp.go, type_date.go, LICENSE, builtin_string.go, value_primitive.go, cmpl_evaluate_expression.go, Makefile, cmpl_evaluate_statement.go, builtin_error.go, builtin_math.go, object_class.go, evaluate.go, dbg.go, cmpl_evaluate.go, otto.go, builtin_number.go, type_go_slice.go, value_number.go, type_string.go, DESIGN.markdown, type_arguments.go, .gitignore, type_array.go, type_go_map.go, builtin_function.go, runtime.go, type_number.go, builtin.go, inline.go, error.go, inline.pl, type_go_array.go, global.go, builtin_array.go, README.markdown, type_error.go, builtin_object.go, type_boolean.go, builtin_boolean.go, otto_.go, value_string.go, object.go, cmpl.go, type_function.go, scope.go, value.go, property.go, script.go, builtin_json.go, stash.go, type_regexp.go, clone.go, type_reference.go, console.go, type_go_struct.go, value_boolean.go, builtin_date.go, README.markdown, node.go, comments.go, lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go, dbg.go, README.markdown, tokenfmt, token_const.go, Makefile, token.go, README.markdown, registry.go, README.markdown, file.go]
                     ast: {
                        [README.markdown, node.go, comments.go]
                     }
                     parser: {
                        [lexer.go, README.markdown, scope.go, error.go, expression.go, Makefile, parser.go, statement.go, regexp.go, dbg.go]
                     }
                     dbg: {
                        [dbg.go]
                     }
                     token: {
                        [README.markdown, tokenfmt, token_const.go, Makefile, token.go]
                     }
                     registry: {
                        [README.markdown, registry.go]
                     }
                     file: {
                        [README.markdown, file.go]
                     }
                  }
               }
               rcrowley: {
                  [runtime_no_gccpufraction.go, LICENSE, syslog.go, .gitignore, timer.go, histogram.go, runtime.go, graphite.go, debug.go, ewma.go, counter.go, writer.go, meter.go, healthcheck.go, runtime_gccpufraction.go, validate.sh, opentsdb.go, metrics.go, README.md, json.go, memory.md, gauge_float64.go, runtime_cgo.go, log.go, runtime_no_cgo.go, .travis.yml, exp.go]
                  go-metrics: {
                     [runtime_no_gccpufraction.go, LICENSE, syslog.go, .gitignore, timer.go, histogram.go, runtime.go, graphite.go, debug.go, ewma.go, counter.go, writer.go, meter.go, healthcheck.go, runtime_gccpufraction.go, validate.sh, opentsdb.go, metrics.go, README.md, json.go, memory.md, gauge_float64.go, runtime_cgo.go, log.go, runtime_no_cgo.go, .travis.yml, exp.go]
                     exp: {
                        [exp.go]
                     }
                  }
               }
               fatih: {
                  [LICENSE.md, .travis.yml]
                  color: {
                     [LICENSE.md, .travis.yml]
                  }
               }
               hashicorp: {
                  [LICENSE, 2q.go, .gitignore, arc.go, lru.go, README.md, lru.go]
                  golang-lru: {
                     [LICENSE, 2q.go, .gitignore, arc.go, lru.go, README.md, lru.go]
                     simplelru: {
                        [lru.go]
                     }
                  }
               }
               pborman: {
                  [json.go, CONTRIBUTING.md, version4.go, CONTRIBUTORS, LICENSE, uuid.go, node.go, doc.go, time.go, hash.go, version1.go, .travis.yml, util.go, sql.go, dce.go]
                  uuid: {
                     [json.go, CONTRIBUTING.md, version4.go, CONTRIBUTORS, LICENSE, uuid.go, node.go, doc.go, time.go, hash.go, version1.go, .travis.yml, util.go, sql.go, dce.go]
                  }
               }
               rs: {
                  [middleware.go, LICENSE, xhandler.go, chain.go, .travis.yml, README.md, cors.go, .travis.yml, README.md, LICENSE, utils.go]
                  xhandler: {
                     [middleware.go, LICENSE, xhandler.go, chain.go, .travis.yml, README.md]
                  }
                  cors: {
                     [cors.go, .travis.yml, README.md, LICENSE, utils.go]
                  }
               }
               rjeczalik: {
                  [notify.go, watchpoint_other.go, watcher_fsevents.go, event_fen.go, watcher_inotify.go, tree_recursive.go, event_trigger.go, watcher_kqueue.go, util.go, event_readdcw.go, watchpoint.go, debug.go, LICENSE, doc.go, .gitignore, watcher_readdcw.go, tree_nonrecursive.go, event_inotify.go, watcher_trigger.go, tree.go, watchpoint_readdcw.go, appveyor.yml, watcher_fsevents_cgo.go, watcher_stub.go, event_fsevents.go, event.go, debug_debug.go, README.md, event_stub.go, event_kqueue.go, node.go, watcher_fen.go, AUTHORS, watcher_fen_cgo.go, .travis.yml, watcher.go]
                  notify: {
                     [notify.go, watchpoint_other.go, watcher_fsevents.go, event_fen.go, watcher_inotify.go, tree_recursive.go, event_trigger.go, watcher_kqueue.go, util.go, event_readdcw.go, watchpoint.go, debug.go, LICENSE, doc.go, .gitignore, watcher_readdcw.go, tree_nonrecursive.go, event_inotify.go, watcher_trigger.go, tree.go, watchpoint_readdcw.go, appveyor.yml, watcher_fsevents_cgo.go, watcher_stub.go, event_fsevents.go, event.go, debug_debug.go, README.md, event_stub.go, event_kqueue.go, node.go, watcher_fen.go, AUTHORS, watcher_fen_cgo.go, .travis.yml, watcher.go]
                  }
               }
               nsf: {
                  [api_common.go, LICENSE, collect_terminfo.py, termbox_common.go, syscalls_netbsd.go, syscalls_darwin.go, syscalls_darwin_amd64.go, terminfo_builtin.go, terminfo.go, syscalls_linux.go, syscalls_dragonfly.go, termbox_windows.go, AUTHORS, api_windows.go, syscalls_windows.go, syscalls_openbsd.go, syscalls_freebsd.go, syscalls.go]
                  termbox-go: {
                     [api_common.go, LICENSE, collect_terminfo.py, termbox_common.go, syscalls_netbsd.go, syscalls_darwin.go, syscalls_darwin_amd64.go, terminfo_builtin.go, terminfo.go, syscalls_linux.go, syscalls_dragonfly.go, termbox_windows.go, AUTHORS, api_windows.go, syscalls_windows.go, syscalls_openbsd.go, syscalls_freebsd.go, syscalls.go]
                  }
               }
               gizak: {
                  [LICENSE, mkdocs.yml, .gitignore, README.md, .travis.yml]
                  termui: {
                     [LICENSE, mkdocs.yml, .gitignore, README.md, .travis.yml]
                  }
               }
               golang: {
                  [decode_other.go, encode_amd64.s, CONTRIBUTORS, LICENSE, encode_other.go, encode.go, decode_amd64.go, .gitignore, decode.go, decode_amd64.s, encode_amd64.go, AUTHORS, README, snappy.go]
                  snappy: {
                     [decode_other.go, encode_amd64.s, CONTRIBUTORS, LICENSE, encode_other.go, encode.go, decode_amd64.go, .gitignore, decode.go, decode_amd64.s, encode_amd64.go, AUTHORS, README, snappy.go]
                  }
               }
               jackpal: {
                  [LICENSE, recorder.go, natpmp.go, network.go, .travis.yml, README.md]
                  go-nat-pmp: {
                     [LICENSE, recorder.go, natpmp.go, network.go, .travis.yml, README.md]
                  }
               }
               peterh: {
                  [output_windows.go, input_linux.go, output.go, input_darwin.go, fallbackinput.go, bsdinput.go, COPYING, unixmode.go, README.md]
                  liner: {
                     [output_windows.go, input_linux.go, output.go, input_darwin.go, fallbackinput.go, bsdinput.go, COPYING, unixmode.go, README.md]
                  }
               }
               syndtr: {
                  [.travis.yml, README.md, LICENSE, errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go]
                  goleveldb: {
                     [.travis.yml, README.md, LICENSE, errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go]
                     leveldb: {
                        [errors.go, db_write.go, db_transaction.go, session_record.go, util.go, db.go, doc.go, filter.go, table.go, db_snapshot.go, session_compaction.go, batch.go, db_util.go, options.go, db_state.go, key.go, db_compaction.go, comparer.go, db_iter.go, options.go, filter.go, bloom.go, errors.go, merged_iter.go, iter.go, array_iter.go, indexed_iter.go, memdb.go, journal.go, lru.go, cache.go, file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go, crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go, comparer.go, bytes_comparer.go, writer.go, table.go, reader.go]
                        opt: {
                           [options.go]
                        }
                        util: {
                           [crc32.go, buffer.go, hash.go, buffer_pool.go, range.go, util.go]
                        }
                        errors: {
                           [errors.go]
                        }
                        iterator: {
                           [merged_iter.go, iter.go, array_iter.go, indexed_iter.go]
                        }
                        memdb: {
                           [memdb.go]
                        }
                        journal: {
                           [journal.go]
                        }
                        cache: {
                           [lru.go, cache.go]
                        }
                        storage: {
                           [file_storage_nacl.go, file_storage_solaris.go, file_storage_unix.go, file_storage.go, file_storage_plan9.go, file_storage_windows.go, storage.go, mem_storage.go]
                        }
                        filter: {
                           [filter.go, bloom.go]
                        }
                        comparer: {
                           [comparer.go, bytes_comparer.go]
                        }
                        table: {
                           [writer.go, table.go, reader.go]
                        }
                     }
                  }
               }
               ethereum: {
                  [ethashc.go, Vagrantfile, ethash.go, Makefile, MANIFEST.in, .gitignore, appveyor.yml, CMakeLists.txt, .travis.yml, setup.py, README.md, sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h]
                  ethash: {
                     [ethashc.go, Vagrantfile, ethash.go, Makefile, MANIFEST.in, .gitignore, appveyor.yml, CMakeLists.txt, .travis.yml, setup.py, README.md, sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h]
                     src: {
                        [sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h]
                        libethash: {
                           [sha3_cryptopp.h, compiler.h, mmap_win32.c, sha3.c, sha3_cryptopp.cpp, ethash.h, data_sizes.h, util.h, io_posix.c, util_win32.c, io.c, sha3.h, io_win32.c, CMakeLists.txt, fnv.h, endian.h, mmap.h, internal.c, io.h, internal.h]
                        }
                     }
                  }
               }
               mattn: {
                  [LICENSE, .travis.yml, README.md, LICENSE, isatty_linux.go, doc.go, isatty_solaris.go, isatty_windows.go, isatty_bsd.go, README.md, isatty_appengine.go, runewidth.go, LICENSE, README.mkd, runewidth_posix.go, runewidth_windows.go, .travis.yml, runewidth_js.go]
                  go-colorable: {
                     [LICENSE, .travis.yml, README.md]
                  }
                  go-isatty: {
                     [LICENSE, isatty_linux.go, doc.go, isatty_solaris.go, isatty_windows.go, isatty_bsd.go, README.md, isatty_appengine.go]
                  }
                  go-runewidth: {
                     [runewidth.go, LICENSE, README.mkd, runewidth_posix.go, runewidth_windows.go, .travis.yml, runewidth_js.go]
                  }
               }
               cespare: {
                  [cp.go, LICENSE.txt, README.md]
                  cp: {
                     [cp.go, LICENSE.txt, README.md]
                  }
               }
               mitchellh: {
                  [LICENSE.md, README.md, wordwrap.go]
                  go-wordwrap: {
                     [LICENSE.md, README.md, wordwrap.go]
                  }
               }
               davecgh: {
                  [test_coverage.txt, cov_report.sh, .gitignore, .travis.yml]
                  go-spew: {
                     [test_coverage.txt, cov_report.sh, .gitignore, .travis.yml]
                     spew: {
                        
                     }
                  }
               }
            }
            gopkg.in: {
               [set_ts.go, set.go, LICENSE.md, set_nots.go, .travis.yml, README.md, README.md, LICENSE, prque.go, sstack.go, category.go, LICENSE, .gitignore, funcs.go, helpers.go, printer.go, LICENSE, run.go, .gitignore, benchmark.go, reporter.go, TODO, README.md, LICENSE, Makefile, consumer.go, .travis.yml, README.md, base64_vlq.go, znpipe_windows_amd64.go, doc.go, .gitignore, npipe_windows.go, znpipe_windows_386.go, LICENSE.txt, README.md]
               fatih: {
                  [set_ts.go, set.go, LICENSE.md, set_nots.go, .travis.yml, README.md]
                  set.v0: {
                     [set_ts.go, set.go, LICENSE.md, set_nots.go, .travis.yml, README.md]
                  }
               }
               karalabe: {
                  [README.md, LICENSE, prque.go, sstack.go]
                  cookiejar.v2: {
                     [README.md, LICENSE, prque.go, sstack.go]
                     collections: {
                        [prque.go, sstack.go]
                        prque: {
                           [prque.go, sstack.go]
                        }
                     }
                  }
               }
               urfave: {
                  [category.go, LICENSE, .gitignore, funcs.go]
                  cli.v1: {
                     [category.go, LICENSE, .gitignore, funcs.go]
                  }
               }
               check.v1: {
                  [helpers.go, printer.go, LICENSE, run.go, .gitignore, benchmark.go, reporter.go, TODO, README.md]
               }
               sourcemap.v1: {
                  [LICENSE, Makefile, consumer.go, .travis.yml, README.md, base64_vlq.go]
                  base64vlq: {
                     [base64_vlq.go]
                  }
               }
               natefinch: {
                  [znpipe_windows_amd64.go, doc.go, .gitignore, npipe_windows.go, znpipe_windows_386.go, LICENSE.txt, README.md]
                  npipe.v2: {
                     [znpipe_windows_amd64.go, doc.go, .gitignore, npipe_windows.go, znpipe_windows_386.go, LICENSE.txt, README.md]
                  }
               }
            }
            golang.org: {
               [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, runes.go, cond.go, common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go, encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go, transform.go, tag.go, gen.go, utf8internal.go, makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go, dial.go, client.go, hybi.go, server.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, enclosing.go, util.go, imports.go, zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, pbkdf2.go, ripemd160.go, ripemd160block.go, scrypt.go]
               x: {
                  [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, runes.go, cond.go, common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go, encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go, transform.go, tag.go, gen.go, utf8internal.go, makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go, dial.go, client.go, hybi.go, server.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, enclosing.go, util.go, imports.go, zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go, CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, pbkdf2.go, ripemd160.go, ripemd160block.go, scrypt.go]
                  sys: {
                     [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go]
                     unix: {
                        [zsysnum_freebsd_arm.go, mkpost.go, zsyscall_darwin_arm64.go, zsyscall_darwin_386.go, asm_darwin_arm64.s, zsyscall_netbsd_386.go, ztypes_openbsd_386.go, syscall_freebsd_amd64.go, zsyscall_freebsd_amd64.go, zsysnum_dragonfly_amd64.go, zsysnum_darwin_arm.go, asm_freebsd_386.s, .gitignore, zsysnum_linux_amd64.go, ztypes_openbsd_amd64.go, mksysnum_dragonfly.pl, asm_openbsd_amd64.s, zsysnum_freebsd_386.go, asm_linux_mips64x.s, asm_freebsd_arm.s, ztypes_freebsd_arm.go, syscall_openbsd_amd64.go, env_unix.go, syscall_darwin_arm.go, zsyscall_netbsd_arm.go, ztypes_darwin_amd64.go, zsysnum_linux_386.go, asm_darwin_amd64.s, types_dragonfly.go, asm.s, zerrors_darwin_386.go, mksysnum_openbsd.pl, zerrors_freebsd_amd64.go, gccgo.go, ztypes_netbsd_amd64.go, race.go, zsysnum_linux_ppc64.go, zsysnum_openbsd_amd64.go, syscall_linux_arm64.go, zsysnum_freebsd_amd64.go, ztypes_netbsd_arm.go, zerrors_openbsd_amd64.go, zsysnum_linux_arm64.go, ztypes_freebsd_amd64.go, zsyscall_openbsd_386.go, race0.go, zsysnum_netbsd_amd64.go, ztypes_solaris_amd64.go, zsysnum_linux_mips64le.go, syscall_netbsd.go, types_netbsd.go, asm_linux_ppc64x.s, asm_linux_386.s, zerrors_netbsd_arm.go, zerrors_netbsd_386.go, zsyscall_freebsd_386.go, mksyscall_solaris.pl, types_darwin.go, syscall_netbsd_386.go, syscall_netbsd_amd64.go, flock.go, syscall_freebsd_arm.go, gccgo_c.c, zerrors_darwin_arm.go, str.go, zsyscall_darwin_arm.go, syscall_linux_sparc64.go, syscall_linux_arm.go, ztypes_darwin_arm64.go, zsysctl_openbsd.go, types_freebsd.go, asm_dragonfly_amd64.s, sockcmsg_linux.go, mksysnum_netbsd.pl, types_openbsd.go, syscall_dragonfly.go, syscall_netbsd_arm.go, zsysnum_linux_mips64.go, ztypes_darwin_arm.go, zsyscall_openbsd_amd64.go, zsysnum_solaris_amd64.go, gccgo_linux_sparc64.go, zsyscall_solaris_amd64.go, syscall.go, mkall.sh, ztypes_netbsd_386.go, asm_netbsd_386.s, syscall_darwin_386.go, zerrors_freebsd_arm.go, asm_linux_arm64.s, zsyscall_freebsd_arm.go, zsyscall_netbsd_amd64.go, asm_netbsd_arm.s, zsysnum_linux_sparc64.go, ztypes_freebsd_386.go, asm_freebsd_amd64.s, mksyscall.pl, zsysnum_linux_s390x.go, zsysnum_openbsd_386.go, zerrors_linux_mips64le.go, zsysnum_darwin_386.go, syscall_freebsd.go, syscall_openbsd_386.go, syscall_darwin_arm64.go, zsysnum_darwin_arm64.go, syscall_no_getwd.go, zsyscall_darwin_amd64.go, asm_linux_s390x.s, zsysnum_linux_ppc64le.go, syscall_darwin_amd64.go, types_solaris.go, zsysnum_netbsd_arm.go, zsysnum_netbsd_386.go, asm_darwin_386.s, zerrors_dragonfly_amd64.go, syscall_linux_mips64x.go, mksysnum_darwin.pl, env_unset.go, syscall_linux_s390x.go, zerrors_freebsd_386.go, zerrors_netbsd_amd64.go, syscall_darwin.go, zsyscall_dragonfly_amd64.go, gccgo_linux_amd64.go, asm_netbsd_amd64.s, zerrors_openbsd_386.go, zsysnum_linux_arm.go, asm_linux_arm.s, sockcmsg_unix.go, asm_darwin_arm.s, zerrors_solaris_amd64.go, zerrors_darwin_amd64.go, zsysnum_darwin_amd64.go, syscall_freebsd_386.go, mksysctl_openbsd.pl, constants.go, asm_solaris_amd64.s, syscall_solaris.go, ztypes_darwin_386.go, ztypes_dragonfly_amd64.go, zerrors_linux_mips64.go, syscall_dragonfly_amd64.go, asm_linux_amd64.s, zerrors_darwin_arm64.go, syscall_linux_386.go, asm_openbsd_386.s, syscall_solaris_amd64.go, syscall_openbsd.go, mksysnum_freebsd.pl, bluetooth_linux.go, syscall_linux_ppc64x.go]
                     }
                  }
                  text: {
                     [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, runes.go, cond.go, common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go, encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go, transform.go, tag.go, gen.go, utf8internal.go, makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go]
                     runes: {
                        [runes.go, cond.go]
                     }
                     language: {
                        [common.go, gen_index.go, index.go, language.go, maketables.go, match.go, lookup.go, Makefile, gen_common.go, go1_2.go, coverage.go, parse.go, tags.go, go1_1.go]
                     }
                     encoding: {
                        [encoding.go, tables.go, charmap.go, maketables.go, tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go, gbk.go, all.go, tables.go, hzgb2312.go, maketables.go, gen.go, tables.go, htmlindex.go, map.go, internal.go, gen.go, identifier.go, mib.go, tables.go, maketables.go, big5.go, override.go, unicode.go, tables.go, maketables.go, euckr.go]
                        charmap: {
                           [tables.go, charmap.go, maketables.go]
                        }
                        japanese: {
                           [tables.go, maketables.go, all.go, shiftjis.go, eucjp.go, iso2022jp.go]
                        }
                        simplifiedchinese: {
                           [gbk.go, all.go, tables.go, hzgb2312.go, maketables.go]
                        }
                        htmlindex: {
                           [gen.go, tables.go, htmlindex.go, map.go]
                        }
                        internal: {
                           [internal.go, gen.go, identifier.go, mib.go]
                           identifier: {
                              [gen.go, identifier.go, mib.go]
                           }
                        }
                        traditionalchinese: {
                           [tables.go, maketables.go, big5.go]
                        }
                        unicode: {
                           [override.go, unicode.go]
                        }
                        korean: {
                           [tables.go, maketables.go, euckr.go]
                        }
                     }
                     transform: {
                        [transform.go]
                     }
                     internal: {
                        [tag.go, gen.go, utf8internal.go]
                        tag: {
                           [tag.go]
                        }
                        gen: {
                           [gen.go]
                        }
                        utf8internal: {
                           [utf8internal.go]
                        }
                     }
                     unicode: {
                        [makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go]
                        cldr: {
                           [makexml.go, resolve.go, collate.go, cldr.go, decode.go, base.go, slice.go, xml.go]
                        }
                     }
                  }
                  net: {
                     [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go, dial.go, client.go, hybi.go, server.go]
                     html: {
                        [doctype.go, render.go, node.go, const.go, foreign.go, doc.go, entity.go, token.go, escape.go, parse.go, charset.go, gen.go, table.go, atom.go]
                        charset: {
                           [charset.go]
                        }
                        atom: {
                           [gen.go, table.go, atom.go]
                        }
                     }
                     websocket: {
                        [dial.go, client.go, hybi.go, server.go]
                     }
                  }
                  tools: {
                     [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, enclosing.go, util.go, imports.go, zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go]
                     go: {
                        [enclosing.go, util.go, imports.go]
                        ast: {
                           [enclosing.go, util.go, imports.go]
                           astutil: {
                              [enclosing.go, util.go, imports.go]
                           }
                        }
                     }
                     imports: {
                        [zstdlib.go, imports.go, mkstdlib.go, sortimports.go, fastwalk_unix.go, fastwalk.go, mkindex.go, fastwalk_dirent_ino.go, fastwalk_portable.go, fastwalk_dirent_fileno.go]
                     }
                  }
                  crypto: {
                     [CONTRIBUTING.md, CONTRIBUTORS, LICENSE, codereview.cfg, .gitignore, AUTHORS, README, .gitattributes, PATENTS, pbkdf2.go, ripemd160.go, ripemd160block.go, scrypt.go]
                     pbkdf2: {
                        [pbkdf2.go]
                     }
                     ripemd160: {
                        [ripemd160.go, ripemd160block.go]
                     }
                     scrypt: {
                        [scrypt.go]
                     }
                  }
               }
            }
         }
         contracts: {
            [api.go, gencode.go, chequebook.sol, code.go, chequebook.go, contract.go, contract_test.go, ens.go, README.md, ens.go, ens.sol]
            chequebook: {
               [api.go, gencode.go, chequebook.sol, code.go, chequebook.go]
               contract: {
                  [chequebook.sol, code.go, chequebook.go]
               }
            }
            release: {
               [contract.go, contract_test.go]
            }
            ens: {
               [ens.go, README.md, ens.go, ens.sol]
               contract: {
                  [ens.go, ens.sol]
               }
            }
         }
         ethdb: {
            [database_test.go, interface.go, .gitignore]
         }
         metrics: {
            [disk_nop.go, disk.go]
         }
         p2p: {
            [rlpx_test.go, message.go, message_test.go, peer.go, peer_error.go, server_test.go, metrics.go, protocol.go, ntp.go, node_test.go, natupnp_test.go, nat.go, natupnp.go]
            discover: {
               [ntp.go, node_test.go]
            }
            nat: {
               [natupnp_test.go, nat.go, natupnp.go]
            }
         }
         .git: {
            [description, exclude, pre-rebase.sample, prepare-commit-msg.sample, post-update.sample, applypatch-msg.sample, update.sample, pre-receive.sample, pre-applypatch.sample, commit-msg.sample, pre-push.sample, pre-commit.sample, HEAD]
            info: {
               [exclude]
            }
            hooks: {
               [pre-rebase.sample, prepare-commit-msg.sample, post-update.sample, applypatch-msg.sample, update.sample, pre-receive.sample, pre-applypatch.sample, commit-msg.sample, pre-push.sample, pre-commit.sample]
            }
            refs: {
               [HEAD]
               remotes: {
                  [HEAD]
                  origin: {
                     [HEAD]
                  }
               }
               heads: {
                  
               }
            }
            objects: {
               
               info: {
                  
               }
               pack: {
                  
               }
            }
            logs: {
               
               refs: {
                  
                  remotes: {
                     
                     origin: {
                        
                     }
                  }
                  heads: {
                     
                  }
               }
            }
         }
         light: {
            
         }
         cmd: {
            [genesis_test.go, run_test.go, guswallet.json, wrong-passwords.txt, passwords.txt, empty.js, fdlimit_windows.go, fdlimit_freebsd.go, customflags_test.go, fdlimit_unix.go, fdlimit_test.go, main.go]
            geth: {
               [genesis_test.go, run_test.go, guswallet.json, wrong-passwords.txt, passwords.txt, empty.js]
               testdata: {
                  [guswallet.json, wrong-passwords.txt, passwords.txt, empty.js]
               }
            }
            abigen: {
               
            }
            bootnode: {
               
            }
            evm: {
               
            }
            utils: {
               [fdlimit_windows.go, fdlimit_freebsd.go, customflags_test.go, fdlimit_unix.go, fdlimit_test.go]
            }
            ethtest: {
               
            }
            disasm: {
               
            }
            rlpdump: {
               [main.go]
            }
            gethrpctest: {
               
            }
         }
         crypto: {
            [encrypt_decrypt_test.go, LICENSE, params.go, .gitignore, README, xor_unaligned.go, sha3.go, LICENSE, shake.go, xor.go, doc.go, xor_generic.go, register.go, keccakf_amd64.s, keccakf.go, keccakf_amd64.go, hashes.go, PATENTS, keccakKats.json.deflate, rand_entropy.go, curve_test.go, .gitignore, panic_cb.go, autogen.sh, COPYING, TODO, scalar_8x32.h, scalar_4x64.h, field_5x52_asm_impl.h, ecmult_const.h, gen_context.c, bench.h, ecmult_gen.h, num_impl.h, bench_sign.c, num_gmp.h, bench_recover.c, basic-config.h, ecmult.h, scalar_8x32_impl.h, field_5x52.h, bench_schnorr_verify.c, field_10x26.h, .gitignore]
            ecies: {
               [LICENSE, params.go, .gitignore, README]
            }
            sha3: {
               [xor_unaligned.go, sha3.go, LICENSE, shake.go, xor.go, doc.go, xor_generic.go, register.go, keccakf_amd64.s, keccakf.go, keccakf_amd64.go, hashes.go, PATENTS, keccakKats.json.deflate]
               testdata: {
                  [keccakKats.json.deflate]
               }
            }
            secp256k1: {
               [curve_test.go, .gitignore, panic_cb.go, autogen.sh, COPYING, TODO, scalar_8x32.h, scalar_4x64.h, field_5x52_asm_impl.h, ecmult_const.h, gen_context.c, bench.h, ecmult_gen.h, num_impl.h, bench_sign.c, num_gmp.h, bench_recover.c, basic-config.h, ecmult.h, scalar_8x32_impl.h, field_5x52.h, bench_schnorr_verify.c, field_10x26.h, .gitignore]
               libsecp256k1: {
                  [autogen.sh, COPYING, TODO, scalar_8x32.h, scalar_4x64.h, field_5x52_asm_impl.h, ecmult_const.h, gen_context.c, bench.h, ecmult_gen.h, num_impl.h, bench_sign.c, num_gmp.h, bench_recover.c, basic-config.h, ecmult.h, scalar_8x32_impl.h, field_5x52.h, bench_schnorr_verify.c, field_10x26.h, .gitignore]
                  src: {
                     [scalar_8x32.h, scalar_4x64.h, field_5x52_asm_impl.h, ecmult_const.h, gen_context.c, bench.h, ecmult_gen.h, num_impl.h, bench_sign.c, num_gmp.h, bench_recover.c, basic-config.h, ecmult.h, scalar_8x32_impl.h, field_5x52.h, bench_schnorr_verify.c, field_10x26.h]
                     java: {
                        
                        org: {
                           
                           bitcoin: {
                              
                           }
                        }
                     }
                     modules: {
                        
                        ecdh: {
                           
                        }
                        recovery: {
                           
                        }
                     }
                  }
                  include: {
                     
                  }
                  obj: {
                     [.gitignore]
                  }
               }
            }
            randentropy: {
               [rand_entropy.go]
            }
         }
         common: {
            [path.go, debug.go, size.go, .gitignore, icap_test.go, test_utils.go, list.go, big.go, size_test.go, README.md, main_test.go, types_template.go, icap.go, .travis.yml, uint_test.go, int.go, dist.go]
            number: {
               [uint_test.go, int.go]
            }
            math: {
               [dist.go]
            }
            compiler: {
               
            }
         }
         eth: {
            [peer.go, metrics.go, fetcher.go, metrics.go, modes.go, events.go, types.go, metrics.go, api.go]
            fetcher: {
               [fetcher.go, metrics.go]
            }
            filters: {
               
            }
            downloader: {
               [modes.go, events.go, types.go, metrics.go, api.go]
            }
         }
         ethclient: {
            
         }
      }

------

IN BOTH, BUT DIFFERENT: 490

      {
         [Makefile, vendor.conf, .gitignore, appveyor.yml, VERSION, README.md, interfaces.go, .mailmap, AUTHORS, .travis.yml, sync.go, hasher.go, trie.go, sync_test.go, encoding.go, iterator_test.go, trie_test.go, message.go, message_test.go, whisper.go, envelope.go, whisper_test.go, benchmarks_test.go, doc.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, topic.go, api_test.go, api.go, envelope_test.go, message_test.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, api.go, subscription.go, json.go, types.go, server.go, subscription_test.go, client.go, argument.go, abi.go, reflect.go, type.go, abi_test.go, event.go, packing.go, auth.go, util_test.go, bind_test.go, template.go, base.go, bind.go, backend.go, simulated.go, errors.go, errors_test.go, event_test.go, event.go, generic_filter.go, console_test.go, prompter.go, console.go, bridge.go, read_write.go, index, HEAD, packed-refs, config, master, HEAD, HEAD, master, CONTRIBUTING.md, ISSUE_TEMPLATE.md, swarm.go, api.go, config_test.go, filesystem.go, manifest.go, config.go, filesystem_test.go, roundtripper.go, roundtripper_test.go, server.go, chunker.go, memstore.go, common_test.go, localstore.go, dbstore.go, dbstore_test.go, dpa.go, types.go, netstore.go, dpa_test.go, syncdb_test.go, depo.go, hive.go, protocol.go, syncer.go, protocol_test.go, kademlia_test.go, web3ext.go, tracer.go, backend.go, tracer_test.go, api.go, pretty.go, jsre.go, archive.go, util.go, env.go, gas_table.go, protocol_params.go, util.go, env.sh, ci.go, ci-notes.md, update-license.go, glog.go, Dockerfile, Dockerfile, Dockerfile, Dockerfile, config_test.go, node.go, node_example_test.go, config.go, node_test.go, api.go, chain_pow_test.go, genesis.go, block_validator_test.go, bench_test.go, tx_pool.go, block_validator.go, dao.go, tx_list.go, chain_makers.go, blocks.go, headerchain.go, blockchain_test.go, events.go, default_genesis.go, tx_pool_test.go, state_processor.go, chain_makers_test.go, types.go, database_util_test.go, tx_list_test.go, database_util.go, blockchain.go, state_transition.go, sync.go, iterator.go, statedb.go, statedb_test.go, sync_test.go, journal.go, iterator_test.go, managed_state_test.go, state_object.go, state_test.go, contracts.go, opcodes.go, errors.go, stack.go, vm.go, vm_jit_fake.go, vm_jit.go, logger_test.go, instructions.go, environment.go, logger.go, jump_table.go, gas.go, contract.go, runtime_test.go, env.go, runtime.go, transaction_test.go, block.go, bloom9.go, receipt.go, block_test.go, transaction.go, init.go, vm_test_util.go, block_test_util.go, transaction_test_util.go, transaction_test.go, vm_test.go, state_test_util.go, block_test.go, util.go, state_test.go, vmIOandFlowOperationsTest.json, vmPerformanceTest.json, vmEnvironmentalInfoTest.json, vmPushDupSwapTest.json, vmSystemOperationsTest.json, stPreCompiledContracts.json, stSystemOperationsTest.json, stMemExpandingEIPCalls.json, stEIPSpecificTest.json, stEIPSingleCodeGasPrices.json, stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, stPreCompiledContracts.json, stTransactionTest.json, stDelegatecallTest.json, stSystemOperationsTest.json, ttTransactionTest.json, ttTransactionTest.json, bcInvalidHeaderTest.json, bcTheDaoTest.json, bcEIP150Test.json, bcShanghaiLove.json, bcSuicideIssue.json, bcInvalidHeaderTest.json, README.md, registry.go, registry.go, sample.go, gauge.go, color.go, doc.go, README.md, termbox.go, README.md, api.go, block_windows.go, block.go, sparkline.go, block_common.go, barchart.go, mbarchart.go, buffer.go, doc.go, theme.go, linechart_others.go, canvas.go, list.go, events.go, linechart_windows.go, grid.go, glide.yaml, helper.go, render.go, textbuilder.go, widget.go, linechart.go, pos.go, par.go, glide.lock, gauge.go, README.md, common.go, input_windows.go, width.go, line.go, input.go, session_util.go, session.go, version.go, colorable_windows.go, colorable_others.go, noncolorable.go, LICENSE, README.md, common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go, app.go, cli.go, flag.go, help.go, runtests, errors.go, CHANGELOG.md, appveyor.yml, command.go, context.go, .travis.yml, README.md, check.go, checkers.go, zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go, tables.go, code.go, websocket.go, fix.go, cheque_test.go, cheque.go, release.go, contract.sol, ens_test.go, memory_database.go, database.go, disk_linux.go, metrics.go, server.go, dial.go, dial_test.go, peer_test.go, rlpx.go, udp_test.go, udp.go, database_test.go, node.go, database.go, table_test.go, table.go, natpmp.go, nat_test.go, odr.go, trie.go, state.go, state_object.go, state_test.go, chaincmd.go, usage.go, consolecmd.go, accountcmd_test.go, main.go, accountcmd.go, consolecmd_test.go, monitorcmd.go, main.go, main.go, main.go, cmd.go, customflags.go, flags.go, main.go, main.go, main.go, crypto_test.go, crypto.go, asn1.go, ecies_test.go, ecies.go, sha3_test.go, secp256.go, secp256_test.go, curve.go, libsecp256k1.pc.in, .gitignore, configure.ac, Makefile.am, .travis.yml, README.md, field_5x52_int128_impl.h, eckey.h, ecmult_const_impl.h, tests.c, field_impl.h, ecdsa_impl.h, hash.h, num_gmp_impl.h, group.h, secp256k1.c, num.h, scalar_impl.h, ecmult_gen_impl.h, eckey_impl.h, hash_impl.h, scalar_4x64_impl.h, ecmult_impl.h, testrand_impl.h, scalar.h, bench_internal.c, bench_verify.c, util.h, testrand.h, field_10x26_impl.h, field_5x52_impl.h, group_impl.h, bench_ecdh.c, field.h, ecdsa.h, tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h, org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java, secp256k1.h, secp256k1_recovery.h, secp256k1_ecdh.h, format.go, types_test.go, bytes_test.go, types.go, bytes.go, big_test.go, dist_test.go, solidity.go, solidity_test.go, sync.go, backend_test.go, helper_test.go, api_backend.go, handler.go, handler_test.go, protocol.go, protocol_test.go, db_upgrade.go, bad_block.go, backend.go, bind.go, api.go, fetcher_test.go, filter_system_test.go, filter.go, filter_test.go, filter_system.go, api.go, api_test.go, downloader_test.go, peer.go, downloader.go, queue.go, ethclient.go, ethclient_test.go]
         trie: {
            [sync.go, hasher.go, trie.go, sync_test.go, encoding.go, iterator_test.go, trie_test.go]
         }
         whisper: {
            [message.go, message_test.go, whisper.go, envelope.go, whisper_test.go, benchmarks_test.go, doc.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, topic.go, api_test.go, api.go, envelope_test.go, message_test.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, api.go]
            whisperv5: {
               [message.go, message_test.go, whisper.go, envelope.go, whisper_test.go, benchmarks_test.go, doc.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, topic.go]
            }
            whisperv2: {
               [envelope_test.go, message_test.go, filter.go, filter_test.go, peer.go, peer_test.go, topic_test.go, api.go]
            }
            shhapi: {
               [api_test.go, api.go]
            }
         }
         rpc: {
            [subscription.go, json.go, types.go, server.go, subscription_test.go, client.go]
         }
         accounts: {
            [argument.go, abi.go, reflect.go, type.go, abi_test.go, event.go, packing.go, auth.go, util_test.go, bind_test.go, template.go, base.go, bind.go, backend.go, simulated.go]
            abi: {
               [argument.go, abi.go, reflect.go, type.go, abi_test.go, event.go, packing.go, auth.go, util_test.go, bind_test.go, template.go, base.go, bind.go, backend.go, simulated.go]
               bind: {
                  [auth.go, util_test.go, bind_test.go, template.go, base.go, bind.go, backend.go, simulated.go]
                  backends: {
                     [simulated.go]
                  }
               }
            }
         }
         errs: {
            [errors.go, errors_test.go]
         }
         event: {
            [event_test.go, event.go, generic_filter.go]
            filter: {
               [generic_filter.go]
            }
         }
         console: {
            [console_test.go, prompter.go, console.go, bridge.go]
            testdata: {
               
            }
         }
         compression: {
            [read_write.go]
            rle: {
               [read_write.go]
            }
         }
         .github: {
            [CONTRIBUTING.md, ISSUE_TEMPLATE.md]
         }
         rlp: {
            
         }
         swarm: {
            [swarm.go, api.go, config_test.go, filesystem.go, manifest.go, config.go, filesystem_test.go, roundtripper.go, roundtripper_test.go, server.go, chunker.go, memstore.go, common_test.go, localstore.go, dbstore.go, dbstore_test.go, dpa.go, types.go, netstore.go, dpa_test.go, syncdb_test.go, depo.go, hive.go, protocol.go, syncer.go, protocol_test.go, kademlia_test.go]
            services: {
               
               swap: {
                  
                  swap: {
                     
                  }
               }
            }
            api: {
               [api.go, config_test.go, filesystem.go, manifest.go, config.go, filesystem_test.go, roundtripper.go, roundtripper_test.go, server.go]
               http: {
                  [roundtripper.go, roundtripper_test.go, server.go]
               }
               testdata: {
                  
                  test0: {
                     
                     img: {
                        
                     }
                  }
               }
            }
            storage: {
               [chunker.go, memstore.go, common_test.go, localstore.go, dbstore.go, dbstore_test.go, dpa.go, types.go, netstore.go, dpa_test.go]
            }
            network: {
               [syncdb_test.go, depo.go, hive.go, protocol.go, syncer.go, protocol_test.go, kademlia_test.go]
               kademlia: {
                  [kademlia_test.go]
               }
            }
         }
         internal: {
            [web3ext.go, tracer.go, backend.go, tracer_test.go, api.go, pretty.go, jsre.go, archive.go, util.go, env.go]
            debug: {
               
            }
            web3ext: {
               [web3ext.go]
            }
            ethapi: {
               [tracer.go, backend.go, tracer_test.go, api.go]
            }
            jsre: {
               [pretty.go, jsre.go]
            }
            build: {
               [archive.go, util.go, env.go]
            }
         }
         params: {
            [gas_table.go, protocol_params.go, util.go]
         }
         build: {
            [env.sh, ci.go, ci-notes.md, update-license.go]
            _vendor: {
               
               src: {
                  
                  golang.org: {
                     
                     x: {
                        
                        net: {
                           
                           context: {
                              
                           }
                        }
                     }
                  }
               }
            }
         }
         pow: {
            
         }
         logger: {
            [glog.go]
            glog: {
               [glog.go]
            }
         }
         containers: {
            [Dockerfile, Dockerfile, Dockerfile, Dockerfile]
            docker: {
               [Dockerfile, Dockerfile, Dockerfile, Dockerfile]
               master-alpine: {
                  [Dockerfile]
               }
               develop-alpine: {
                  [Dockerfile]
               }
               develop-ubuntu: {
                  [Dockerfile]
               }
               master-ubuntu: {
                  [Dockerfile]
               }
            }
            vagrant: {
               
            }
         }
         node: {
            [config_test.go, node.go, node_example_test.go, config.go, node_test.go, api.go]
         }
         core: {
            [chain_pow_test.go, genesis.go, block_validator_test.go, bench_test.go, tx_pool.go, block_validator.go, dao.go, tx_list.go, chain_makers.go, blocks.go, headerchain.go, blockchain_test.go, events.go, default_genesis.go, tx_pool_test.go, state_processor.go, chain_makers_test.go, types.go, database_util_test.go, tx_list_test.go, database_util.go, blockchain.go, state_transition.go, sync.go, iterator.go, statedb.go, statedb_test.go, sync_test.go, journal.go, iterator_test.go, managed_state_test.go, state_object.go, state_test.go, contracts.go, opcodes.go, errors.go, stack.go, vm.go, vm_jit_fake.go, vm_jit.go, logger_test.go, instructions.go, environment.go, logger.go, jump_table.go, gas.go, contract.go, runtime_test.go, env.go, runtime.go, transaction_test.go, block.go, bloom9.go, receipt.go, block_test.go, transaction.go]
            state: {
               [sync.go, iterator.go, statedb.go, statedb_test.go, sync_test.go, journal.go, iterator_test.go, managed_state_test.go, state_object.go, state_test.go]
            }
            vm: {
               [contracts.go, opcodes.go, errors.go, stack.go, vm.go, vm_jit_fake.go, vm_jit.go, logger_test.go, instructions.go, environment.go, logger.go, jump_table.go, gas.go, contract.go, runtime_test.go, env.go, runtime.go]
               runtime: {
                  [runtime_test.go, env.go, runtime.go]
               }
            }
            types: {
               [transaction_test.go, block.go, bloom9.go, receipt.go, block_test.go, transaction.go]
            }
         }
         tests: {
            [init.go, vm_test_util.go, block_test_util.go, transaction_test_util.go, transaction_test.go, vm_test.go, state_test_util.go, block_test.go, util.go, state_test.go, vmIOandFlowOperationsTest.json, vmPerformanceTest.json, vmEnvironmentalInfoTest.json, vmPushDupSwapTest.json, vmSystemOperationsTest.json, stPreCompiledContracts.json, stSystemOperationsTest.json, stMemExpandingEIPCalls.json, stEIPSpecificTest.json, stEIPSingleCodeGasPrices.json, stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, stPreCompiledContracts.json, stTransactionTest.json, stDelegatecallTest.json, stSystemOperationsTest.json, ttTransactionTest.json, ttTransactionTest.json, bcInvalidHeaderTest.json, bcTheDaoTest.json, bcEIP150Test.json, bcShanghaiLove.json, bcSuicideIssue.json, bcInvalidHeaderTest.json]
            files: {
               [vmIOandFlowOperationsTest.json, vmPerformanceTest.json, vmEnvironmentalInfoTest.json, vmPushDupSwapTest.json, vmSystemOperationsTest.json, stPreCompiledContracts.json, stSystemOperationsTest.json, stMemExpandingEIPCalls.json, stEIPSpecificTest.json, stEIPSingleCodeGasPrices.json, stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, stPreCompiledContracts.json, stTransactionTest.json, stDelegatecallTest.json, stSystemOperationsTest.json, ttTransactionTest.json, ttTransactionTest.json, bcInvalidHeaderTest.json, bcTheDaoTest.json, bcEIP150Test.json, bcShanghaiLove.json, bcSuicideIssue.json, bcInvalidHeaderTest.json]
               VMTests: {
                  [vmIOandFlowOperationsTest.json, vmPerformanceTest.json, vmEnvironmentalInfoTest.json, vmPushDupSwapTest.json, vmSystemOperationsTest.json]
                  RandomTests: {
                     
                  }
               }
               TrieTests: {
                  
               }
               StateTests: {
                  [stPreCompiledContracts.json, stSystemOperationsTest.json, stMemExpandingEIPCalls.json, stEIPSpecificTest.json, stEIPSingleCodeGasPrices.json, stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json, stPreCompiledContracts.json, stTransactionTest.json, stDelegatecallTest.json, stSystemOperationsTest.json]
                  RandomTests: {
                     
                  }
                  EIP150: {
                     [stMemExpandingEIPCalls.json, stEIPSpecificTest.json, stEIPSingleCodeGasPrices.json, stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json]
                     Homestead: {
                        [stPreCompiledContracts.json, stBoundsTest.json, stQuadraticComplexityTest.json, stTransactionTest.json, stLogTests.json, stCallCodes.json, stRecursiveCreate.json, stDelegatecallTest.json, stInitCodeTest.json, stWalletTest.json, stSystemOperationsTest.json, stCallCreateCallCodeTest.json, stSpecialTest.json, stMemoryTest.json, stCallDelegateCodes.json, stHomeSteadSpecific.json, stRefundTest.json, stCallDelegateCodesCallCode.json]
                     }
                  }
                  Homestead: {
                     [stPreCompiledContracts.json, stTransactionTest.json, stDelegatecallTest.json, stSystemOperationsTest.json]
                  }
               }
               ABITests: {
                  
               }
               PoWTests: {
                  
               }
               RLPTests: {
                  
                  RandomRLPTests: {
                     
                  }
               }
               KeyStoreTests: {
                  
               }
               BasicTests: {
                  
               }
               GenesisTests: {
                  
               }
               TransactionTests: {
                  [ttTransactionTest.json, ttTransactionTest.json]
                  RandomTests: {
                     
                  }
                  Homestead: {
                     [ttTransactionTest.json]
                  }
               }
               BlockchainTests: {
                  [bcInvalidHeaderTest.json, bcTheDaoTest.json, bcEIP150Test.json, bcShanghaiLove.json, bcSuicideIssue.json, bcInvalidHeaderTest.json]
                  RandomTests: {
                     
                  }
                  TestNetwork: {
                     [bcTheDaoTest.json, bcEIP150Test.json]
                  }
                  Homestead: {
                     [bcShanghaiLove.json, bcSuicideIssue.json, bcInvalidHeaderTest.json]
                  }
               }
            }
         }
         vendor: {
            [README.md, registry.go, registry.go, sample.go, gauge.go, color.go, doc.go, README.md, termbox.go, README.md, api.go, block_windows.go, block.go, sparkline.go, block_common.go, barchart.go, mbarchart.go, buffer.go, doc.go, theme.go, linechart_others.go, canvas.go, list.go, events.go, linechart_windows.go, grid.go, glide.yaml, helper.go, render.go, textbuilder.go, widget.go, linechart.go, pos.go, par.go, glide.lock, gauge.go, README.md, common.go, input_windows.go, width.go, line.go, input.go, session_util.go, session.go, version.go, colorable_windows.go, colorable_others.go, noncolorable.go, LICENSE, README.md, common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go, app.go, cli.go, flag.go, help.go, runtests, errors.go, CHANGELOG.md, appveyor.yml, command.go, context.go, .travis.yml, README.md, check.go, checkers.go, zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go, tables.go, code.go, websocket.go, fix.go]
            github.com: {
               [README.md, registry.go, registry.go, sample.go, gauge.go, color.go, doc.go, README.md, termbox.go, README.md, api.go, block_windows.go, block.go, sparkline.go, block_common.go, barchart.go, mbarchart.go, buffer.go, doc.go, theme.go, linechart_others.go, canvas.go, list.go, events.go, linechart_windows.go, grid.go, glide.yaml, helper.go, render.go, textbuilder.go, widget.go, linechart.go, pos.go, par.go, glide.lock, gauge.go, README.md, common.go, input_windows.go, width.go, line.go, input.go, session_util.go, session.go, version.go, colorable_windows.go, colorable_others.go, noncolorable.go, LICENSE, README.md, common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go]
               huin: {
                  [README.md, registry.go]
                  goupnp: {
                     [README.md, registry.go]
                     dcps: {
                        
                        internetgateway1: {
                           
                        }
                        internetgateway2: {
                           
                        }
                     }
                     httpu: {
                        
                     }
                     ssdp: {
                        [registry.go]
                     }
                     scpd: {
                        
                     }
                     soap: {
                        
                     }
                  }
               }
               robertkrimen: {
                  
                  otto: {
                     
                     ast: {
                        
                     }
                     parser: {
                        
                     }
                     dbg: {
                        
                     }
                     token: {
                        
                     }
                     registry: {
                        
                     }
                     file: {
                        
                     }
                  }
               }
               rcrowley: {
                  [registry.go, sample.go, gauge.go]
                  go-metrics: {
                     [registry.go, sample.go, gauge.go]
                     exp: {
                        
                     }
                  }
               }
               fatih: {
                  [color.go, doc.go, README.md]
                  color: {
                     [color.go, doc.go, README.md]
                  }
               }
               hashicorp: {
                  
                  golang-lru: {
                     
                     simplelru: {
                        
                     }
                  }
               }
               pborman: {
                  [README.md]
                  uuid: {
                     [README.md]
                  }
               }
               rs: {
                  
                  xhandler: {
                     
                  }
                  cors: {
                     
                  }
               }
               rjeczalik: {
                  
                  notify: {
                     
                  }
               }
               nsf: {
                  [termbox.go, README.md, api.go]
                  termbox-go: {
                     [termbox.go, README.md, api.go]
                  }
               }
               gizak: {
                  [block_windows.go, block.go, sparkline.go, block_common.go, barchart.go, mbarchart.go, buffer.go, doc.go, theme.go, linechart_others.go, canvas.go, list.go, events.go, linechart_windows.go, grid.go, glide.yaml, helper.go, render.go, textbuilder.go, widget.go, linechart.go, pos.go, par.go, glide.lock, gauge.go]
                  termui: {
                     [block_windows.go, block.go, sparkline.go, block_common.go, barchart.go, mbarchart.go, buffer.go, doc.go, theme.go, linechart_others.go, canvas.go, list.go, events.go, linechart_windows.go, grid.go, glide.yaml, helper.go, render.go, textbuilder.go, widget.go, linechart.go, pos.go, par.go, glide.lock, gauge.go]
                  }
               }
               golang: {
                  
                  snappy: {
                     
                  }
               }
               jackpal: {
                  
                  go-nat-pmp: {
                     
                  }
               }
               peterh: {
                  [common.go, input_windows.go, width.go, line.go, input.go]
                  liner: {
                     [common.go, input_windows.go, width.go, line.go, input.go]
                  }
               }
               syndtr: {
                  [session_util.go, session.go, version.go]
                  goleveldb: {
                     [session_util.go, session.go, version.go]
                     leveldb: {
                        [session_util.go, session.go, version.go]
                        opt: {
                           
                        }
                        util: {
                           
                        }
                        errors: {
                           
                        }
                        iterator: {
                           
                        }
                        memdb: {
                           
                        }
                        journal: {
                           
                        }
                        cache: {
                           
                        }
                        storage: {
                           
                        }
                        filter: {
                           
                        }
                        comparer: {
                           
                        }
                        table: {
                           
                        }
                     }
                  }
               }
               ethereum: {
                  
                  ethash: {
                     
                     src: {
                        
                        libethash: {
                           
                        }
                     }
                  }
               }
               mattn: {
                  [colorable_windows.go, colorable_others.go, noncolorable.go]
                  go-colorable: {
                     [colorable_windows.go, colorable_others.go, noncolorable.go]
                  }
                  go-isatty: {
                     
                  }
                  go-runewidth: {
                     
                  }
               }
               cespare: {
                  
                  cp: {
                     
                  }
               }
               mitchellh: {
                  
                  go-wordwrap: {
                     
                  }
               }
               davecgh: {
                  [LICENSE, README.md, common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go]
                  go-spew: {
                     [LICENSE, README.md, common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go]
                     spew: {
                        [common.go, format.go, doc.go, bypass.go, config.go, dump.go, bypasssafe.go, spew.go]
                     }
                  }
               }
            }
            gopkg.in: {
               [app.go, cli.go, flag.go, help.go, runtests, errors.go, CHANGELOG.md, appveyor.yml, command.go, context.go, .travis.yml, README.md, check.go, checkers.go]
               fatih: {
                  
                  set.v0: {
                     
                  }
               }
               karalabe: {
                  
                  cookiejar.v2: {
                     
                     collections: {
                        
                        prque: {
                           
                        }
                     }
                  }
               }
               urfave: {
                  [app.go, cli.go, flag.go, help.go, runtests, errors.go, CHANGELOG.md, appveyor.yml, command.go, context.go, .travis.yml, README.md]
                  cli.v1: {
                     [app.go, cli.go, flag.go, help.go, runtests, errors.go, CHANGELOG.md, appveyor.yml, command.go, context.go, .travis.yml, README.md]
                  }
               }
               check.v1: {
                  [check.go, checkers.go]
               }
               sourcemap.v1: {
                  
                  base64vlq: {
                     
                  }
               }
               natefinch: {
                  
                  npipe.v2: {
                     
                  }
               }
            }
            golang.org: {
               [zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go, tables.go, code.go, websocket.go, fix.go]
               x: {
                  [zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go, tables.go, code.go, websocket.go, fix.go]
                  sys: {
                     [zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go]
                     unix: {
                        [zsyscall_linux_ppc64.go, types_linux.go, mksysnum_linux.pl, syscall_linux.go, zsyscall_linux_mips64.go, zerrors_linux_ppc64le.go, mkerrors.sh, zerrors_linux_arm64.go, ztypes_linux_amd64.go, ztypes_linux_mips64le.go, syscall_unix.go, zsyscall_linux_ppc64le.go, zsyscall_linux_386.go, zerrors_linux_sparc64.go, ztypes_linux_ppc64le.go, zsyscall_linux_amd64.go, zerrors_linux_amd64.go, zerrors_linux_s390x.go, ztypes_linux_arm64.go, ztypes_linux_s390x.go, zsyscall_linux_mips64le.go, ztypes_linux_mips64.go, syscall_linux_amd64.go, zerrors_linux_ppc64.go, ztypes_linux_386.go, zsyscall_linux_arm.go, ztypes_linux_ppc64.go, zsyscall_linux_s390x.go, zerrors_linux_386.go, zerrors_linux_arm.go, zsyscall_linux_sparc64.go, zsyscall_linux_arm64.go, flock_linux_32bit.go, ztypes_linux_arm.go, ztypes_linux_sparc64.go, syscall_bsd.go]
                     }
                  }
                  text: {
                     [tables.go, code.go]
                     runes: {
                        
                     }
                     language: {
                        [tables.go]
                     }
                     encoding: {
                        
                        charmap: {
                           
                        }
                        japanese: {
                           
                        }
                        simplifiedchinese: {
                           
                        }
                        htmlindex: {
                           
                        }
                        internal: {
                           
                           identifier: {
                              
                           }
                        }
                        traditionalchinese: {
                           
                        }
                        unicode: {
                           
                        }
                        korean: {
                           
                        }
                     }
                     transform: {
                        
                     }
                     internal: {
                        [code.go]
                        tag: {
                           
                        }
                        gen: {
                           [code.go]
                        }
                        utf8internal: {
                           
                        }
                     }
                     unicode: {
                        
                        cldr: {
                           
                        }
                     }
                  }
                  net: {
                     [websocket.go]
                     html: {
                        
                        charset: {
                           
                        }
                        atom: {
                           
                        }
                     }
                     websocket: {
                        [websocket.go]
                     }
                  }
                  tools: {
                     [fix.go]
                     go: {
                        
                        ast: {
                           
                           astutil: {
                              
                           }
                        }
                     }
                     imports: {
                        [fix.go]
                     }
                  }
                  crypto: {
                     
                     pbkdf2: {
                        
                     }
                     ripemd160: {
                        
                     }
                     scrypt: {
                        
                     }
                  }
               }
            }
         }
         contracts: {
            [cheque_test.go, cheque.go, release.go, contract.sol, ens_test.go]
            chequebook: {
               [cheque_test.go, cheque.go]
               contract: {
                  
               }
            }
            release: {
               [release.go, contract.sol]
            }
            ens: {
               [ens_test.go]
               contract: {
                  
               }
            }
         }
         ethdb: {
            [memory_database.go, database.go]
         }
         metrics: {
            [disk_linux.go, metrics.go]
         }
         p2p: {
            [server.go, dial.go, dial_test.go, peer_test.go, rlpx.go, udp_test.go, udp.go, database_test.go, node.go, database.go, table_test.go, table.go, natpmp.go, nat_test.go]
            discover: {
               [udp_test.go, udp.go, database_test.go, node.go, database.go, table_test.go, table.go]
            }
            nat: {
               [natpmp.go, nat_test.go]
            }
         }
         .git: {
            [index, HEAD, packed-refs, config, master, HEAD, HEAD, master]
            info: {
               
            }
            hooks: {
               
            }
            refs: {
               [master]
               remotes: {
                  
                  origin: {
                     
                  }
               }
               heads: {
                  [master]
               }
            }
            objects: {
               
               info: {
                  
               }
               pack: {
                  
               }
            }
            logs: {
               [HEAD, HEAD, master]
               refs: {
                  [HEAD, master]
                  remotes: {
                     [HEAD]
                     origin: {
                        [HEAD]
                     }
                  }
                  heads: {
                     [master]
                  }
               }
            }
         }
         light: {
            [odr.go, trie.go, state.go, state_object.go, state_test.go]
         }
         cmd: {
            [chaincmd.go, usage.go, consolecmd.go, accountcmd_test.go, main.go, accountcmd.go, consolecmd_test.go, monitorcmd.go, main.go, main.go, main.go, cmd.go, customflags.go, flags.go, main.go, main.go, main.go]
            geth: {
               [chaincmd.go, usage.go, consolecmd.go, accountcmd_test.go, main.go, accountcmd.go, consolecmd_test.go, monitorcmd.go]
               testdata: {
                  
               }
            }
            abigen: {
               [main.go]
            }
            bootnode: {
               [main.go]
            }
            evm: {
               [main.go]
            }
            utils: {
               [cmd.go, customflags.go, flags.go]
            }
            ethtest: {
               [main.go]
            }
            disasm: {
               [main.go]
            }
            rlpdump: {
               
            }
            gethrpctest: {
               [main.go]
            }
         }
         crypto: {
            [crypto_test.go, crypto.go, asn1.go, ecies_test.go, ecies.go, sha3_test.go, secp256.go, secp256_test.go, curve.go, libsecp256k1.pc.in, .gitignore, configure.ac, Makefile.am, .travis.yml, README.md, field_5x52_int128_impl.h, eckey.h, ecmult_const_impl.h, tests.c, field_impl.h, ecdsa_impl.h, hash.h, num_gmp_impl.h, group.h, secp256k1.c, num.h, scalar_impl.h, ecmult_gen_impl.h, eckey_impl.h, hash_impl.h, scalar_4x64_impl.h, ecmult_impl.h, testrand_impl.h, scalar.h, bench_internal.c, bench_verify.c, util.h, testrand.h, field_10x26_impl.h, field_5x52_impl.h, group_impl.h, bench_ecdh.c, field.h, ecdsa.h, tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h, org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java, secp256k1.h, secp256k1_recovery.h, secp256k1_ecdh.h]
            ecies: {
               [asn1.go, ecies_test.go, ecies.go]
            }
            sha3: {
               [sha3_test.go]
               testdata: {
                  
               }
            }
            secp256k1: {
               [secp256.go, secp256_test.go, curve.go, libsecp256k1.pc.in, .gitignore, configure.ac, Makefile.am, .travis.yml, README.md, field_5x52_int128_impl.h, eckey.h, ecmult_const_impl.h, tests.c, field_impl.h, ecdsa_impl.h, hash.h, num_gmp_impl.h, group.h, secp256k1.c, num.h, scalar_impl.h, ecmult_gen_impl.h, eckey_impl.h, hash_impl.h, scalar_4x64_impl.h, ecmult_impl.h, testrand_impl.h, scalar.h, bench_internal.c, bench_verify.c, util.h, testrand.h, field_10x26_impl.h, field_5x52_impl.h, group_impl.h, bench_ecdh.c, field.h, ecdsa.h, tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h, org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java, secp256k1.h, secp256k1_recovery.h, secp256k1_ecdh.h]
               libsecp256k1: {
                  [libsecp256k1.pc.in, .gitignore, configure.ac, Makefile.am, .travis.yml, README.md, field_5x52_int128_impl.h, eckey.h, ecmult_const_impl.h, tests.c, field_impl.h, ecdsa_impl.h, hash.h, num_gmp_impl.h, group.h, secp256k1.c, num.h, scalar_impl.h, ecmult_gen_impl.h, eckey_impl.h, hash_impl.h, scalar_4x64_impl.h, ecmult_impl.h, testrand_impl.h, scalar.h, bench_internal.c, bench_verify.c, util.h, testrand.h, field_10x26_impl.h, field_5x52_impl.h, group_impl.h, bench_ecdh.c, field.h, ecdsa.h, tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h, org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java, secp256k1.h, secp256k1_recovery.h, secp256k1_ecdh.h]
                  src: {
                     [field_5x52_int128_impl.h, eckey.h, ecmult_const_impl.h, tests.c, field_impl.h, ecdsa_impl.h, hash.h, num_gmp_impl.h, group.h, secp256k1.c, num.h, scalar_impl.h, ecmult_gen_impl.h, eckey_impl.h, hash_impl.h, scalar_4x64_impl.h, ecmult_impl.h, testrand_impl.h, scalar.h, bench_internal.c, bench_verify.c, util.h, testrand.h, field_10x26_impl.h, field_5x52_impl.h, group_impl.h, bench_ecdh.c, field.h, ecdsa.h, tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h, org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java]
                     java: {
                        [org_bitcoin_NativeSecp256k1.h, org_bitcoin_NativeSecp256k1.c, NativeSecp256k1.java]
                        org: {
                           [NativeSecp256k1.java]
                           bitcoin: {
                              [NativeSecp256k1.java]
                           }
                        }
                     }
                     modules: {
                        [tests_impl.h, Makefile.am.include, main_impl.h, tests_impl.h, Makefile.am.include, main_impl.h]
                        ecdh: {
                           [tests_impl.h, Makefile.am.include, main_impl.h]
                        }
                        recovery: {
                           [tests_impl.h, Makefile.am.include, main_impl.h]
                        }
                     }
                  }
                  include: {
                     [secp256k1.h, secp256k1_recovery.h, secp256k1_ecdh.h]
                  }
                  obj: {
                     
                  }
               }
            }
            randentropy: {
               
            }
         }
         common: {
            [format.go, types_test.go, bytes_test.go, types.go, bytes.go, big_test.go, dist_test.go, solidity.go, solidity_test.go]
            number: {
               
            }
            math: {
               [dist_test.go]
            }
            compiler: {
               [solidity.go, solidity_test.go]
            }
         }
         eth: {
            [sync.go, backend_test.go, helper_test.go, api_backend.go, handler.go, handler_test.go, protocol.go, protocol_test.go, db_upgrade.go, bad_block.go, backend.go, bind.go, api.go, fetcher_test.go, filter_system_test.go, filter.go, filter_test.go, filter_system.go, api.go, api_test.go, downloader_test.go, peer.go, downloader.go, queue.go]
            fetcher: {
               [fetcher_test.go]
            }
            filters: {
               [filter_system_test.go, filter.go, filter_test.go, filter_system.go, api.go, api_test.go]
            }
            downloader: {
               [downloader_test.go, peer.go, downloader.go, queue.go]
            }
         }
         ethclient: {
            [ethclient.go, ethclient_test.go]
         }
      }

-----------------------------

RELATIVE DIFFERENCE FOR <<IN BOTH, BUT DIFFERENT>>:

Makefile => 0.977112485085 

vendor.conf => 0.728567794454 

.gitignore => 0.994464944649 

appveyor.yml => 0.720138488171 

VERSION => 0.833333333333 

README.md => 0.555308028447 

interfaces.go => 0.933380402441 

.mailmap => 0.844064386318 

AUTHORS => 0.719160104987 

.travis.yml => 0.336860068259 

trie/sync.go => 0.992237196765 

trie/hasher.go => 1.0 

trie/trie.go => 0.997552557264 

trie/sync_test.go => 0.99719814377 

trie/encoding.go => 0.999463615233 

trie/iterator_test.go => 0.999525391552 

trie/trie_test.go => 0.996974174935 

whisper/whisperv5/message.go => 0.99335780458 

whisper/whisperv5/message_test.go => 0.908453303802 

whisper/whisperv5/whisper.go => 0.959877435393 

whisper/whisperv5/envelope.go => 0.989672599429 

whisper/whisperv5/whisper_test.go => 0.877927017711 

whisper/whisperv5/benchmarks_test.go => 0.965661641541 

whisper/whisperv5/doc.go => 0.965740142211 

whisper/whisperv5/filter.go => 0.959339894622 

whisper/whisperv5/filter_test.go => 0.938699690402 

whisper/whisperv5/peer.go => 0.98972043424 

whisper/whisperv5/peer_test.go => 0.984287520318 

whisper/whisperv5/topic_test.go => 0.989748743719 

whisper/whisperv5/topic.go => 0.973273942094 

whisper/shhapi/api_test.go => 0.42419250456 

whisper/shhapi/api.go => 0.970473575375 

whisper/whisperv2/envelope_test.go => 0.990726268626 

whisper/whisperv2/message_test.go => 0.997246262785 

whisper/whisperv2/filter.go => 0.996067214873 

whisper/whisperv2/filter_test.go => 0.99618164462 

whisper/whisperv2/peer.go => 0.999714421704 

whisper/whisperv2/peer_test.go => 0.999803729146 

whisper/whisperv2/topic_test.go => 0.968546637744 

whisper/whisperv2/api.go => 0.987799011676 

rpc/subscription.go => 1.0 

rpc/json.go => 0.985508416421 

rpc/types.go => 0.82583512931 

rpc/server.go => 0.999597072057 

rpc/subscription_test.go => 0.999204093235 

rpc/client.go => 0.998360046356 

accounts/abi/argument.go => 0.982703847511 

accounts/abi/abi.go => 0.925532348031 

accounts/abi/reflect.go => 0.973799894496 

accounts/abi/type.go => 0.935528664947 

accounts/abi/abi_test.go => 0.959917751113 

accounts/abi/event.go => 0.963291139241 

accounts/abi/packing.go => 0.997235023041 

accounts/abi/bind/auth.go => 0.986823529412 

accounts/abi/bind/util_test.go => 0.993390950686 

accounts/abi/bind/bind_test.go => 0.972432864519 

accounts/abi/bind/template.go => 0.851066404477 

accounts/abi/bind/base.go => 0.996311259441 

accounts/abi/bind/bind.go => 0.745989470424 

accounts/abi/bind/backend.go => 0.999787640688 

accounts/abi/bind/backends/simulated.go => 0.964371202357 

errs/errors.go => 0.885793871866 

errs/errors_test.go => 0.851877133106 

event/event_test.go => 0.967829326109 

event/event.go => 0.963283352557 

event/filter/generic_filter.go => 0.998958694898 

console/console_test.go => 0.998245697217 

console/prompter.go => 0.997817476356 

console/console.go => 0.993385121612 

console/bridge.go => 0.982407037185 

compression/rle/read_write.go => 0.994087504927 

.git/index => 0.934161191795 

.git/HEAD => 0.823529411765 

.git/packed-refs => 0.111462951235 

.git/config => 0.872675250358 

.git/refs/heads/master => 0.658536585366 

.git/logs/HEAD => 0.4 

.git/logs/refs/remotes/origin/HEAD => 0.869778869779 

.git/logs/refs/heads/master => 0.869778869779 

.github/CONTRIBUTING.md => 0.711349419124 

.github/ISSUE_TEMPLATE.md => 0.940711462451 

swarm/swarm.go => 0.975473801561 

swarm/api/api.go => 0.975075663165 

swarm/api/config_test.go => 0.962147780868 

swarm/api/filesystem.go => 0.983314285714 

swarm/api/manifest.go => 0.992228854601 

swarm/api/config.go => 0.953900263786 

swarm/api/filesystem_test.go => 0.997287032013 

swarm/api/http/roundtripper.go => 0.988316745997 

swarm/api/http/roundtripper_test.go => 0.977249747219 

swarm/api/http/server.go => 0.909716342083 

swarm/storage/chunker.go => 0.997338935574 

swarm/storage/memstore.go => 0.965125254368 

swarm/storage/common_test.go => 0.999316239316 

swarm/storage/localstore.go => 0.985769728331 

swarm/storage/dbstore.go => 0.939481268012 

swarm/storage/dbstore_test.go => 0.998657460683 

swarm/storage/dpa.go => 0.995263266287 

swarm/storage/types.go => 0.998902730265 

swarm/storage/netstore.go => 0.993172915501 

swarm/storage/dpa_test.go => 0.999037304452 

swarm/network/syncdb_test.go => 0.99138313938 

swarm/network/depo.go => 0.996285336523 

swarm/network/hive.go => 0.989806678383 

swarm/network/protocol.go => 0.995624111148 

swarm/network/syncer.go => 0.999784613577 

swarm/network/protocol_test.go => 0.998763906057 

swarm/network/kademlia/kademlia_test.go => 0.999416538482 

internal/web3ext/web3ext.go => 0.796662211466 

internal/ethapi/tracer.go => 0.99830517741 

internal/ethapi/backend.go => 0.980517937752 

internal/ethapi/tracer_test.go => 0.807933718303 

internal/ethapi/api.go => 0.955788600098 

internal/jsre/pretty.go => 0.997905612957 

internal/jsre/jsre.go => 0.991482112436 

internal/build/archive.go => 0.974000687207 

internal/build/util.go => 0.92661611618 

internal/build/env.go => 0.982429139413 

params/gas_table.go => 0.903944315545 

params/protocol_params.go => 0.991922755547 

params/util.go => 0.935965578335 

build/env.sh => 0.925160370634 

build/ci.go => 0.643906850554 

build/ci-notes.md => 0.995230524642 

build/update-license.go => 0.997753818509 

logger/glog/glog.go => 0.99994622644 

containers/docker/master-alpine/Dockerfile => 0.913770913771 

containers/docker/develop-alpine/Dockerfile => 0.95213454075 

containers/docker/develop-ubuntu/Dockerfile => 0.833855799373 

containers/docker/master-ubuntu/Dockerfile => 0.82340862423 

node/config_test.go => 0.998086490624 

node/node.go => 0.994838806193 

node/node_example_test.go => 0.998566993074 

node/config.go => 0.962914455091 

node/node_test.go => 0.999133871055 

node/api.go => 0.99332391209 

core/chain_pow_test.go => 0.993904916701 

core/genesis.go => 0.871891301711 

core/block_validator_test.go => 0.979231758868 

core/bench_test.go => 0.991086129563 

core/tx_pool.go => 0.976351207914 

core/block_validator.go => 0.837512327785 

core/dao.go => 0.994923857868 

core/tx_list.go => 0.999871536848 

core/chain_makers.go => 0.991525838844 

core/blocks.go => 0.957514846962 

core/headerchain.go => 0.932430044183 

core/blockchain_test.go => 0.90503844074 

core/events.go => 0.962650348175 

core/default_genesis.go => 0.997140993839 

core/tx_pool_test.go => 0.811272898074 

core/state_processor.go => 0.935503525111 

core/chain_makers_test.go => 0.971787637856 

core/types.go => 0.873303167421 

core/database_util_test.go => 0.994140320389 

core/tx_list_test.go => 0.996082820369 

core/database_util.go => 0.967773901195 

core/blockchain.go => 0.987382601271 

core/state_transition.go => 0.925334125334 

core/state/sync.go => 0.972719869707 

core/state/iterator.go => 0.998619873817 

core/state/statedb.go => 0.966092531088 

core/state/statedb_test.go => 0.984489318115 

core/state/sync_test.go => 0.996500358938 

core/state/journal.go => 0.933644548183 

core/state/iterator_test.go => 0.999207816213 

core/state/managed_state_test.go => 0.996569188041 

core/state/state_object.go => 0.96620296891 

core/state/state_test.go => 0.999026542929 

core/vm/contracts.go => 0.917533620908 

core/vm/opcodes.go => 0.990428319341 

core/vm/errors.go => 0.93900833699 

core/vm/stack.go => 0.975641583297 

core/vm/vm.go => 0.653246540124 

core/vm/vm_jit_fake.go => 0.922128851541 

core/vm/vm_jit.go => 0.998328845975 

core/vm/logger_test.go => 0.976397515528 

core/vm/instructions.go => 0.926602814699 

core/vm/environment.go => 0.571645089991 

core/vm/logger.go => 0.981887078439 

core/vm/jump_table.go => 0.438189658099 

core/vm/gas.go => 0.998646296654 

core/vm/contract.go => 0.979342627455 

core/vm/runtime/runtime_test.go => 0.999044281618 

core/vm/runtime/env.go => 0.54930875576 

core/vm/runtime/runtime.go => 0.935692412385 

core/types/transaction_test.go => 0.918760315423 

core/types/block.go => 0.980282938254 

core/types/bloom9.go => 0.957216028924 

core/types/receipt.go => 0.994771643857 

core/types/block_test.go => 0.975 

core/types/transaction.go => 0.92433354277 

tests/init.go => 0.942865345966 

tests/vm_test_util.go => 0.986799501868 

tests/block_test_util.go => 0.997054120024 

tests/transaction_test_util.go => 0.983890038427 

tests/transaction_test.go => 0.701766420854 

tests/vm_test.go => 0.996900025833 

tests/state_test_util.go => 0.948488908739 

tests/block_test.go => 0.585379568885 

tests/util.go => 0.758123640882 

tests/state_test.go => 0.771015929523 

tests/files/VMTests/vmIOandFlowOperationsTest.json => 0.999978688717 

tests/files/VMTests/vmPerformanceTest.json => 0.918431298072 

tests/files/VMTests/vmEnvironmentalInfoTest.json => 0.999896313364 

tests/files/VMTests/vmPushDupSwapTest.json => 0.993959222548 

tests/files/VMTests/vmSystemOperationsTest.json => 0.983965324306 

tests/files/StateTests/stPreCompiledContracts.json => 0.999850490604 

tests/files/StateTests/stSystemOperationsTest.json => 0.999909957798 

tests/files/StateTests/EIP150/stMemExpandingEIPCalls.json => 0.999083718234 

tests/files/StateTests/EIP150/stEIPSpecificTest.json => 0.88140317951 

tests/files/StateTests/EIP150/stEIPSingleCodeGasPrices.json => 0.998910763524 

tests/files/StateTests/EIP150/Homestead/stPreCompiledContracts.json => 0.998792945341 

tests/files/StateTests/EIP150/Homestead/stBoundsTest.json => 0.999155228416 

tests/files/StateTests/EIP150/Homestead/stQuadraticComplexityTest.json => 0.999954299224 

tests/files/StateTests/EIP150/Homestead/stTransactionTest.json => 0.998491086633 

tests/files/StateTests/EIP150/Homestead/stLogTests.json => 0.999190606341 

tests/files/StateTests/EIP150/Homestead/stCallCodes.json => 0.999222260629 

tests/files/StateTests/EIP150/Homestead/stRecursiveCreate.json => 0.999947549697 

tests/files/StateTests/EIP150/Homestead/stDelegatecallTest.json => 0.998866855524 

tests/files/StateTests/EIP150/Homestead/stInitCodeTest.json => 0.995596400536 

tests/files/StateTests/EIP150/Homestead/stWalletTest.json => 0.999654420798 

tests/files/StateTests/EIP150/Homestead/stSystemOperationsTest.json => 0.999499319618 

tests/files/StateTests/EIP150/Homestead/stCallCreateCallCodeTest.json => 0.998949221594 

tests/files/StateTests/EIP150/Homestead/stSpecialTest.json => 0.999806772965 

tests/files/StateTests/EIP150/Homestead/stMemoryTest.json => 0.998657487091 

tests/files/StateTests/EIP150/Homestead/stCallDelegateCodes.json => 0.999235621782 

tests/files/StateTests/EIP150/Homestead/stHomeSteadSpecific.json => 0.998669505056 

tests/files/StateTests/EIP150/Homestead/stRefundTest.json => 0.987661394283 

tests/files/StateTests/EIP150/Homestead/stCallDelegateCodesCallCode.json => 0.999233756969 

tests/files/StateTests/Homestead/stPreCompiledContracts.json => 0.999850717622 

tests/files/StateTests/Homestead/stTransactionTest.json => 0.986811625874 

tests/files/StateTests/Homestead/stDelegatecallTest.json => 0.999765691059 

tests/files/StateTests/Homestead/stSystemOperationsTest.json => 0.999274301835 

tests/files/TransactionTests/ttTransactionTest.json => 0.966114150404 

tests/files/TransactionTests/Homestead/ttTransactionTest.json => 0.966980215877 

tests/files/BlockchainTests/bcInvalidHeaderTest.json => 0.929272126172 

tests/files/BlockchainTests/TestNetwork/bcTheDaoTest.json => 0.999997125388 

tests/files/BlockchainTests/TestNetwork/bcEIP150Test.json => 0.999995756508 

tests/files/BlockchainTests/Homestead/bcShanghaiLove.json => 0.999999641505 

tests/files/BlockchainTests/Homestead/bcSuicideIssue.json => 0.767977879444 

tests/files/BlockchainTests/Homestead/bcInvalidHeaderTest.json => 0.925803792251 

vendor/github.com/huin/goupnp/README.md => 0.925287356322 

vendor/github.com/huin/goupnp/ssdp/registry.go => 0.999865356133 

vendor/github.com/rcrowley/go-metrics/registry.go => 0.999865501009 

vendor/github.com/rcrowley/go-metrics/sample.go => 0.995872720011 

vendor/github.com/rcrowley/go-metrics/gauge.go => 0.999823788546 

vendor/github.com/fatih/color/color.go => 0.908426036414 

vendor/github.com/fatih/color/doc.go => 0.936842105263 

vendor/github.com/fatih/color/README.md => 0.941585535466 

vendor/github.com/nsf/termbox-go/termbox.go => 0.998508069985 

vendor/github.com/nsf/termbox-go/README.md => 0.986472844741 

vendor/github.com/nsf/termbox-go/api.go => 0.999082874771 

vendor/github.com/gizak/termui/block_windows.go => 0.988571428571 

vendor/github.com/gizak/termui/block.go => 0.999250796029 

vendor/github.com/gizak/termui/sparkline.go => 0.998934185985 

vendor/github.com/gizak/termui/block_common.go => 0.992409867173 

vendor/github.com/gizak/termui/barchart.go => 0.998861696073 

vendor/github.com/gizak/termui/mbarchart.go => 0.999358974359 

vendor/github.com/gizak/termui/buffer.go => 0.99721448468 

vendor/github.com/gizak/termui/doc.go => 0.993893129771 

vendor/github.com/gizak/termui/theme.go => 0.998742533794 

vendor/github.com/gizak/termui/linechart_others.go => 0.984962406015 

vendor/github.com/gizak/termui/canvas.go => 0.997041420118 

vendor/github.com/gizak/termui/list.go => 0.998064828254 

vendor/github.com/gizak/termui/events.go => 0.999313304721 

vendor/github.com/gizak/termui/linechart_windows.go => 0.984555984556 

vendor/github.com/gizak/termui/grid.go => 0.99926335175 

vendor/github.com/gizak/termui/glide.yaml => 0.916666666667 

vendor/github.com/gizak/termui/helper.go => 0.999048525214 

vendor/github.com/gizak/termui/render.go => 0.868014647349 

vendor/github.com/gizak/termui/textbuilder.go => 0.999365079365 

vendor/github.com/gizak/termui/widget.go => 0.997518610422 

vendor/github.com/gizak/termui/linechart.go => 0.999466025898 

vendor/github.com/gizak/termui/pos.go => 0.997594708358 

vendor/github.com/gizak/termui/par.go => 0.997501561524 

vendor/github.com/gizak/termui/glide.lock => 0.691374663073 

vendor/github.com/gizak/termui/gauge.go => 0.998247919404 

vendor/github.com/pborman/uuid/README.md => 0.999239543726 

vendor/github.com/peterh/liner/common.go => 0.970376301041 

vendor/github.com/peterh/liner/input_windows.go => 0.961911401229 

vendor/github.com/peterh/liner/width.go => 0.926543751829 

vendor/github.com/peterh/liner/line.go => 0.981271723574 

vendor/github.com/peterh/liner/input.go => 0.985487301389 

vendor/github.com/syndtr/goleveldb/leveldb/session_util.go => 0.965839626034 

vendor/github.com/syndtr/goleveldb/leveldb/session.go => 0.994663421028 

vendor/github.com/syndtr/goleveldb/leveldb/version.go => 0.992370499264 

vendor/github.com/mattn/go-colorable/colorable_windows.go => 0.984725824622 

vendor/github.com/mattn/go-colorable/colorable_others.go => 0.711453744493 

vendor/github.com/mattn/go-colorable/noncolorable.go => 0.916822429907 

vendor/github.com/davecgh/go-spew/LICENSE => 0.99868938401 

vendor/github.com/davecgh/go-spew/README.md => 0.966741540468 

vendor/github.com/davecgh/go-spew/spew/common.go => 0.999758722193 

vendor/github.com/davecgh/go-spew/spew/format.go => 0.999779298168 

vendor/github.com/davecgh/go-spew/spew/doc.go => 0.97757793765 

vendor/github.com/davecgh/go-spew/spew/bypass.go => 0.999567959907 

vendor/github.com/davecgh/go-spew/spew/config.go => 0.984581323634 

vendor/github.com/davecgh/go-spew/spew/dump.go => 0.996658676545 

vendor/github.com/davecgh/go-spew/spew/bypasssafe.go => 0.998556165175 

vendor/github.com/davecgh/go-spew/spew/spew.go => 0.999580993883 

vendor/gopkg.in/urfave/cli.v1/app.go => 0.982836125868 

vendor/gopkg.in/urfave/cli.v1/cli.go => 0.93302891933 

vendor/gopkg.in/urfave/cli.v1/flag.go => 0.943710084658 

vendor/gopkg.in/urfave/cli.v1/help.go => 0.958082133485 

vendor/gopkg.in/urfave/cli.v1/runtests => 0.905019593208 

vendor/gopkg.in/urfave/cli.v1/errors.go => 0.917541229385 

vendor/gopkg.in/urfave/cli.v1/CHANGELOG.md => 0.894710444076 

vendor/gopkg.in/urfave/cli.v1/appveyor.yml => 0.973952434881 

vendor/gopkg.in/urfave/cli.v1/command.go => 0.971386967601 

vendor/gopkg.in/urfave/cli.v1/context.go => 0.651062740077 

vendor/gopkg.in/urfave/cli.v1/.travis.yml => 0.90310786106 

vendor/gopkg.in/urfave/cli.v1/README.md => 0.983325531468 

vendor/gopkg.in/check.v1/check.go => 0.998767928958 

vendor/gopkg.in/check.v1/checkers.go => 0.999960036766 

vendor/golang.org/x/sys/unix/zsyscall_linux_ppc64.go => 0.997462848858 

vendor/golang.org/x/sys/unix/types_linux.go => 0.992613313519 

vendor/golang.org/x/sys/unix/mksysnum_linux.pl => 0.922048997773 

vendor/golang.org/x/sys/unix/syscall_linux.go => 0.976340477984 

vendor/golang.org/x/sys/unix/zsyscall_linux_mips64.go => 0.997383948087 

vendor/golang.org/x/sys/unix/zerrors_linux_ppc64le.go => 0.994897765398 

vendor/golang.org/x/sys/unix/mkerrors.sh => 0.998227793387 

vendor/golang.org/x/sys/unix/zerrors_linux_arm64.go => 0.994694017274 

vendor/golang.org/x/sys/unix/ztypes_linux_amd64.go => 0.993770178709 

vendor/golang.org/x/sys/unix/ztypes_linux_mips64le.go => 0.993600224226 

vendor/golang.org/x/sys/unix/syscall_unix.go => 0.975670344122 

vendor/golang.org/x/sys/unix/zsyscall_linux_ppc64le.go => 0.997462960319 

vendor/golang.org/x/sys/unix/zsyscall_linux_386.go => 0.997120311156 

vendor/golang.org/x/sys/unix/zerrors_linux_sparc64.go => 0.995180578809 

vendor/golang.org/x/sys/unix/ztypes_linux_ppc64le.go => 0.993769612079 

vendor/golang.org/x/sys/unix/zsyscall_linux_amd64.go => 0.997452215249 

vendor/golang.org/x/sys/unix/zerrors_linux_amd64.go => 0.994460404954 

vendor/golang.org/x/sys/unix/zerrors_linux_s390x.go => 0.995045488075 

vendor/golang.org/x/sys/unix/ztypes_linux_arm64.go => 0.993644166087 

vendor/golang.org/x/sys/unix/ztypes_linux_s390x.go => 0.993794446709 

vendor/golang.org/x/sys/unix/zsyscall_linux_mips64le.go => 0.997384066587 

vendor/golang.org/x/sys/unix/ztypes_linux_mips64.go => 0.993599028174 

vendor/golang.org/x/sys/unix/syscall_linux_amd64.go => 0.992105263158 

vendor/golang.org/x/sys/unix/zerrors_linux_ppc64.go => 0.99489834671 

vendor/golang.org/x/sys/unix/ztypes_linux_386.go => 0.99355081674 

vendor/golang.org/x/sys/unix/zsyscall_linux_arm.go => 0.997330066228 

vendor/golang.org/x/sys/unix/ztypes_linux_ppc64.go => 0.993768478508 

vendor/golang.org/x/sys/unix/zsyscall_linux_s390x.go => 0.997073541522 

vendor/golang.org/x/sys/unix/zerrors_linux_386.go => 0.994457814756 

vendor/golang.org/x/sys/unix/zerrors_linux_arm.go => 0.994205857404 

vendor/golang.org/x/sys/unix/zsyscall_linux_sparc64.go => 0.99742368647 

vendor/golang.org/x/sys/unix/zsyscall_linux_arm64.go => 0.997291244034 

vendor/golang.org/x/sys/unix/flock_linux_32bit.go => 0.968085106383 

vendor/golang.org/x/sys/unix/ztypes_linux_arm.go => 0.993493850026 

vendor/golang.org/x/sys/unix/ztypes_linux_sparc64.go => 0.993814060595 

vendor/golang.org/x/sys/unix/syscall_bsd.go => 0.991705240921 

vendor/golang.org/x/text/language/tables.go => 0.999875560754 

vendor/golang.org/x/text/internal/gen/code.go => 0.970810210877 

vendor/golang.org/x/net/websocket/websocket.go => 0.992367045549 

vendor/golang.org/x/tools/imports/fix.go => 0.999324729892 

contracts/chequebook/cheque_test.go => 0.9978404643 

contracts/chequebook/cheque.go => 0.999953246996 

contracts/release/release.go => 0.973810526316 

contracts/release/contract.sol => 0.999945843488 

contracts/ens/ens_test.go => 0.997462514418 

ethdb/memory_database.go => 0.99944842802 

ethdb/database.go => 0.942737038767 

metrics/disk_linux.go => 0.989050165521 

metrics/metrics.go => 0.970303352847 

p2p/server.go => 0.98622313929 

p2p/dial.go => 0.946199169323 

p2p/dial_test.go => 0.972888425443 

p2p/peer_test.go => 0.999834646971 

p2p/rlpx.go => 0.999630168397 

p2p/discover/udp_test.go => 0.974248206014 

p2p/discover/udp.go => 0.986346438559 

p2p/discover/database_test.go => 0.999740977379 

p2p/discover/node.go => 0.998286245899 

p2p/discover/database.go => 0.999386986601 

p2p/discover/table_test.go => 0.998217271735 

p2p/discover/table.go => 0.999897933146 

p2p/nat/natpmp.go => 0.99943019943 

p2p/nat/nat_test.go => 0.995735607676 

light/odr.go => 0.764843142339 

light/trie.go => 0.975515818432 

light/state.go => 0.955969234199 

light/state_object.go => 0.932062592569 

light/state_test.go => 0.982028506507 

cmd/geth/chaincmd.go => 0.906409903714 

cmd/geth/usage.go => 0.966831460674 

cmd/geth/consolecmd.go => 0.979996720774 

cmd/geth/accountcmd_test.go => 0.988606573906 

cmd/geth/main.go => 0.900245607406 

cmd/geth/accountcmd.go => 0.965662968833 

cmd/geth/consolecmd_test.go => 0.997530022996 

cmd/geth/monitorcmd.go => 0.996765474766 

cmd/abigen/main.go => 0.951740139211 

cmd/bootnode/main.go => 0.898844388159 

cmd/evm/main.go => 0.78559033803 

cmd/utils/cmd.go => 0.962512495835 

cmd/utils/customflags.go => 0.985762711864 

cmd/utils/flags.go => 0.947900071184 

cmd/ethtest/main.go => 0.980158392234 

cmd/disasm/main.go => 0.930129798398 

cmd/gethrpctest/main.go => 0.99201385548 

crypto/crypto_test.go => 0.944951734933 

crypto/crypto.go => 0.949636182052 

crypto/ecies/asn1.go => 0.999375433727 

crypto/ecies/ecies_test.go => 0.999273563775 

crypto/ecies/ecies.go => 0.999185750636 

crypto/sha3/sha3_test.go => 0.999774926851 

crypto/secp256k1/secp256.go => 0.780012771392 

crypto/secp256k1/secp256_test.go => 0.975323323919 

crypto/secp256k1/curve.go => 0.960773166572 

crypto/secp256k1/libsecp256k1/libsecp256k1.pc.in => 0.992295839753 

crypto/secp256k1/libsecp256k1/.gitignore => 0.816568047337 

crypto/secp256k1/libsecp256k1/configure.ac => 0.854964698813 

crypto/secp256k1/libsecp256k1/Makefile.am => 0.759230252853 

crypto/secp256k1/libsecp256k1/.travis.yml => 0.897058823529 

crypto/secp256k1/libsecp256k1/README.md => 0.998382923674 

crypto/secp256k1/libsecp256k1/src/field_5x52_int128_impl.h => 0.999891197911 

crypto/secp256k1/libsecp256k1/src/eckey.h => 0.889871086556 

crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h => 0.960120229725 

crypto/secp256k1/libsecp256k1/src/tests.c => 0.628760895477 

crypto/secp256k1/libsecp256k1/src/field_impl.h => 0.899956038435 

crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h => 0.906726085605 

crypto/secp256k1/libsecp256k1/src/hash.h => 0.999124087591 

crypto/secp256k1/libsecp256k1/src/num_gmp_impl.h => 0.95840328297 

crypto/secp256k1/libsecp256k1/src/group.h => 0.989475035297 

crypto/secp256k1/libsecp256k1/src/secp256k1.c => 0.956164383562 

crypto/secp256k1/libsecp256k1/src/num.h => 0.95393258427 

crypto/secp256k1/libsecp256k1/src/scalar_impl.h => 0.95308268281 

crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h => 0.983955269235 

crypto/secp256k1/libsecp256k1/src/eckey_impl.h => 0.574579642018 

crypto/secp256k1/libsecp256k1/src/hash_impl.h => 0.999132834056 

crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h => 0.997423352903 

crypto/secp256k1/libsecp256k1/src/ecmult_impl.h => 0.983081418419 

crypto/secp256k1/libsecp256k1/src/testrand_impl.h => 0.667335674862 

crypto/secp256k1/libsecp256k1/src/scalar.h => 0.993555203381 

crypto/secp256k1/libsecp256k1/src/bench_internal.c => 0.96480299614 

crypto/secp256k1/libsecp256k1/src/bench_verify.c => 0.760883280757 

crypto/secp256k1/libsecp256k1/src/util.h => 0.984969053935 

crypto/secp256k1/libsecp256k1/src/testrand.h => 0.827392871446 

crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h => 0.998267280292 

crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h => 0.996660077704 

crypto/secp256k1/libsecp256k1/src/group_impl.h => 0.945424592456 

crypto/secp256k1/libsecp256k1/src/bench_ecdh.c => 0.976138828633 

crypto/secp256k1/libsecp256k1/src/field.h => 0.962539273342 

crypto/secp256k1/libsecp256k1/src/ecdsa.h => 0.922471467926 

crypto/secp256k1/libsecp256k1/src/modules/ecdh/tests_impl.h => 0.839393939394 

crypto/secp256k1/libsecp256k1/src/modules/ecdh/Makefile.am.include => 0.938230383973 

crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h => 0.993633952255 

crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_impl.h => 0.783940197733 

crypto/secp256k1/libsecp256k1/src/modules/recovery/Makefile.am.include => 0.938461538462 

crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h => 0.895355086372 

crypto/secp256k1/libsecp256k1/src/java/org_bitcoin_NativeSecp256k1.h => 0.246009389671 

crypto/secp256k1/libsecp256k1/src/java/org_bitcoin_NativeSecp256k1.c => 0.117574161568 

crypto/secp256k1/libsecp256k1/src/java/org/bitcoin/NativeSecp256k1.java => 0.235103046595 

crypto/secp256k1/libsecp256k1/include/secp256k1.h => 0.969415455149 

crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h => 0.997119385469 

crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h => 0.953798767967 

common/format.go => 0.998276456394 

common/types_test.go => 0.937366686058 

common/bytes_test.go => 0.997499553492 

common/types.go => 0.924075531078 

common/bytes.go => 0.999256505576 

common/big_test.go => 0.991426344505 

common/math/dist_test.go => 0.978545887962 

common/compiler/solidity.go => 0.975614066089 

common/compiler/solidity_test.go => 0.929750375119 

eth/sync.go => 0.998003992016 

eth/backend_test.go => 0.990273101384 

eth/helper_test.go => 0.982259427079 

eth/api_backend.go => 0.962946974602 

eth/handler.go => 0.987291849255 

eth/handler_test.go => 0.992954107755 

eth/protocol.go => 0.998636983189 

eth/protocol_test.go => 0.999734994037 

eth/db_upgrade.go => 0.999907398833 

eth/bad_block.go => 0.999587968686 

eth/backend.go => 0.952573829459 

eth/bind.go => 0.989124714962 

eth/api.go => 0.884523701759 

eth/fetcher/fetcher_test.go => 0.998225921443 

eth/filters/filter_system_test.go => 0.832100098447 

eth/filters/filter.go => 0.878231339663 

eth/filters/filter_test.go => 0.970395910118 

eth/filters/filter_system.go => 0.814859197124 

eth/filters/api.go => 0.975630170943 

eth/filters/api_test.go => 0.991248541424 

eth/downloader/downloader_test.go => 0.978745272701 

eth/downloader/peer.go => 0.999840781233 

eth/downloader/downloader.go => 0.991882451336 

eth/downloader/queue.go => 0.994335736354 

ethclient/ethclient.go => 0.969704556835 

ethclient/ethclient_test.go => 0.592820512821 
