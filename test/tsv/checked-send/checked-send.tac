Block [0x0:0xf]
---
Predecessors: []
Successors: []
---
0x0 PUSH1 0x60
0x2 PUSH1 0x40
0x4 MSTORE
0x5 PUSH1 0x47
0x7 DUP1
0x8 PUSH1 0x10
0xa PUSH1 0x0
0xc CODECOPY
0xd PUSH1 0x0
0xf RETURN
---
0x0: V0 = 0x60
0x2: V1 = 0x40
0x4: M[0x40] = 0x60
0x5: V2 = 0x47
0x8: V3 = 0x10
0xa: V4 = 0x0
0xc: CODECOPY 0x0 0x10 0x47
0xd: V5 = 0x0
0xf: RETURN 0x0 0x47
---
Stack pops: 0
Stack additions: []

-----

Block [0x10:0x19]
---
Predecessors: []
Successors: [0x1a]
---
0x10 PUSH1 0x60
0x12 PUSH1 0x40
0x14 MSTORE
0x15 CALLDATASIZE
0x16 ISZERO
0x17 PUSH1 0xa
0x19 JUMPI
---
0x10: V0 = 0x60
0x12: V1 = 0x40
0x14: M[0x40] = 0x60
0x15: V2 = CALLDATASIZE
0x16: V3 = ISZERO V2
0x17: V4 = 0xa
0x19: THROWI V3
---
Stack pops: 0
Stack additions: []

-----

Block [0x1a:0x4f]
---
Predecessors: [0x10]
Successors: [0x50]
---
0x1a JUMPDEST
0x1b PUSH1 0x43
0x1d PUSH1 0x40
0x1f MLOAD
0x20 PUSH20 0xffffffffffffffffffffffffffffffffffffffff
0x35 CALLER
0x36 AND
0x37 SWAP1
0x38 PUSH1 0x0
0x3a SWAP1
0x3b PUSH1 0x64
0x3d SWAP1
0x3e DUP3
0x3f DUP2
0x40 DUP2
0x41 DUP2
0x42 DUP6
0x43 DUP9
0x44 DUP4
0x45 CALL
0x46 SWAP4
0x47 POP
0x48 POP
0x49 POP
0x4a POP
0x4b ISZERO
0x4c ISZERO
0x4d PUSH1 0x45
0x4f JUMPI
---
0x1a: JUMPDEST 
0x1b: V0 = 0x43
0x1d: V1 = 0x40
0x1f: V2 = M[0x40]
0x20: V3 = 0xffffffffffffffffffffffffffffffffffffffff
0x35: V4 = CALLER
0x36: V5 = AND V4 0xffffffffffffffffffffffffffffffffffffffff
0x38: V6 = 0x0
0x3b: V7 = 0x64
0x45: V8 = CALL 0x0 V5 0x64 V2 0x0 V2 0x0
0x4b: V9 = ISZERO V8
0x4c: V10 = ISZERO V9
0x4d: V11 = 0x45
0x4f: THROWI V10
---
Stack pops: 0
Stack additions: [0x43]

-----

Block [0x50:0x52]
---
Predecessors: [0x1a]
Successors: []
---
0x50 PUSH1 0x2
0x52 JUMP
---
0x50: V0 = 0x2
0x52: THROW 
---
Stack pops: 0
Stack additions: []

-----

Block [0x53:0x54]
---
Predecessors: []
Successors: []
---
0x53 JUMPDEST
0x54 STOP
---
0x53: JUMPDEST 
0x54: STOP 
---
Stack pops: 0
Stack additions: []

-----

Block [0x55:0x56]
---
Predecessors: []
Successors: []
Has unresolved jump.
---
0x55 JUMPDEST
0x56 JUMP
---
0x55: JUMPDEST 
0x56: JUMP S0
---
Stack pops: 1
Stack additions: []
