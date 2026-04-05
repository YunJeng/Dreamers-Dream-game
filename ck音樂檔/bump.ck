
SinOsc s1 => Gain g => dac;
TriOsc s2 => g;
0.4 => g.gain;
[600, 800, 1000, 1300, 1600] @=> int freqs[];

for (0 => int i; i < freqs.size(); i++) {
    freqs[i] => s1.freq;
    freqs[i] * 0.8 => s2.freq;
    0.04::second => now;
}
100 => s2.freq;
50::ms => now;
