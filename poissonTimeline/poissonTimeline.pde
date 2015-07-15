float time = 0;
int y = 5;

void setup() {
  size(1200,200);
  background(255);
}

void draw() {
  fill(0);
  ellipse(time*100,y,5,5);
  poisson(7);
  if(time > 12) {
    time -= 12;
    y += 5;
    if(y>200) {
      clear();
      y = 5;
      background(255);
    }
  }
  delay(10);
}

float poisson(float LAMBDA) {
  time += -log(1 - random(1))/LAMBDA;
  return time;
}
