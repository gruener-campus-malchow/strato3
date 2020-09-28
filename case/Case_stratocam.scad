difference(){
    cube([0.5, 27,28]); //2mm more z-axes
    translate([-1,1+8.5,7.5])cube([3, 8.1,8.1]);
}

translate([1.5,3,7.5]) {
    rotate([0,90,0]) cylinder(3, 1,1, $fn=30, true);
    translate([-0.5,0,0]) rotate([0,90,0]) cylinder(1, 1.5,1.5, $fn=30, true);
}

translate([1.5,3,7.5+12.5]) {
    rotate([0,90,0]) cylinder(3, 1,1, $fn=30, true);
    translate([-0.5,0,0]) rotate([0,90,0]) cylinder(1, 1.5,1.5, $fn=30, true);
}

translate([1.5,3+21,7.5+12.5]) {
    rotate([0,90,0]) cylinder(3, 1,1, $fn=30, true);
    translate([-0.5,0,0]) rotate([0,90,0]) cylinder(1, 1.5,1.5, $fn=30, true);
}

translate([1.5,3+21,7.5]) {
    rotate([0,90,0]) cylinder(3, 1,1, $fn=30, true);
    translate([-0.5,0,0]) rotate([0,90,0]) cylinder(1, 1.5,1.5, $fn=30, true);
}

difference(){
    cube([70, 27,0.5]);
    union(){
        translate([5,2,-0.5])cube([20, 27-4,1.5]);
        translate([5+25,2,-0.5])cube([20, 27-4,1.5]);
    }
}

translate([8,3,1.5]) {
    cylinder(3, 1.5,1.5, $fn=30, true);
    translate([0,0,-0.5]) cylinder(1, 2,2, $fn=30, true);
}

translate([8+58,3,1.5]) {
    cylinder(3, 1.5,1.5, $fn=30, true);
    translate([0,0,-0.5]) cylinder(1, 2,2, $fn=30, true);
}

translate([8,3+23,1.5]) {
    cylinder(3, 1.5,1.5, $fn=30, true);
    translate([0,0,-0.5]) cylinder(1, 2,2, $fn=30, true);
}

translate([8+58,3+23,1.5]) {
    cylinder(3, 1.5,1.5, $fn=30, true);
    translate([0,0,-0.5]) cylinder(1, 2,2, $fn=30, true);
}