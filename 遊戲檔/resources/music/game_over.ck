SinOsc s[6]=>dac;
for (0 => int i; i < s.cap(); i++) 
    {
        s[i] => dac;
}

ModalBar one => dac;
ModalBar two => dac;
1=> one. preset;//樂器
4=> two. preset;
one.controlChange(2, 60);   // Stick Hardness
one.controlChange(4, 20);    // Stick Position
one.controlChange(11,50);   // Vibrato Gain
one.controlChange(7, 10);     // Vibrato Frequency
one.controlChange(1, 50);    // Direct Stick Mix
one.controlChange(128,90); // Volume

two.controlChange(2, 60);   // Stick Hardness
two.controlChange(4, 10);    // Stick Position
two.controlChange(11,50);   // Vibrato Gain
two.controlChange(7, 2);     // Vibrato Frequency
two.controlChange(1, 50);    // Direct Stick Mix
two.controlChange(128,30); // Volume


Std.mtof(48) => one.freq;
Std.mtof(43) => two.freq;

//設定bpm

60=> float BPM;
1000 * 60/BPM => float beatDuration; // in millisecond 

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




[60,62,63,65,67,68,71,72]@=> int notelist[];
[0.3,0.2,0.1,0.1,0.1,0.1]@=> float gainArray[];
[0,1,2,4,3,2,1,0,2,3,5,4,3,2,1,2] @=> int fadeInOrder[];


fun void melody() {
    while(true){
        for (0 => int j; j < fadeInOrder.cap(); j++) {
            fadeInOrder[j] => int idx;
            Std.mtof(notelist[idx]) => float freq;

            // 判斷是否為長音
            0.25::second => dur noteduration;
            if (j==0||j==1||j==6||j==8||j==10){
                0.5::second => noteduration;}
            else if (j==2){
                0.75::second => noteduration;}
            else if (j==7||j==9||j==15){
            1::second => noteduration;
                }
        
            

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
