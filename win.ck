SinOsc s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
        s[i] => dac;
}

ModalBar one => dac;
ModalBar two => dac;
1=> one. preset;//樂器
0=> two. preset;

one.controlChange(2, 40);   // Stick Hardness越大聲音越尖
one.controlChange(4, 100);    // Stick Position越大打擊位置越中心
one.controlChange(11,20);   // Vibrato Gain顫音
one.controlChange(7, 5);     // Vibrato Frequency顫音頻率
one.controlChange(1, 20);    // Direct Stick Mix原始打擊因比例
one.controlChange(128,50); // Volume

two.controlChange(2, 20);   // Stick Hardness
two.controlChange(4, 90);    // Stick Position
two.controlChange(11,20);   // Vibrato Gain
two.controlChange(7, 2);     // Vibrato Frequency
two.controlChange(1, 40);    // Direct Stick Mix
two.controlChange(128,20); // Volume


Std.mtof(57) => one.freq;
Std.mtof(40) => two.freq;

//設定bpm

60=> float BPM;
500 * 60/BPM => float beatDuration; // in millisecond 
0.5=> float sub1division;
1=> int sub2division;
beatDuration/sub1division => float halfbeat;
beatDuration/sub2division => float quatbeat;

fun void beat(){
    while (true){
    1=> one.strike;
    halfbeat  :: ms => now;
    }
}
fun void subbeat(){
    while (true){
    1=> two.strike;
    quatbeat  :: ms => now;
    }
}




[76,78,80,80,81,83,85,87]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,2,4,5,4,5,7,5,4,2,0,2,4,5,7,6] @=> int fadeInOrder[];


fun void melody() {
    while(true){
        for (0 => int j; j < fadeInOrder.cap(); j++) {
            fadeInOrder[j] => int idx;
            Std.mtof(notelist[idx]) => float freq;

            // 判斷是否為長音
            0.125::second => dur noteduration;
            if (j==0||j==3||j==6||j==7||j==14||j==15){
                0.25::second => noteduration;}
            

           // 設定音高與目前總 gain
            for (0 => int i; i < s.cap(); i++) {
                freq => s[i].freq;
                gainArray[i]*0.25  => s[i].gain;
                
            }

            // 播完這個音
            noteduration => now;

            
            }
               

            // 結束這個 note
            for (0 => int i; i < s.cap(); i++) {
                
            }

           1::ms => now;
}
}


spork~beat();// children thread
spork~subbeat();
spork~melody();// children thread
while(true) 1:: second => now; // parent thread
