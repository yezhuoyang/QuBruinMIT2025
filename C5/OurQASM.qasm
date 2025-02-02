// Generated from Cirq v1.4.1

OPENQASM 2.0;
include "qelib1.inc";


// Qubits: [q(0), q(1), q(2), q(3), q(4), q(5), q(6)]
qreg q[7];


ry (0.5*pi) q[0];
ry (0.5*pi) q[1];
ry (0.5*pi) q[2];
ry (0.5*pi) q[3];
ry (0.5*pi) q[4];
ry (0.5*pi) q[5];
ry (0.5*pi) q[6];
rx (pi) q[0];
rx (pi) q[1];
rx (pi) q[2];
rx (pi) q[3];
rx (pi) q[4];
rx (pi) q[5];
rx (pi) q[6];
cz q[0], q[1];
cz q[2], q[4];
cz q[5], q[6];
cz q[0], q[2];
cz q[3], q[5];
cz q[4], q[6];

ry (0.5*pi) q[6];
rx (pi) q[6];

cz q[3], q[4];
cz q[1], q[5];
cz q[2], q[6];

cz q[0], q[3];
cz q[1], q[6];

ry (0.5*pi) q[0];
ry (0.5*pi) q[4];
ry (0.5*pi) q[5];
ry (0.5*pi) q[6];
rx (pi) q[0];
rx (pi) q[4];
rx (pi) q[5];
rx (pi) q[6];

