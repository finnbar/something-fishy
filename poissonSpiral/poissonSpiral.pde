float gradientReciprocal = -10;
int sx = 250;
int sy = 250;
int x,y;
FloatList outs = new FloatList();
int LAMBDA = 5;
int t = 0;
int multi = 5;
int xmulti = 1;

void setup() {
  size(500,500);
  x = sx;
  y = sy;
  clear();
  background(255);
  println("READY");
}

void draw() {
  fill(0);
  float[] res = poisson(LAMBDA);
  for(float f : res) {
    x += (f+t)*multi*xmulti;
    y += (1/gradientReciprocal)*(f+t)*multi;
    if(x > 500 || y > 500 || x < 0 || y < 0) {
      x = sx;
      y = sy;
      t = 0;
      gradientReciprocal/=2;
      if(abs(gradientReciprocal) < 0.0625) {
        if(xmulti == -1) {
          if(gradientReciprocal > 0) {
            gradientReciprocal = -10;
            clear();
            background(255);
          } else {
            gradientReciprocal = 10;
            xmulti = 1;
          }
        } else {
          if(gradientReciprocal > 0) {
            gradientReciprocal = -10;
          } else {
            gradientReciprocal = 10;
            xmulti = -1;
          }
        }
      }
    }
    ellipse(x,y,multi,multi);
  }
  t++;
}

float[] poisson(float l) {
  float t = 0;
  outs.clear();
  while(t<1) {
    t += -log(1 - random(1))/l;
    outs.append(t);
  }
  float[] res = new float[outs.size()];
  for(int i=0;i<outs.size();i++) {
    res[i] = outs.get(i);
  }
  return res;
}
