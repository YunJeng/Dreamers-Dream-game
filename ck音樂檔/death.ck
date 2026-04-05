
SinOsc s => JCRev rev => ADSR env => dac;
0.5 => s.gain;
0.3 => rev.mix;


10::ms => env.attackTime;
100::ms => env.decayTime;
0.2 => env.sustainLevel;
400::ms => env.releaseTime;

env.keyOn();


[880, 660, 500, 380, 300, 220] @=> int freqs[];

for (0 => int i; i < freqs.size(); i++) {
    freqs[i] => s.freq;
    100::ms => now;
}

env.keyOff();
500::ms => now;
