ArrayList<Point> points = new ArrayList<Point>();
int LAMBDA = 5;
int p1,p2;
float ran;
int[] ranPoints = new int[2];
float[] chosenPoint = new float[2];
boolean goodPoint = true;
int WIDTH = 800;
int HEIGHT = 800;
FloatList CUMU = new FloatList();
int iter = 0;

class Point {
  float x,y;
  boolean active = true;
  Point (float xin, float yin) {
    x = xin;
    y = yin;
  }
  float distanceFrom(float x2, float y2) {
    return sqrt(sq(x-x2)+sq(y-y2));
  }
  void display(float size) {
    ellipse(x,y,size,size);
  }
}

void setup() {
  frameRate(30);
  size(HEIGHT,WIDTH);
  ellipseMode(RADIUS);
  points.add(new Point(400,400));
  points.add(new Point(400+sqrt(0.5*sq(LAMBDA)),400+sqrt(0.5*sq(LAMBDA))));
  // Generate Poisson Cumulative Table
  CUMU.append(0);
  int k = 0;
  float prev = 0;
  while(true) {
    float next = getPoisson(LAMBDA,k);
    float newp = CUMU.get(CUMU.size()-1) + next;
    if(newp == prev || newp>1) {
      CUMU.append(1);
      break;
    } else {
      CUMU.append(newp);
      prev = newp;
    }
    k++;
  }
  CUMU.remove(0);
  /*for(int i=0;i<CUMU.size();i++) {
    println(CUMU.get(i));
  }*/
}

void draw() {
  // Remove the previous stuff
  clear();
  background(255,255,255);
  noFill();
  // OK, let's go!
  // Now show off what we've got:
  for (Point p : points) {
    // During an enhanced for loop
    // Do not edit the contents of points!
    if(p.active) {
      fill(0,200,0);
    } else {
      fill(0,0,255);
    }
    p.display(5);
  }
  noFill();
  // First, select two different random points:
  ranPoints[0] = -1;
  ranPoints[1] = -1;
  while(ranPoints[0] == -1) {
    ran = poissonInterval(LAMBDA,500);
    ranPoints = randomPoints(ran);
  }
  // Draw circles with our current Poisson val:
  points.get(ranPoints[0]).display(ran);
  points.get(ranPoints[1]).display(ran);
  // OK, cool graphical bit done, now work out
  // where the intersections are using the
  // FORMULA OF DOOOOOOM
  // And add them if we like them.
  addNewPoints(ranPoints,ran,true);
  addNewPoints(ranPoints,ran,false);
  iter++;
}

void addNewPoints(int[] ranPoints,float ran,boolean plus) {
  Point a = points.get(ranPoints[0]);
  Point b = points.get(ranPoints[1]);
  chosenPoint = doom(a,b,ran,plus);
  if(chosenPoint[0] != -1) {
    fill(255,0,0);
    ellipse(chosenPoint[0],chosenPoint[1],5,5);
    line(a.x,a.y,b.x,b.y);
    goodPoint = true;
    if(!(chosenPoint[0]>0 && chosenPoint[0]<HEIGHT && chosenPoint[1]>0 && chosenPoint[1]<WIDTH)) {
      goodPoint = false;
    }
    for (Point p : points) {
      if(p.distanceFrom(chosenPoint[0],chosenPoint[1])<(0.8*ran)) {
        goodPoint = false;
        break;
      }
    }
    if(goodPoint) {
      points.add(new Point(chosenPoint[0],chosenPoint[1]));
    }
  }
}

int poisson(int LAMBDA,int multi) {
  //return LAMBDA; // OH GOD TEMPORARY
  float r = random(1);
  int k = 0;
  while(true) {
    if(r<CUMU.get(k)) {
       if(k>0) return k*multi;
       k=-1;
       r = random(1);
    }
    k++;
  }
}

float poissonInterval(int LAMBDA, int multi) {
  return -log(1-random(1))*multi/LAMBDA;
}

int[] randomPoints(float pois) {
  // Change so one random is selected,
  // then get a nearby one
  int lowerEnd = points.size()-50;
  if(lowerEnd<0) lowerEnd = 0;
  p1 = int(random(lowerEnd,points.size()));
  p2 = int(random(lowerEnd,points.size()));
  // Why not points.size()-1?
  // Well, int truncates things.
  // And random() doesn't include the upper bound.
  int loops = 0;
  while (p1 == p2 || points.get(p1).distanceFrom(points.get(p2).x,points.get(p2).y) >= pois) {
    p2 = int(random(0,points.size()));
    if(loops > 10) {
      int[] output = {-1,-1};
      return output;
    }
    loops++;
  }
  int[] output = {p1,p2};
  return output;
}

float[] doom(Point p1, Point p2, float ran, boolean plus) {
  // thanks http://paulbourke.net/geometry/circlesphere/!
  float d = p1.distanceFrom(p2.x,p2.y);
  if(d > 2*ran) {
    float[] out = {-1,-1};
    return out; // no intersections
  }
  float a = d/2;
  float h = sqrt(sq(ran)-sq(a));
  float x2 = p1.x + (a * (p2.x-p1.x))/d;
  float y2 = p1.y + (a * (p2.y-p1.y))/d;
  fill(0,0,255);
  ellipse(x2,y2,5,5);
  if(plus) {
    float x3 = x2 + (h * (p2.y-p1.y)/d);
    float y3 = y2 - (h * (p2.x-p1.x)/d);
    float[] out = {x3,y3};
    return out;
  } else {
    float x3 = x2 - (h * (p2.y-p1.y)/d);
    float y3 = y2 + (h * (p2.x-p1.x)/d);
    float[] out = {x3,y3};
    return out;
  }
}

float getPoisson(int L,int k) {
  return exp(-L) * (pow(L,k)/fact(k));
}

int fact(int k) {
  int tot = 1;
  for(int i=1;i<=k;i++) {
    tot *= i;
  }
  return tot;
}
