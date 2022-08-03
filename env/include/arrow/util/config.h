// Licensed to the Apache Software Foundation (ASF) under one
// or more contributor license agreements.  See the NOTICE file
// distributed with this work for additional information
// regarding copyright ownership.  The ASF licenses this file
// to you under the Apache License, Version 2.0 (the
// "License"); you may not use this file except in compliance
// with the License.  You may obtain a copy of the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing,
// software distributed under the License is distributed on an
// "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
// KIND, either express or implied.  See the License for the
// specific language governing permissions and limitations
// under the License.

#define ARROW_VERSION_MAJOR 7
#define ARROW_VERSION_MINOR 0
#define ARROW_VERSION_PATCH 0
#define ARROW_VERSION ((ARROW_VERSION_MAJOR * 1000) + ARROW_VERSION_MINOR) * 1000 + ARROW_VERSION_PATCH

#define ARROW_VERSION_STRING "7.0.0"

#define ARROW_SO_VERSION "700"
#define ARROW_FULL_SO_VERSION "700.0.0"

#define ARROW_CXX_COMPILER_ID "Clang"
#define ARROW_CXX_COMPILER_VERSION "13.0.1"
#define ARROW_CXX_COMPILER_FLAGS "-march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -stdlib=libc++ -fvisibility-inlines-hidden -fmessage-length=0 -isystem /Users/bluntsord/Documents/Projects/GIC-Test/Temp/env/include -fdebug-prefix-map=/Users/runner/miniforge3/conda-bld/arrow-cpp-ext_1655627463070/work=/usr/local/src/conda/arrow-cpp-7.0.0 -fdebug-prefix-map=/Users/bluntsord/Documents/Projects/GIC-Test/Temp/env=/usr/local/src/conda-prefix -Qunused-arguments -fcolor-diagnostics -O3 -DNDEBUG"

#define ARROW_BUILD_TYPE "RELEASE"

#define ARROW_GIT_ID ""
#define ARROW_GIT_DESCRIPTION ""

#define ARROW_PACKAGE_KIND ""

#define ARROW_COMPUTE
#define ARROW_CSV
#define ARROW_DATASET
#define ARROW_FILESYSTEM
#define ARROW_FLIGHT
#define ARROW_IPC
#define ARROW_JSON

#define ARROW_S3
#define ARROW_USE_NATIVE_INT128
/* #undef ARROW_WITH_OPENTELEMETRY */

#define GRPCPP_PP_INCLUDE
