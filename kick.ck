
TriOsc s => LPF lpf => ADSR env => dac;

0.9 => s.gain;
800 => s.freq;
600 => lpf.freq;
2 => lpf.Q;

5::ms => env.attackTime;
30::ms => env.decayTime;
0.1 => env.sustainLevel;
80::ms => env.releaseTime;

env.keyOn();

[800, 600, 420, 300] @=> int freqs[];
for (0 => int i; i < freqs.size(); i++) {
    freqs[i] => s.freq;
    20::ms => now;
}

env.keyOff();
200::ms => now;