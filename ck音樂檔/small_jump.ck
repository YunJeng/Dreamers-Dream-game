TriOsc osc => LPF lpf => ADSR env => dac;

800 => lpf.freq;       
2 => lpf.Q;            

10::ms => env.attackTime;
50::ms => env.decayTime;
0.4 => env.sustainLevel;
100::ms => env.releaseTime;

330 => osc.freq;

env.keyOn();

[330, 360, 400, 450] @=> int freqs[];

for (0 => int i; i < freqs.size(); i++) {
    freqs[i] => osc.freq;
    30::ms => now;
}

env.keyOff();
200::ms => now;
