from .points import Point


POINT_PAIRS = [
    (Point.HEAD, Point.NECK),
    (Point.NECK, Point.R_SHOULDER),
    (Point.R_SHOULDER, Point.R_ELBOW),
    (Point.R_ELBOW, Point.R_WRIST),
    (Point.NECK, Point.L_SHOULDER),
    (Point.L_SHOULDER, Point.L_ELBOW),
    (Point.L_ELBOW, Point.L_WRIST),
    (Point.NECK, Point.CHEST),
    (Point.CHEST, Point.R_HIP),
    (Point.R_HIP, Point.R_KNEE),
    (Point.R_KNEE, Point.R_ANCKLE),
    (Point.CHEST, Point.L_HIP),
    (Point.L_HIP, Point.L_KNEE),
    (Point.L_KNEE, Point.L_ANCKLE),
]