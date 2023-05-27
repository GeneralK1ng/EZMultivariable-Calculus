# 11.1 Cartesian Coordinates in Three-Space

Cartesian Coordinates are a way of representing points in three-dimensional space using three real numbers. In this system, each point is located at a unique position described by its coordinates, which are measured along three perpendicular axes, typically labeled x, y, and z. These axes are also known as the Cartesian axes.

## Notation and Representation

A point in three-space is represented by an ordered triple `(x,y,z)` of real numbers. The first number, `x`, represents the distance from the point to the `yz-plane`, measured along the `x-axis`. The second number, `y`, represents the distance from the point to the `xz-plane`, measured along the `y-axis`. The third number, `z`, represents the distance from the point to the `xy-plane`, measured along the z-axis.



<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 1 A visualization of Cartesian Coordinates in Three-Space.png" alt="Figure 1 A visualization of Cartesian Coordinates in Three-Space" style="zoom: 50%;" />

## The Distance Formula

In three-dimensional space, we can use the Euclidean distance formula to calculate the distance between two points. Suppose there are two points $A=(x_1,y_1,z_1)$ and $B=(x_2,y_2,z_2)$, the Euclidean distance between them can be expressed as

$$
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}
$$
This formula can be proved by the Pythagorean theorem. We can connect the points $A$ and $B$ into a line segment and assume that the length of this line segment is $d$. Then we project this line onto the three axes to get three line segments, $x_2-x_1$, $y_2-y_1$ and $z_2-z_1$.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 2.png" alt="Figure 2" style="zoom:67%;" />

Next, we can use the Pythagorean theorem to prove the Euclidean distance formula. According to the Pythagorean Theorem, if the two right-angled sides of a right triangle are $a$ and $b$, and the hypotenuse is $c$, then we have $a^2+b^2=c^2$.

We can consider the line segments $x_2-x_1$, $y_2-y_1$ and $z_2-z_1$ as the two right-angled sides of three right triangles, and the hypotenuse is the distance $d$ between the points $A$ and $B$. By the Pythagorean theorem, we have:

$$
(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2=d^2
$$
Squaring both sides of the equation yields the Euclidean distance formula:

$$
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}
$$
Therefore, the Euclidean distance formula can be proved by the Pythagorean theorem.



## Midpoint Formula

The midpoint of a line segment in three-space can be calculated using the midpoint formula:
$$
(x,y,z) = (\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}, \frac{z_1 + z_2}{2})
$$
Where `(x1, y1, z1)` and `(x2, y2, z2)` are the coordinates of the endpoints of the line segment. This formula calculates the coordinates of the point that is equidistant from the two endpoints.

> In conclusion, Cartesian Coordinates in Three-Space provide a way to represent points in three-dimensional space using three real numbers. The distance formula and midpoint formula allow us to calculate distances and midpoints of line segments in three-space. These concepts are essential in the study of multivariable calculus and have many applications in physics, engineering, and other fields.



## Spheres and Their Equations

### Equations

Spheres are a type of three-dimensional object that are defined as the set of all points that are a fixed distance from a given point, called the center. The distance from the center to any point on the sphere is called the radius. In multivariable calculus, we often work with equations that describe the geometry of spheres in three-dimensional space.

The equation of a sphere with center $(a, b, c)$ and radius $r$ is given by:
$$
(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2
$$
This equation can also be written in vector from as:
$$
(\vec{X}-\vec{C})(\vec{X}-\vec{C})=r^2
$$
where $\mathbf{x} = \langle x, y, z \rangle$ is a vector representing a point in three-dimensional space, $\mathbf{c} = \langle a, b, c \rangle$ is the center of the sphere, and $\cdot$ represents the dot product of two vectors.

To derive the equation of a sphere, we start by considering a point $(x, y, z)$ on the surface of the sphere. Since this point is a fixed distance $r$ from the center $(a, b, c)$, we have:
$$
(x-a)^2 + (y-b)^2 + (z-c)^2 = r^2
$$
We can also use this equation to find the center and radius of a sphere given its equation. If we expand the equation, we get:
$$
x^2 - 2ax + a^2 + y^2 - 2by +b^2 + z^2 - 2cz + c^2 = r^2
$$
Comparing this to the general form of a quadratic equation in three variables:
$$
Ax^2 + By^2 + Cz^2 + Dx + Ey + F =0
$$
we can see that the center of the sphere is $(a, b, c)$, and the radius is $\sqrt{a^2+b^2+c^2-r^2}$.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 3 A Sphere.png" alt="Figure 3 A Sphere" style="zoom: 50%;" />

### What is a Sphere?

A sphere can be defined mathematically as a set of points in three-dimensional space that are at a fixed distance, called the radius (r), from a central point, called the center (C).

Using markdown syntax, the equation for a sphere can be written as:
$$
(x - Cx)^2 + (y - Cy)^2 + (z - Cz)^2 = r^2
$$
where `(x, y, z)` are the coordinates of any point on the surface of the sphere, and `(Cx, Cy, Cz)` are the coordinates of the center of the sphere.

Visually, a sphere can be represented as a solid, perfectly round object with no flat sides or edges. It is similar in shape to a ball or a globe. Every point on the surface of the sphere is equidistant from the center, and the distance from the center to any point on the surface is equal to the radius of the sphere.



## Graph in Three-Space

In multivariable calculus, we often work with graphs in three-dimensional space. A graph in three-space is a set of points $(x,y,z)$ that satisfy an equation of the form $z=f(x,y)$, where $f(x,y)$ is a function of two variables. In other words, a graph in three-space is a surface.

To visualize a graph in three-space, we can use a three-dimensional coordinate system with three mutually perpendicular axes: the $x$-axis, the $y$-axis, and the $z$-axis. Each point in three-space is represented by an ordered triple $(x,y,z)$, where $x$ is the horizontal coordinate, $y$ is the vertical coordinate, and $z$ is the depth coordinate. The point where the three axes intersect is called the origin, and is typically labeled $(0,0,0)$.

To graph a surface in three-space, we can use techniques such as level curves and contour plots. Level curves are curves in the $xy$-plane that represent the values of $z$ for which $f(x,y)$ is constant. In other words, they are curves that lie on the surface of the graph. Contour plots are two-dimensional plots that show the level curves of a function in three-space.

To find the equations of level curves, we set $z$ equal to a constant $c$ and solve for $x$ and $y$. For example, if $f(x,y)=x^2+y^2$, the level curves would be given by the equation $x^2+y^2=c$, which represents circles centered at the origin with radius $\sqrt{c}$. To visualize the graph of this function, we could plot a series of these circles at different heights above the $xy$-plane.

Another technique for visualizing graphs in three-space is to use slices. A slice is a cross-section of the graph taken by a plane perpendicular to one of the coordinate planes. For example, if we take a slice of the graph of $z=f(x,y)$ by a plane parallel to the $xy$-plane at a fixed height $z=c$, we obtain the curve $f(x,y)=c$. This curve represents the intersection of the graph with the plane $z=c$, and can be plotted in the $xy$-plane.

Here are some additional mathematical formulas that may be helpful when working with graphs in three-space:

- The distance between two points $(x_1,y_1,z_1)$ and $(x_2,y_2,z_2)$ is given by the formula:

  > $$
  > d = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}
  > $$

- The equation of a plane in three-space can be written in the form $ax+by+cz=d$, where $(a,b,c)$ is the normal vector to the plane and $d$ is the distance from the origin to the plane.

- The dot product of two vectors $\mathbf{u}=\langle u_1,u_2,u_3 \rangle$ and $\mathbf{v}=\langle v_1,v_2,v_3 \rangle$ is given by the formula:

  > $$
  > \vec{u} \cdot \vec{v} = \vec{u_1}\vec{v_1} + \vec{u_2}\vec{v_2} +\vec{u_3}\vec{v_3}
  > $$

- The cross product of two vectors $\mathbf{u}$ and $\mathbf{v}$ is a vector $\mathbf{w}$ that is perpendicular to both $\mathbf{u}$ and $\mathbf{v}$, and is given by the formula:

  > $$
  > \mathbf{U} \times \mathbf{V} =  
  > \begin{vmatrix}  
  > \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  > \vec{u_1}& \vec{u_2}& \vec{u_3}\\  
  > \vec{v_1}& \vec{v_1}& \vec{v_1}\\  
  > \end{vmatrix}
  > $$

- The gradient of a function $f(x,y,z)$ is a vector field that points in the direction of the greatest increase of $f$, and is given by the formula:

  > $$
  > \nabla f (x,y,z)=<\cfrac{\partial f}{\partial x } ,\cfrac{\partial f}{\partial y },\cfrac{\partial f}{\partial z }>
  > $$

- The directional derivative of $f(x,y,z)$ in the direction of a unit vector $\mathbf{u}$ is given by the formula:

  > $$
  > D_uf(x,y,z)=\nabla f(x,y,z) \cdot \vec{u}
  > $$

- The partial derivatives of a function $f(x,y,z)$ can be used to find the equation of the tangent plane to the graph of $f$ at a point $(x_0,y_0,z_0)$, which is given by the equation:

  > $$
  > \cfrac{\partial f}{\partial x }(x_0,y_0,z_0)(x-x_0) +\cfrac{\partial f}{\partial y }(x_0,y_0,z_0)(y-y_0) +\cfrac{\partial f}{\partial z }(x_0,y_0,z_0)(z-z_0) =0
  > $$

These are just a few of the mathematical formulas that are used when working with graphs in three-space. Other techniques and formulas include partial derivatives, double and triple integrals, parametric equations, and vector fields.

When solving problems involving graphs in three-space, it can be helpful to start by visualizing the graph and identifying any symmetries or patterns. From there, we can use techniques such as level curves, slices, and gradients to gain a deeper understanding of the graph and its behavior. We can also use calculus techniques such as partial derivatives and integrals to calculate various properties of the graph, such as its slope, curvature, and volume.



If you don't quite understand this one little section, no matter, because there is a lot of knowledge we haven't covered yet and it's not your problem if you can't read it. In the next study we will slowly delve into the mysteries of multivariable calculus.

So did I make myself clear in this section? Feel free to contact if you have any questions.

# 11.2 Vectors

In mathematics, a vector is a quantity that has both magnitude and direction. Vectors can be represented geometrically by directed line segments, with the length of the line segment representing the magnitude of the vector, and the direction of the line segment representing the direction of the vector.

There are several concepts and terminology involved when working with vectors, including:

- Magnitude: The magnitude of a vector is its length or size. It is denoted by $||v||$ or $|v|$, and is calculated using the Pythagorean theorem: $||v|| = \sqrt{v_1^2 + v_2^2 + ... + v_n^2}$, where $v_1, v_2, ..., v_n$ are the components of the vector.
- Direction: The direction of a vector is given by the angle it makes with a reference axis or plane. Vectors in two dimensions have a direction angle, while vectors in three dimensions have a direction cosine or direction ratios.
- Components: A vector can be represented in terms of its components, which are the projections of the vector onto the coordinate axes. In two dimensions, a vector is represented as $(x,y)$, while in three dimensions it is represented as$ (x,y,z)$.
- Unit vectors: A unit vector is a vector of magnitude 1 that points in the same direction as a given vector. It is denoted by a hat (^) on top of the vector symbol, such as $\hat{v}$.
- Dot product: The dot product of two vectors is a scalar quantity that measures the similarity of their directions. It is denoted by v · w, and is calculated using the formula: $v · w = v_1w_1 + v_2w_2 + ... + v_nw_n$.
- Cross product: The cross product of two vectors is a vector that is perpendicular to both of the input vectors. It is denoted by $v × w$, and is calculated using the formula: $v × w = <v_2w_3 - v_3w_2, v_3w_1 - v_1w_3, v_1w_2 - v_2w_1>$.

Vectors are used in many areas of mathematics and science, including physics, engineering, and computer graphics. They are particularly useful for describing physical quantities such as force, velocity, and acceleration, which have both magnitude and direction.

This is also just some basic concepts, and I believe you should have no problem asking me questions, so let's start formally studying the chapter on vectors.

## Operations on Vectors

1. Vector addition and subtraction: To add two vectors, we simply add their corresponding components. For example, if $v = <v_1, v_2, v_3> $and $w = <w_1, w_2, w_3>$, then $v + w = <v_1+w_1, v_2+w_2, v_3+w_3>$. To subtract one vector from another, we can simply add the negative of the second vector to the first. For example, $v - w = v + (-w)$.

   <img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 3 Vectors addition and subtraction.png" alt="Figure 3 Vectors addition and subtraction" style="zoom:50%;" />

   > The geometric meaning of vector addition is that it represents the displacement resulting from the sequential application of two or more individual displacements. For example, if we start at point $A$ and then travel along vector $v$ to reach point $ B$, and then travel along vector $w$ to reach point $C$, the displacement from $A$ to $C$ is given by the vector$ v + w$.
   >
   > The geometric meaning of vector subtraction is that it represents the displacement required to get from the end point of one vector to the end point of another vector, when the start point of the second vector coincides with the end point of the first vector. For example, if we start at point A and then travel along vector $v$ to reach point $B$, and then travel along vector w to reach point $C$, the displacement from $B$ to $C$ is given by the vector $w - v$.

2. Scalar multiplication: We can multiply a vector by a scalar (a real number). This operation scales the vector by the magnitude of the scalar, and changes its direction if the scalar is negative. For example, if $v = <v1, v2, v3> $and c is a scalar, then $cv = <cv_1, cv_2, cv_3>$.

   <img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 5 Vectors Scalar multiplication.png" alt="Figure 5 Vectors Scalar multiplication" style="zoom:50%;" />

   > Scalar multiplication involves multiplying a vector by a scalar (a real number), which results in either stretching or shrinking the vector, depending on the sign and magnitude of the scalar. If the scalar is positive, the vector gets stretched in the same direction. If the scalar is negative, the vector gets flipped in the opposite direction, and if the scalar is zero, the vector collapses to the origin.

3. Dot product: The dot product measures the similarity of the directions of two vectors. It is defined as v · w = v1w1 + v2w2 + v3w3. Geometrically, it is equal to the product of the magnitudes of the two vectors and the cosine of the angle between them. One useful application of the dot product is finding the angle between two vectors, which can be calculated using the formula $cos\theta = \frac{(v · w) }{(||v|| ||w||)} $.

   <img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 6 Vectors Dot Product.png" alt="Figure 6 Vectors Dot Product" style="zoom:50%;" />

   > The dot product, also known as the inner product, is a scalar quantity that measures the projection of one vector onto another. The geometric meaning of the dot product is that it gives the cosine of the angle between the two vectors, multiplied by their lengths. For example, if we have two vectors v and w, their dot product is defined as $v \cdot w = |v||w|cos\theta$, where |v| and |w| are the lengths of the vectors, and theta is the angle between them.

4. Cross product: The cross product of two vectors is a vector that is perpendicular to both of the input vectors. Its magnitude is equal to the product of the magnitudes of the two vectors and the sine of the angle between them. Geometrically, the cross product can be visualized as the area of the parallelogram formed by the two input vectors. The direction of the cross product can be determined using the right-hand rule.

   <img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 7 Vectors Cross Product.png" alt="Figure 7 Vectors Cross Product" style="zoom:50%;" />

   > Finally, the cross product, also known as the outer product, is a vector quantity that measures the area of the parallelogram formed by two vectors. The geometric meaning of the cross product is that it gives a vector that is perpendicular to both of the input vectors, and whose direction follows the right-hand rule. For example, if we have two vectors $v$ and $w$, their cross product is defined as $v \times w = |v||w|sin\theta n$, where $|v| $and $|w|$ are the lengths of the vectors, theta is the angle between them, and n is a unit vector perpendicular to the plane defined by $v$ and $w$.

5. Unit vectors: A unit vector is a vector of magnitude 1 that points in the same direction as a given vector. We can find a unit vector in the direction of a given vector by dividing the vector by its magnitude. For example, if $v = <v_1, v_2, v_3>$, then the unit vector in the direction of v is given by $u = \frac{v}{||v||}$.



The standard unit vectors are usually denoted by $i$,$ j$, and $k$ and are defined as vectors that have a magnitude of one and point in the positive $x$, $y$, and $z$ directions, respectively. These vectors are used to construct any other vector in three-dimensional space.

Given a vector v with components $(v1, v2, v3)$, we can represent it in terms of its components and standard unit vectors as follows:
$$
v = v_1 i + v_2 j + v_3 k
$$
Here, $v_1$,$ v_2$, and $v_3$ are the scalar coefficients that represent the magnitude of the vector along each of the three axes. The standard unit vectors $i$, $j$, and $k$ represent the direction of the vector along each of the axes.

To add or subtract vectors, we can simply add or subtract their corresponding components. For example, if we have two vectors $v_1$ and $v_2$ with components $(v_1x, v_1y, v_1z)$ and $(v_2x, v_2y, v_2z)$, respectively, then their sum is given by:
$$
v_1 + v_2 = (v_1x + v_2x) i + (v_1y + v_2y) j + (v_1z + v_2z) k
$$
Similarly, their difference is given by:
$$
v_1 - v_2 = (v_1x - v_2x) i + (v_1y - v_2y) j + (v_1z - v_2z) k
$$
To find the magnitude of a vector, we can use the Pythagorean theorem. For a vector v with components $(v1, v2, v3)$, its magnitude is given by:
$$
||v|| = \sqrt{v_1^2 + v_2^2 + v_3^2}
$$
To find the unit vector in the same direction as a given vector v, we can divide the vector by its magnitude:
$$
u = \frac{v}{||v||} 
$$
where u is the unit vector in the direction of $v$.

To find the dot product of two vectors $u$ and $v$, we multiply their corresponding components and then add up the results. Mathematically, the dot product of $u$ and $v$ is given by:
$$
u · v = u_1v_1 + u_2v_2 + u_3v_3
$$
where $u_1$, $u_2$, $u_3$ and $v_1$,$ v_2$,$ v_3$ are the components of $u$ and $v$, respectively.

The dot product is a useful tool for finding the angle between two vectors. If $u$ and $v$ are two vectors, then the angle between them, denoted by $θ$, is given by:
$$
cosθ = \frac {(u · v)}{(||u|| \cdot ||v||)}
$$
To find the cross product of two vectors $u$ and $v$, we first write them as 3-dimensional vectors and then use the determinant to calculate their cross product. Mathematically, the cross product of $u$ and $v$ is given by:
$$
u × v = (u_2v_3 - u_3v_2) i - (u_1v_3 - u_3v_1) j + (u_1v_2 - u_2v_1) k
$$
The cross product is useful for finding the area of a parallelogram formed by two vectors and the volume of a parallelepiped formed by three vectors.

In summary, an algebraic approach to vectors involves representing vectors in terms of their components using standard unit vectors or basis vectors. To add, subtract, find the magnitude, and the unit vector of a vector, we use to add, subtract, find the magnitude, and the unit vector of a vector, we use scalar multiplication, and vector addition/subtraction. To find the dot product of two vectors, we use their components and add them up. To find the cross product of two vectors, we use the determinant of their components.

When solving problems involving vectors, it is important to keep in mind the properties of vectors, such as commutativity and distributivity, and to use algebraic techniques to simplify expressions. Some useful techniques for solving problems involving vectors are:

1. Decomposing vectors: Sometimes, it is useful to decompose a vector into its components along different axes or planes. For example, if a vector $v$ makes an angle $θ$ with the x-axis, then its components along the $x$ and $y$ axes are given by v $cos(θ)$ and $v$ $sin(θ)$, respectively.
2. Projection: The projection of a vector $u$ onto another vector $v$ is the component of $u$ that lies along the direction of $v$. The projection of $u$ onto $v$ is given by:

$$
proj_v(u) = \frac{\vec{u} · \vec{v} }{||\vec{v}||^2} \vec{v}
$$

3. Vector equations: Vector equations can be used to solve systems of equations involving vectors. For example, if we have two vectors u and v, and we know that their sum is equal to another vector w, we can write:

$$
u + v = w
$$

​	   and then solve for either u or v in terms of the other two vectors.

4. Geometric interpretations: Geometric interpretations of vectors can be helpful in visualizing and understanding the problem at hand. For example, the dot product of two vectors can be interpreted as the product of the magnitudes of the vectors and the cosine of the angle between them, while the cross product can be interpreted as the area of the parallelogram formed by the two vectors.

Overall, an algebraic approach to vectors involves representing vectors in terms of their components using standard unit vectors or basis vectors and using algebraic techniques to simplify expressions and solve problems. It is important to keep in mind the properties of vectors and to use geometric interpretations to gain insight into the problem.

# 11.3 The Dot Product

In the previous section 11.3 we learned some basics of vectors and some basic operations of vectors in general, which should not be particularly difficult for everyone at the moment, so in this section we will learn a simple concept mentioned in the previous section in concrete terms, which is really simple, believe me, and that is - $inner -product$.

In multivariable calculus, the inner product, also known as the dot product, is a fundamental concept that plays an important role in many areas of mathematics, physics, and engineering. It is a way of measuring the degree of similarity or alignment between two vectors in a Euclidean space.

The inner product of two vectors is defined as the product of their magnitudes and the cosine of the angle between them. Geometrically, it can be interpreted as the projection of one vector onto the other, multiplied by the magnitude of the other vector. It is denoted by the symbol · or < , >, and can be expressed in terms of the components of the vectors as:
$$
u · v = u_1v_1 + u_2v_2 + ... + u_nv_n
$$
where u and v are vectors in n-dimensional Euclidean space, and $u_1, u_2, ..., u_n$ and $v_1, v_2, ..., v_n$ are their corresponding components.

The dot product satisfies several important properties, such as commutativity $(u · v = v · u)$, distributivity $(u · (v + w) = u · v + u · w)$, and associativity with scalar multiplication $((k u) · v = k (u · v))$, among others. It also allows us to define the magnitude of a vector as the square root of its dot product with itself, i.e., $||u|| = \sqrt{u · u}$.

The inner product has many applications in geometry, physics, and engineering, such as determining the angle between two vectors, finding the projection of one vector onto another, computing work done by a force on an object, and calculating the norm of a matrix, among others.

## Theorems

Next we will learn some necessary theorems, very simple, I try to express the process of proof and description as concise and vivid as possible, if there are doubts, please ask me. If you really can't understand it, but you have to deal with the exam, there is no way, then please memorize these formulas by heart.

### Theorem A: properties of the Dot Product

If $u$, $v$, and $w$ are vectors, and $c$ is a scalar, then

- $u \cdot v = v \cdot u$

- $u \cdot (v + u) = u \cdot v + u \cdot w$
- $c(u \cdot v)=(cu) \cdot v$
- $0 \cdot u = 0$
- $u \cdot u = ||u||^2$

### Theorem B

If $\theta$ is the smallest nonnegative angle between the nonzero vectors $u$ and $v$ , then 
$$
u \cdot v = ||u||||v||cos\theta
$$
$Proof$ 

To prove that $u · v = ||u|| ||v|| cos θ$, we can start by expressing u and v in terms of their components using standard unit vectors or basis vectors. Let $u = (u1, u2, u3) $ and $v = (v1, v2, v3)$, and let θ be the angle between $u$ and $v$.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 8 Dot Product.png" alt="Figure 8 Dot Product" style="zoom:50%;" />

Then, the dot product of $u$ and $v$ can be expressed as:
$$
u · v = u_1v_1 + u_2v_2 + u_3v_3
$$
The magnitudes of u and v can be expressed as:
$$
||u|| = \sqrt{u_1^2 + u_2^2 + u_3^2}
$$

$$
||v|| = \sqrt{v_1^2 + v_2^2 + v_3^2}
$$

Using the properties of the dot product, we can express the cosine of the angle between u and v in terms of their components:
$$
cos θ = \frac{u · v}{||u|| ||v||} 
$$
Substituting $u · v$ and $||u||$ and $||v||$, we get:
$$
cos θ = \frac{u_1v_1 + u_2v_2 + u_3v_3}{\sqrt{u_1^2 + u_2^2 + u_3^2} \sqrt{v_1^2 + v_2^2 + v_3^2}}
$$
Multiplying both sides by $||u|| ||v||$, we get:
$$
||u|| ||v|| cos θ = u_1v_1 + u_2v_2 + u_3v_3
$$
But this is just the expression for $u · v$ that we started with, so we have shown that:
$$
u · v = ||u|| ||v|| cos θ
$$
as desired.

This equation is a fundamental result in linear algebra and has many important applications in geometry, physics, and engineering, such as determining the angle between two vectors, finding the projection of one vector onto another, and calculating work done by a force on an object, among others.

### Theorem C: Perpendicular Criterion

The Perpendicular Criterion theorem states that two vectors in a Euclidean space are perpendicular, or orthogonal, if and only if their dot product is equal to zero.

In other words, if $u$ and $v$ are two vectors in a Euclidean space, then u and v are perpendicular if and only if:
$$
u ⋅ v = 0
$$
Geometrically, this means that the angle between u and v is 90 degrees, since the cosine of a 90 degree angle is zero.

The Perpendicular Criterion theorem is a very useful tool in multivariable calculus and linear algebra, as it allows us to easily determine whether two vectors are perpendicular without having to explicitly calculate their angle or projection. It also has important applications in physics, engineering, and other fields where vectors are commonly used to represent physical quantities.

For example, if we are given the velocity and force vectors of an object in a physical system, we can use the Perpendicular Criterion theorem to determine whether the force is acting perpendicular to the motion of the object, which is important in understanding the dynamics of the system. Similarly, in computer graphics and computer vision, the Perpendicular Criterion theorem is used to calculate lighting and shading effects, as well as to determine the orientation of objects in 3D space.

> $Definition Orthogonal$
>
> Vectors that are perpendicular are said to be orthogonal.



$Proof$

Here's a proof of the Perpendicular Criterion theorem using the definition of the dot product:

Let $u$ and $v$ be two vectors in a Euclidean space. By the definition of the dot product, we have:
$$
u ⋅ v = ||u|| ||v|| cosθ
$$
where $θ$ is the angle between $u$ and $v$.

If $u$ and $v$ are perpendicular, then $θ = 90°$, so $cosθ = 0$, and hence $u ⋅ v = 0$.

Conversely, suppose that $u ⋅ v = 0$. Then we have:

$||u - v||^2 = (u - v) ⋅ (u - v)$

$= u ⋅ u - u ⋅ v - v ⋅ u + v ⋅ v $    (by the distributive property)         

$= ||u||^2 - 2(u ⋅ v) + ||v||^2$    (by the definition of the dot product)         

$= ||u||^2 - 2(0) + ||v||^2    (since u ⋅ v = 0)$        

$= ||u||^2 + ||v||^2$

Since $||u - v||^2$ is the sum of two non-negative numbers, it follows that $||u - v||^2 ≥ 0$, with equality if and only if $u - v = 0$, which means that $u = v$.

Therefore, if $u ⋅ v = 0$, then $u = v$ or $u$ and $v$ are perpendicular.

This completes the proof of the Perpendicular Criterion theorem.

The formula for the Perpendicular Criterion theorem is simply:

$u ⋅ v = 0$ if and only if $u$ and $v$ are perpendicular.



## Direction Angles and Cosines

In multivariable calculus, directional angles and cosines are used to describe the orientation of a vector in three-dimensional space.

Let's consider a vector $\vec{v}$ in three-dimensional space with components $(v_1, v_2, v_3)$. We can define the directional angles of $\vec{v}$ with respect to the positive $x$, $y$, and $z$ axes as follows:

1. The angle $\theta_x$ between $\vec{v}$ and the positive $x$-axis is given by:

$$
cos\theta_x = \frac{v_1}{\sqrt{v_1^2+v_2^2+v_3^2}}
$$

2. The angle $\theta_y$ between $\vec{v}$ and the positive $y$-axis is given by:

$$
cos\theta_y = \frac{v_1}{\sqrt{v_1^2+v_2^2+v_3^2}}
$$

3. The angle $\theta_z$ between $\vec{v}$ and the positive $z$-axis is given by:

$$
cos\theta_z = \frac{v_1}{\sqrt{v_1^2+v_2^2+v_3^2}}
$$

The directional cosines are simply the cosine values of these angles:
$$
cos\theta_x,cos\theta_y,cos\theta_z
$$
It is important to note that the sum of the squares of the directional cosines is always equal to 1:
$$
cos^2\theta_x+cos^2\theta_y+cos^2\theta_z=1
$$
This property is known as the direction cosine theorem.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 9 Relationship between Azimuth Angle and Cosine.png" alt="Figure 9 Relationship between Azimuth Angle and Cosine" style="zoom:50%;" />

Now, let's consider some practical ideas and points to solve problems involving directional angles and cosines:

1. When given a vector in component form, you can use the formulas above to calculate the directional angles and cosines.
2. When given the directional cosines, you can use the direction cosine theorem to check if they are valid.
3. When given two vectors, you can find the angle between them using the dot product and the magnitudes of the vectors. This can be useful in finding the directional angles and cosines of a vector.
4. When given a vector and a plane, you can find the angle between the vector and the normal to the plane using the dot product. This can be useful in finding the directional angles and cosines of the vector with respect to the plane.
5. When given a set of three vectors, you can use the cross product to find the normal to the plane containing two of the vectors. This can be useful in finding the directional angles and cosines of the third vector with respect to the plane.

Overall, the relationship between directional angles and cosines is an important concept in multivariable calculus, as it allows us to describe the orientation of vectors in three-dimensional space. 

## Projection

In mathematics, the projection of a vector onto another vector is the component of the first vector that lies in the direction of the second vector. Geometrically, this means that we are finding the shadow of the first vector on the second vector.

To understand the mathematical principles behind projection, let's first define some terms. Let `u` and `v` be two non-zero vectors in a three-dimensional space. The projection of `u` onto `v` is denoted by `proj_v u`. This is a vector that has the same direction as `v`, but a different magnitude. The magnitude of `proj_v u` is the length of the shadow of `u` on `v`.

The projection of `u` onto `v` is given by the formula:
$$
proj_v u = \frac{u · v}{||v||^2} v
$$
where `·` represents the dot product of two vectors.

This formula can be derived geometrically by noting that the projection of `u` onto `v` is the vector `w` that satisfies the following conditions:

1. `w` is parallel to `v`
2. `w` is collinear with `u`
3. `w` has the same direction as `u`

To find `w`, we can start by drawing a line from the tip of `u` perpendicular to `v`. This creates a right-angled triangle, with `v` as the hypotenuse. The length of the adjacent side of this triangle is the magnitude of `proj_v u`, and the length of the opposite side is the magnitude of the component of `u` perpendicular to `v`. Using trigonometry, we can express these lengths in terms of the dot product `u · v` and the magnitude of `v`. By rearranging these expressions, we arrive at the formula for `proj_v u`.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 10 Projections.png" alt="Figure 10 Projections" style="zoom:50%;" />

Now, let's consider some practical strategies and methods for solving problems involving projection.

One common problem is to find the projection of a vector `u` onto a plane. To do this, we can first find a vector `n` that is perpendicular to the plane. This can be done by taking the cross product of two vectors that lie in the plane. Once we have `n`, we can find the projection of `u` onto `n` using the formula we just discussed. The projection of `u` onto the plane is then obtained by subtracting the projection of `u` onto `n` from `u`.

Another common problem is to find the distance between a point and a line in space. To do this, we can first find a vector `v` that points along the line. This can be done by taking the difference between two points on the line. We can then find the projection of the vector from the point to the line onto `v`. The magnitude of this projection is the distance between the point and the line.

In summary, projection is a fundamental concept in linear algebra that has many practical applications in geometry and physics. By understanding the mathematical principles behind projection and using the appropriate strategies and methods, we can solve a wide range of problems involving vectors in space.



## Planes

In the context of multivariable calculus, planes are important mathematical objects that are used to study functions of two or three variables. Here's a brief overview of some key concepts related to planes:

1. Equation of a Plane: A plane in three-dimensional space can be described by an equation of the form $ax + by + cz = d$, where `a`, `b`, and `c` are constants that define the orientation of the plane, and `d` is a constant that defines the distance of the plane from the origin. This is known as the standard form of the equation of a plane.
2. Normal Vector: The vector $n = <a, b, c>$ is known as the normal vector of the plane. This vector is perpendicular to the plane, and its direction determines the orientation of the plane.
3. Point-Normal Form: Another way to define a plane is using a point and a normal vector. Given a point $P = (x_0, y_0, z_0)$ on the plane and a normal vector $n = <a, b, c>$, the equation of the plane can be written as $n \cdot (r - P) = 0$, where $r = <x, y, z>$ is a point on the plane.
4. Vector Equation of a Line: A line in three-dimensional space can be described by a vector equation of the form `r = p + tv`, where $p = <x_0, y_0, z_0>$ is a point on the line and $v = <a, b, c>$ is a direction vector for the line.
5. Intersection of a Line and a Plane: Given a line with vector equation `r = p + tv` and a plane with equation $ax + by + cz = d$, we can find the point of intersection between the line and the plane by solving the system of equations $ax + by + cz = d$ and $x = x_0 + ta, y = y_0 + tb, z = z_0 + tc$ simultaneously.
6. Distance from a Point to a Plane: Given a plane with equation $ax + by + cz = d$ and a point $P = (x_0, y_0, z_0)$ that is not on the plane, we can find the distance between the point and the plane using the formula $distance = \frac{|ax_0 + by_0 + cz_0 - d|}{\sqrt{a^2 + b^2 + c^2}}  $.

These concepts are all interrelated and are essential for understanding the geometry of planes in three-dimensional space.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 11 Example Plane.png" alt="Figure 11 Example Plane" style="zoom:50%;" />

Good, I believe you already understand the concept of inner product or dot product, and almost understand some geometric meaning of the operation between vectors, and also know how to use these formulas. Then we can move on to a new concept - the outer product or fork product.

Did I explain it to you? If you feel okay, remember to practice it regularly so that you can consolidate your knowledge.

# 11.4 The Cross Product

If you were a Chinese high school student before, I think those previous points of knowledge are estimated to be difficult to beat you at all, if you are a student in the United States Britain or in addition to China, it does not matter, my notes aim to try to make the knowledge become clear to understand easy to understand, if you have questions welcome to contact me! So the concepts you will learn today will be a little more difficult to understand than yesterday, but don't be afraid, follow my steps and learn step by step, then welcome to - Cross Product (Outer Product).

The outer product, also known as the vector or cross product, is a fundamental operation in multivariable calculus that relates two vectors in three-dimensional space. The outer product is used to calculate the vector that is perpendicular to both input vectors, and its magnitude is equal to the area of the parallelogram defined by the two input vectors.

To understand this concept more clearly, let's start with the definition. Given two vectors **a** and **b**, their outer product is denoted by **a** x **b**, and is defined as follows:
$$
a \times b = |a||b|sin(θ) n
$$
where |**a**| and |**b**| are the magnitudes of the two vectors, θ is the angle between them, and **n** is the unit vector that is perpendicular to the plane defined by the two input vectors.

The formula for the outer product may seem complicated, but it is actually quite intuitive once you understand the geometric meaning. Imagine two vectors, **a** and **b**, that are not parallel. The angle between these vectors is θ, and the area of the parallelogram defined by the two vectors is |**a**||**b**|sin(θ). The direction of the perpendicular vector, **n**, is determined by the right-hand rule: point your fingers in the direction of **a**, curl them towards **b**, and the direction of your thumb gives the direction of **n**.

In addition to its geometric meaning, the outer product has many practical applications. For example, it is used in physics to calculate torque, in computer graphics to create 3D models, and in engineering to calculate the forces acting on a structure.

It is also important to note that the outer product is not commutative, meaning that **a** x **b** is not necessarily equal to **b** x **a**. Instead, the order of the vectors matters and determines the direction of the resulting vector.

Lastly, it's worth mentioning that the outer product can be extended to higher dimensions. In four dimensions, for example, the outer product of two vectors is a bivector, which can be thought of as a plane that is perpendicular to both input vectors.

## Third order determinant

Since we are studying multivariable calculus, we are exploring the mysteries of space, so inevitably we need to use some knowledge of linear algebra, and if you have studied linear algebra then you can skip this section. But if you have not learned it does not matter, I will use the most concise language for you to explain the operation of the third-order determinant, n you ask why not talk about the higher order? (Hey, because it's not on the exam.) Because it's not covered before this program.

### What is determinant?

Determinants are mathematical objects that can be calculated from square matrices, which are arrays of numbers arranged in rows and columns. The determinant is a scalar value that is uniquely associated with each matrix and can be used to describe various properties of the matrix, including its invertibility, eigenvalues, and volume scaling factor.

The geometric meaning of a determinant can be interpreted as the factor by which the matrix scales the area or volume of a region in space. For example, the determinant of a 2x2 matrix represents the factor by which the matrix scales the area of a parallelogram, while the determinant of a 3x3 matrix represents the factor by which the matrix scales the volume of a parallelepiped.

### Second order determinant

To explain the concept of determinants, let's start with second-order determinants. A second-order determinant is a scalar value calculated from a 2x2 matrix. The general formula for a second-order determinant is:
$$
\begin{vmatrix}
 a & b\\
  c & d
\end{vmatrix}=ad-bc
$$
The vertical bars represent the determinant notation. To calculate the determinant, we take the product of the diagonal elements (a and d) and subtract the product of the off-diagonal elements (b and c).

Geometrically, a second-order determinant can be interpreted as the signed area of a parallelogram formed by two vectors (a,b) and (c,d) in the plane. If the determinant is positive, the vectors form a counterclockwise orientation, while if it is negative, they form a clockwise orientation.

### Third order determinant

Moving on to third-order determinants, a third-order determinant is a scalar value calculated from a 3x3 matrix. The general formula for a third-order determinant is:
$$
\begin{vmatrix}
 a & b & c\\
 d & e & f\\
 g & h & i
\end{vmatrix}=a(ei - fh) - b(di - fg) + c(dh - eg)
$$
To calculate the determinant, we expand along any row or column and use the formula of second-order determinants to calculate the sub-determinants.

Geometrically, a third-order determinant can be interpreted as the signed volume of a parallelepiped formed by three vectors (a,b,c), (d,e,f), and (g,h,i) in space. If the determinant is positive, the vectors form a right-handed orientation, while if it is negative, they form a left-handed orientation.

In general, determinants can be calculated for any square matrix of any size, and they play a crucial role in many areas of mathematics, including linear algebra, calculus, and differential equations. The geometric interpretation of determinants as scaling factors provides a powerful tool for understanding the behavior of matrices and their applications.

> I hope my narrative can make you understand, if it is still unclear you can go watch YouTube video of linear algebra by 3blue1brown, I believe there will be a more intuitive understanding.

## Cross Product

The cross product is an operation that takes two vectors in three-dimensional space and produces a third vector that is orthogonal to both of the input vectors. The resulting vector is also known as the vector product. The cross product is defined as follows:

If $u = (u_1, u_2, u_3)$ and $v = (v_1, v_2, v_3)$ are two vectors in three-dimensional space, then their cross product is given by:
$$
u \times v = (u_2v_3 - u_3v_2, u_3v_1 - u_1v_3, u_1v_2 - u_2v_1)
$$
Some important concepts related to the cross product are:

- Orthogonality: The cross product of two vectors is orthogonal to both of the input vectors. This means that if u and v are non-zero vectors, then u x v is perpendicular to both u and v.
- Magnitude: The magnitude of the cross product of two vectors is equal to the area of the parallelogram that is formed by the two vectors. That is, $||u \times v|| = ||u|| ||v|| sin(\theta)$, where theta is the angle between `u` and `v`.
- Direction: The direction of the cross product can be determined by using the right-hand rule. If u and v are both pointing towards you and you curl your fingers in the direction of u, then your thumb will point in the direction of `u` x `v`.

Some important formulas related to the cross product are:

- $u \times v = -v \times u$ (cross product is anti-commutative)
- $u \times (v + w) = u \times v + u \times w$  (cross product is distributive over addition)
- $(ku) \times v = k(u \times v) = u \times (kv)$ (cross product is linear in its first argument)

In summary, the cross product is an important operation in multivariable calculus that allows us to find a vector that is orthogonal to two given vectors. It has many practical applications in various fields and can be used to solve a wide range of problems.

### Relationship between the Cross Product and the Determinant

The cross product can be expressed in terms of determinants. Specifically, the cross product of two vectors u and v can be written as:
$$
\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix} =\begin{vmatrix}
 u_2 & u_3\\
 v_2 & v_3
\end{vmatrix}\mathbf{i}-\begin{vmatrix}
 u_1 & u_3\\
 v_1 & v_3
\end{vmatrix}\mathbf{j}+\begin{vmatrix}
 u_1 & u_2\\
 v_1 & v_2
\end{vmatrix}\mathbf{k}
$$
where $i$, $j$, and $k$ are the standard basis vectors in three dimensions.

The formula $\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix} =\begin{vmatrix}
 u_2 & u_3\\
 v_2 & v_3
\end{vmatrix}\mathbf{i}-\begin{vmatrix}
 u_1 & u_3\\
 v_1 & v_3
\end{vmatrix}\mathbf{j}+\begin{vmatrix}
 u_1 & u_2\\
 v_1 & v_2
\end{vmatrix}\mathbf{k}$ is a way to express the cross product of two vectors $u$ and $v$ using determinants. To understand how this formula is derived, it helps to first understand the geometric interpretation of the cross product.

#### Geometric interpretation of cross product

The cross product of two vectors $u$ and $v$ in three dimensions is a third vector $w$ that is perpendicular to both $u$ and $v$. This vector $w$ has a magnitude equal to the area of the parallelogram spanned by $u$ and $v$, and its direction is given by the right-hand rule: point your fingers in the direction of $u$, curl them towards $v$, and your thumb will point in the direction of $w$.

#### Formula derivation:

To derive the formula $\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix}$, we start by considering the cross product of two vectors u and v in component form:
$$
u \times v = (u_2v_3 - u_3v_2, u_3v_1 - u_1v_3, u_1v_2 - u_2v_1)
$$
We can write this vector as a linear combination of the standard basis vectors $i$, $j$, and $k$:
$$
u \times v = (u_2v_3 - u_3v_2)i + (u_3v_1 - u_1v_3)j + (u_1v_2 - u_2v_1)k
$$
Now we can express this as a determinant:
$$
\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix}
$$
If we expand the determinant along the first row, we get:
$$
\mathbf{u} \times \mathbf{v} =\begin{vmatrix}
 u_2 & u_3\\
 v_2 & v_3
\end{vmatrix}\mathbf{i}-\begin{vmatrix}
 u_1 & u_3\\
 v_1 & v_3
\end{vmatrix}\mathbf{j}+\begin{vmatrix}
 u_1 & u_2\\
 v_1 & v_2
\end{vmatrix}\mathbf{k}
$$
which is equivalent to the formula $\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix}$.

#### Geometric meaning of the formula

The determinant $\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix}$ is equal to the volume of the parallelepiped spanned by the three vectors $i$, $u$, and $v$. This is because the first row of the determinant contains the basis vectors $i$, $j$, and $k$, which have unit length and are perpendicular to each other. The second and third rows of the determinant contain the components of $u$ and $v$, respectively, so the parallelepiped they span has a base of area equal to the magnitude of the cross product, and a height equal to the projection of u onto a vector perpendicular to both u and v. The sign of the determinant indicates the orientation of the parallelepiped relative to the standard orientation defined by the basis vectors $i$, $j$, and $k$. Thus, the formula  $\mathbf{u} \times \mathbf{v} =  
\begin{vmatrix}  
  \mathbf{i}& \mathbf{j}& \mathbf{k} \\  
  u_1 & u_2& u_3 \\  
  v_1& v_2& v_3 \\  
\end{vmatrix}$ expresses the cross product as a geometric operation involving volumes and orientations.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 12 u×v.png" alt="Figure 12 u×v" style="zoom:50%;" />

## Theorems

### Theorem A

Let $u$ and $v$ be vectors in three-space and $\theta$ be the angle between them. Then

1. $u \cdot (u \times v) = 0 =v \cdot (u \times v)$, that is, $u \times v$ is perpendicular to both $u$ and $v$;
2. $u$,$v$, and $u \times v$ from a right-handed triple;
3. $||u \times v|| = ||u||||v||sin\theta$

> These theorems I think there should be no difficulty in understanding them with the previous padding, so here I will omit the proof steps, if you have any questions you can contact me!

### Theorem B

Two vectors $u$ and $v$ in three-space are parallel if and only if $u \times v=0$.

The formula that two vectors $u$ and $v$ in three-space are parallel if and only if their cross product $u \times v$ is equal to zero is an important result in multivariable calculus and linear algebra. It essentially states that two vectors are parallel if and only if they lie on the same line or are scalar multiples of each other.

To see why this is true, consider the geometric interpretation of the cross product. The cross product of two non-zero vectors $u$ and $v$ produces a third vector w that is orthogonal (perpendicular) to both $u$ and $v$. The magnitude of $w$ is equal to the area of the parallelogram that u and v span, and its direction is determined by the right-hand rule. If u and v are parallel, then the parallelogram they span has zero area, and therefore the magnitude of the cross product w must also be zero. This means that $u \times v = 0$.

Conversely, if $u \times v = 0$, then the magnitude of the cross product w must be zero, which implies that the area of the parallelogram spanned by $u$ and $v$ is also zero. This means that $u$ and $v$ must be parallel, or equivalently, they lie on the same line or are scalar multiples of each other.

Applications of this formula include:

1. Testing for collinearity: The formula is often used in geometry and physics to determine whether three points in three-space are collinear (lie on the same line). If the cross product of two vectors formed from three points is equal to zero, then the three points are collinear.
2. Solving equations: The formula can be used to solve systems of linear equations in three variables. If two of the equations in the system represent vectors that are parallel, then their cross product is zero, and this information can be used to simplify the system.
3. Finding perpendicular vectors: The formula can also be used to find a vector that is perpendicular to two given vectors. If $u$ and $v$ are non-zero and not parallel, then their cross product $w$ is a vector that is perpendicular to both $u$ and $v$. This can be useful in physics and engineering applications where finding a vector that is perpendicular to two given vectors is important.

### Theorem C

If $u$, $v$, and $w$ are vectors in three-space and $k$ is a scalar, then

1. $u \times v = - (v \times u)$ (anticommutative law);
2. $u \times (v+w) = (u \times v)+(u\times w)$ (left distributive law);
3. $k(u \times v)=(ku)\times v = u\times(kv)$;
4. $u \times 0 = 0 \times u = 0, u \times u = 0$;
5. $(u \times v)\cdot w = u \cdot (v\times u)$;
6. $u \times (v \times w) = (u\cdot w)v-(u\cdot v)w$.



In fact, you will find that this chapter involves nothing more than some formulas, the latter theorems you do not need to remember, because these in the front of the pavement can naturally understand, no need to memorize.

And these few formulas are not necessary to remember, you just need to follow the laws of Cross Product, first count the brackets and then count the brackets outside, I think it should not be difficult.

Next we will enter a more abstract chapter, of course, do not be afraid, I will try to explain as clear and concise as possible for you.

# 11.5 Vector-Valued Functions and Curvilinear Motion

After the previous study, both the operations of vectors and the basic theorems of vectors, you can think of them as tools, that is, they are meant to make you understand and operate better the next knowledge. This chapter may be a little bit difficult, but don't worry, I will try to explain it as simple and detailed as possible.

## Parametric Equations

Let's start with the basics. In single-variable calculus, we often use a single equation to describe a curve in the plane, such as $y = f(x)$. In multivariable calculus, we use a set of equations, called parametric equations, to describe a curve in three-dimensional space.

A parametric equation for a curve is a set of equations that describe the position of a point on the curve as a function of one or more parameters. For example, suppose we want to describe a curve in three-dimensional space. We can use the following parametric equations:
$$
x(t)=cos(t)
$$

$$
y(t)=sin(t)
$$

$$
z(t)=t
$$

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 13 Parametric Equations Example.png" alt="Figure 13 Parametric Equations Example" style="zoom:50%;" />

These equations describe a helix that winds around the $z$-axis. The parameter $t$ is a variable that ranges over some interval, such as $t \in [0, 2\pi]$.



If you find it difficult to accept, you can listen to my next example.

A parametric equation is a way of describing the position of a point using a variable called a parameter. For example, if you want to draw a circle, you can use the equation $x^2 + y^2 = r^2$, where r is the radius of the circle. But this equation only tells you if a point is on the circle or not, it doesn’t tell you how to move along the circle. A parametric equation can do that by using another variable, usually called t, to represent how far you have gone around the circle. One possible parametric equation for a circle is:
$$
x = r cos(t)
$$

$$
y = r sin(t)
$$

This means that the $x$-coordinate of a point on the circle is equal to the radius times the cosine of $t$, and the $y$-coordinate is equal to the radius times the sine of $t$. As t changes from 0 to $2π$, you can trace out the whole circle.

A vivid example of a parametric equation is a roller coaster. Imagine you are riding a roller coaster that goes up and down and left and right. You can use a parametric equation to describe your position at any time. For example, suppose your roller coaster has this parametric equation:
$$
x = 10 cos(t)
$$

$$
y = 10 sin(t)
$$

$$
z = t
$$

This means that your $x$-coordinate is equal to 10 times the cosine of $t$, your $y$-coordinate is equal to 10 times the sine of $t$, and your $z$-coordinate is equal to $t$. As $t$ increases, you move around a circle in the $xy$-plane, but also go up and down along the $z$-axis. You can imagine this as a spiral or a corkscrew shape.

Parametric equations are useful because they can describe curves and surfaces that are hard to express with other types of equations. They also allow you to control how fast or slow you move along the curve or surface by changing the parameter. You can also use more than one parameter if you need to describe more complicated shapes.

## Vector-Valued Functions

### Introduction

A vector-valued function is a function that takes one or more numbers as input and gives a vector as output. A vector is an arrow that has a length and a direction. For example, if you throw a ball in the air, you can describe its position at any time with a vector that points from the origin to the ball. A vector-valued function can tell you how this position vector changes over time.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 14 Ball being thrown in the air.png" alt="Figure 14 Ball being thrown in the air" style="zoom:50%;" />

One way to write a vector-valued function is to use three functions for the $x$, $y$, and $z$ coordinates of the output vector. For example, $r(t) = ⟨x(t), y(t), z(t)⟩$ is a vector-valued function that depends on one variable t. You can think of t as time, and $r(t)$ as the position of an object at time $t$.

To graph a vector-valued function, you can plot the points that the output vector points to for different values of $t$. For example, if $r(t) = ⟨t − 1, t^2⟩$, you can graph it by plugging in different values of t and drawing the points $(t − 1, t^2)$. You can also draw arrows from the origin to these points to show the output vectors.

A simple example of a vector-valued function is $r(t) = ⟨cos(t), sin(t)⟩$. This function describes a circle in the $xy$-plane with radius 1 and center at the origin. The output vector $r(t)$ rotates around the origin as t changes. You can see this by plugging in different values of $t$ and drawing the output vectors.

### Explanation

A vector-valued function is a function that maps a scalar parameter to a vector in some vector space. In the context of multivariable calculus, we use vector-valued functions to describe curves and surfaces in space.

A vector-valued function in three-dimensional space takes the form
$$
r(t) = ⟨x(t), y(t), z(t)⟩
$$
where $x(t)$, $y(t)$, and $z(t)$ are scalar functions of the parameter $t$. The vector $\mathbf{r}(t)$ describes the position of a point on the curve or surface as a function of the parameter $t$.

For example, the helix described by the parametric equations above can be written as a vector-valued function:
$$
r(t) = ⟨cos(t), sin(t),t⟩
$$

## Tangent Vectors and Curvature

Imagine you are riding a bike on a curved road. The road is the curve, and your bike is moving along it. The tangent vector is the direction that your bike is pointing at any moment. It is always touching the curve, but not crossing it. The curvature is a measure of how much the curve bends or twists at any point. The more the curve bends or twists, the higher the curvature is.

For example, if you are riding on a straight road, your tangent vector is always pointing in the same direction, and the curvature is zero. If you are riding on a circular road, your tangent vector is always changing direction as you go around the circle, and the curvature is constant and positive. If you are riding on a wavy road, your tangent vector and curvature change depending on where you are on the wave.

To find the tangent vector and curvature mathematically, we need to use some formulas that involve derivatives and integrals. A derivative is a way of finding how fast something changes, and an integral is a way of finding how much something accumulates. For example, if you know how fast your bike is going (the speed), you can find how far you have traveled (the distance) by using an integral. If you know how far you have traveled (the distance), you can find how fast your bike is going (the speed) by using a derivative.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 15 Tangent Vectors and Curvature.png" alt="Figure 15 Tangent Vectors and Curvature" style="zoom:50%;" />

One of the key concepts in vector-valued functions is the tangent vector. The tangent vector to a curve at a given point is the vector that points in the direction of the curve at that point.

The tangent vector to a vector-valued function $\mathbf{r}(t)$ at a given point $\mathbf{r}(t_0)$ is given by the derivative of the function with respect to the parameter $t$ evaluated at $t_0$:
$$
r'(t_0)=\lim_{h \to 0} \frac{r(t_0+h)-r(t_0)}{h} 
$$
This tangent vector describes the direction and rate of change of the position vector $\mathbf{r}(t)$ at the point $\mathbf{r}(t_0)$.

Another important concept is the curvature of a curve. The curvature measures how much the curve deviates from a straight line at a given point. For a smooth curve, the curvature is given by:
$$
\kappa =\frac{||r'(t)\times r''(t)||}{||r'(t)||^3} 
$$
where $\mathbf{r}'(t)$ and $\mathbf{r}''(t)$ are the first and second derivatives of the vector-valued function with respect to the parameter $t$, respectively.

The curvature is a scalar quantity that measures the rate at which the tangent vector is changing as we move along the curve. A high curvature indicates that the curve is changing direction rapidly, while a low curvature indicates that the curve is changing direction slowly.

## Arc Length

Another important concept in vector-valued functions is arc length. The arc length of a curve is the distance traveled along the curve from one point to another.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 16 Arc Length.png" alt="Figure 16 Arc Length" style="zoom:50%;" />

The arc length of a curve can be calculated using the following formula:
$$
s = \int_{a}^{b} ||r'(t)||dt
$$
where $\mathbf{r}(t)$ is a vector-valued function that describes the curve, and $a$ and $b$ are the starting and ending values of the parameter $t$, respectively. The integral computes the distance traveled by integrating the magnitude of the tangent vector along the curve.

## Unit Tangent and Normal Vectors

In mathematics, a unit tangent vector is a vector that has a length of 1 and is tangent to a curve at a given point. It represents the direction of motion of the curve at that point. The unit normal vector is perpendicular to the unit tangent vector and points towards the center of curvature of the curve at that point.

For example, imagine you are driving a car along a curved road. The unit tangent vector represents the direction you are driving in at any given point along the road, while the unit normal vector represents the direction you would turn if you were to keep driving straight ahead but your car was suddenly lifted off the ground and turned perpendicular to the road.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 17 Tangent and Normal Vectors.png" alt="Figure 17 Tangent and Normal Vectors" style="zoom:50%;" />

The unit tangent vector is a unit vector that points in the direction of the tangent vector. It can be computed as:
$$
\mathrm{T} (t)= \frac{r'(t)}{||r'(t)||} 
$$
The unit normal vector is a unit vector that is orthogonal to the tangent vector and points toward the center of curvature. It can be computed as:
$$
\mathrm{N} (t)= \frac{r''(t)-(r''(t)\cdot \mathrm{T}(t))\mathrm{T}(t) }{||r''(t)-(r''(t)\cdot \mathrm{T(t))\mathrm{T}(t)||}}
$$
The binormal vector is the cross product of the unit tangent and normal vectors:
$$
\mathrm{B}(t)=\mathrm{T}(t)\times \mathrm{N}(t)
$$
Together, the unit tangent, normal, and binormal vectors form a set of orthonormal vectors that are tangent to the curve at each point.

## Curvilinear Motion

Curvilinear motion is the motion of an object that moves along a curved path. For example, when you throw a ball in the air at an angle, it follows a curvilinear motion. Another example is when you ride a bicycle on a circular track, you are also moving in a curvilinear motion.

To understand curvilinear motion better, you can imagine that the object has two components of velocity: one that is tangent to the curve (along the direction of the motion), and one that is normal to the curve (perpendicular to the direction of the motion). The tangent velocity determines how fast the object is moving along the curve, while the normal velocity determines how much the object is changing its direction. The normal velocity also causes an acceleration that is called centripetal acceleration, which pulls the object towards the center of the curve.

For example, when you throw a ball in the air at an angle, it has an initial tangent velocity that makes it go up and forward, and an initial normal velocity that makes it go sideways. As the ball moves along the curve, its tangent velocity decreases due to gravity, while its normal velocity remains constant. This means that the ball slows down as it goes up, and speeds up as it goes down. The normal velocity also causes a centripetal acceleration that makes the ball curve towards the ground.

When you ride a bicycle on a circular track, you have a constant tangent velocity that makes you go around the circle, and a constant normal velocity that makes you lean towards the center of the circle. The normal velocity also causes a centripetal acceleration that keeps you on the circular path. If you increase your tangent velocity, you will need to increase your normal velocity as well to maintain the same centripetal acceleration. This means that you will need to lean more towards the center of the circle.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 18 Curvilinear Motion.png" alt="Figure 18 Curvilinear Motion" style="zoom:50%;" />

Finally, we can use vector-valued functions to describe the motion of a particle in space. If we know the position of a particle as a function of time, we can write:
$$
r(t) = ⟨x(t), y(t), z(t)⟩
$$
where $x(t)$, $y(t)$, and $z(t)$ are functions that describe the position of the particle at time $t$. The velocity of the particle is the derivative of the position vector with respect to time:
$$
\mathrm{v}(t) = \frac{\mathrm{d} r}{\mathrm{d} t}  =\left \langle x'(t), y'(t),z'(t)\right \rangle
$$
The acceleration of the particle is the derivative of the velocity vector with respect to time:
$$
\mathrm{a}(t) = \frac{\mathrm{d} \mathrm{v}}{\mathrm{d} t}  =\left \langle x''(t), y''(t),z''(t)\right \rangle
$$
We can use the concepts of tangent vectors, curvature, and unit normal vectors to analyze the motion of a particle in more detail.

For example, the curvature of the path of a particle gives us an indication of how difficult it is to change the direction of its motion. Similarly, the unit tangent and normal vectors give us information about the direction of motion and the orientation of the particle's path relative to its motion.

# 11.6 Lines and Tangent Lines in Three-Space

## Direction Vectors

In multivariable calculus, we often work with vectors in three-dimensional space (also called "three-space" or "3D space"). One important concept is the direction vector of a line in three-space.

A direction vector is simply a vector that points in the direction of the line. Any nonzero vector parallel to the line can be used as a direction vector. For example, consider the line that passes through the points `(1,2,3)` and `(4,5,6)` in three-space. One possible direction vector for this line is the vector from the first point to the second point:
$$
<4-1, 5-2, 6-3> = <3, 3, 3>
$$
This vector is parallel to the line, since it points in the same direction as the line. However, it is not the only direction vector we could choose - any nonzero scalar multiple of this vector (such as `<6, 6, 6>` or `<-1, -1, -1>`) would also be a valid direction vector.

## Parametric Equations of a Line

Once we have a direction vector for a line in three-space, we can use it to write the parametric equations of the line. The parametric equations give the coordinates of any point on the line in terms of a parameter (usually denoted by `t`).

Suppose we have a line that passes through the point `P = (x0, y0, z0)` and has a direction vector `v = <a, b, c>`. Then the parametric equations of the line are:
$$
x = x_0 + at
$$

$$
y = y_0 + bt
$$

$$
z = z_0 + ct
$$

These equations give the coordinates `(x,y,z)` of any point on the line in terms of the parameter `t`. For example, if `t=0`, we get the point `P`; if `t=1`, we get a point one unit away from `P` in the direction of `v`; if `t=-1`, we get a point one unit away from `P` in the opposite direction of `v`, and so on.



## Tangent Lines and Normal Vectors

Another important concept in multivariable calculus is the tangent line to a curve in three-space. Given a curve (which can be thought of as a set of points in three-space), the tangent line at a particular point on the curve is the line that "best approximates" the curve at that point.

One way to find the tangent line is to use the parametric equations of the curve. Suppose we have a curve with parametric equations $x = f(t)$, $y = g(t)$, and $z = h(t)$. If we want to find the tangent line at the point $(x_0, y_0, z_0)$ on the curve (where $x_0 = f(t_0), y_0 = g(t_0), z_0 = h(t_0)$), we can use the following procedure:

1. Compute the first derivatives of `f`, `g`, and `h` with respect to `t`, evaluated at `t=t0`. These derivatives give the direction of the tangent vector to the curve at the point `(x0, y0, z0)`.
2. Write the parametric equations of the tangent line using the point `(x0, y0, z0)` and the tangent vector from step 1.

The direction of the tangent vector gives us some more information about the behavior of the curve at the point `(x0, y0, z0)`. If the tangent vector points in the same direction as the curve is "moving" at that point, we say the curve is "going up" or "going to the right" (depending on which coordinate is increasing). If the tangent vector points in the opposite direction, we say the curve is "going down" or "going to the left".

We can also use the tangent vector to find another important vector associated with the curve: the normal vector. The normal vector is perpendicular to the tangent vector and points "outward" from the curve. We can find the normal vector by taking the cross product of the tangent vector with any other vector that is not parallel to the tangent vector.

## Symmetric equations

### Introduction

Symmetric equations are a way of representing a line or plane in three-dimensional space using equations that are symmetric in x, y, and z. These equations can be useful for finding the intersection of two or more lines or planes, or for determining whether a given point lies on a given line or plane.

### Equations for lines

The symmetric equations for a line in three-dimensional space are:
$$
\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}
$$
where `(x0, y0, z0)` is a point on the line and `(a, b, c)` is a direction vector for the line. These equations can also be written as:
$$
x = x_0 + at
$$

$$
y = y_0 + bt
$$

$$
z = z_0 + ct
$$

where `t` is a parameter that ranges over all real numbers. These equations give the coordinates of any point on the line in terms of the parameter `t`.

We can also use the symmetric equations to find the direction vector of a line given two points on the line. Suppose we have two points `(x1, y1, z1)` and `(x2, y2, z2)` on the line. Then the direction vector `(a, b, c)` is given by:
$$
a=x_2 - x_1
$$

$$
b=y_2-y_1
$$

$$
c=z_2 - z_3
$$

### Equations for planes

The symmetric equations for a plane in three-dimensional space are:
$$
\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}
$$
where `(x0, y0, z0)` is a point on the plane and `(a, b, c)` is a normal vector to the plane. These equations can also be written as:
$$
ax + by + cz = d
$$
where $d = ax_0 + by_0 + cz_0$. This form of the equation is sometimes called the "general form" of the equation for a plane.

We can also use the symmetric equations to find the normal vector of a plane given three points on the plane. Suppose we have three non-collinear points $(x_1, y_1, z_1)$, $(x_2, y_2, z_2)$, and $(x_3, y_3, z_3)$ on the plane. Then two vectors in the plane are:
$$
u = <x_2 - x_1, y_2 - y_1, z_2 - z_1>
$$

$$
v = <x_3 - x_1, y_3 - y_1, z_3 - z_1>
$$

and the normal vector $(a, b, c)$ is given by:
$$
a = u_2v_3 - u_3v_2
$$

$$
b = u_3v_1 - u_1v_3
$$

$$
c = u_1v_2 - u_2v_1
$$

where $u_i$ and $v_i$ denote the components of vectors $u$ and $v$ respectively.

# 11.7 Curvature and Components of Acceleration

## Curvature

### Introduction

Curvature is a way of measuring how much something bends or curves. For example, a straight line has zero curvature, because it does not bend at all. A circle has a constant curvature, because it bends the same amount everywhere. A curve that bends more has a higher curvature than a curve that bends less.

One way to think about curvature is to imagine a tiny bug crawling along a curve. The bug can only see what is right in front of it, so it does not know the shape of the whole curve. However, it can feel how much it has to turn its body as it moves along. The more it has to turn, the higher the curvature of the curve.

A vivid example of introducing curvature is to use a bicycle wheel. You can hold the wheel in different ways and spin it around. If you hold the wheel flat, like a pizza, then the wheel does not bend at all. It has zero curvature. If you hold the wheel upright, like a coin, then the wheel bends in one direction only. It has positive curvature. If you hold the wheel diagonally, like a saddle, then the wheel bends in two opposite directions. It has negative curvature.

You can also use the bicycle wheel to show how curvature depends on direction. If you hold the wheel upright and spin it around its vertical axis, then you see a circle with positive curvature. But if you spin it around its horizontal axis, then you see a straight line with zero curvature. So the same wheel can have different curvatures depending on how you look at it.

### Explanation

Curvature is a measure of how much a curve deviates from being a straight line. In multivariable calculus, we are usually concerned with curves in three-dimensional space. The curvature of a curve at a particular point is defined as the reciprocal of the radius of the osculating circle at that point. The osculating circle is the circle that best approximates the curve at that point.

### Formula for Curvature

The formula for curvature is:
$$
k = \frac{|T'(s)|}{||r'(s)||}
$$
where `T(s)` is the unit tangent vector to the curve at the point with parameter `s`, `r(s)` is the position vector of the curve at that point, `T'(s)` is the derivative of the tangent vector with respect to `s`, and `||r'(s)||` is the magnitude of the velocity vector.

### Intuition behind the Formula

The curvature measures the rate at which the tangent vector is changing as we move along the curve. If the curve is nearly straight, then the tangent vector doesn't change much, and the curvature is small. If the curve is sharply curved, then the tangent vector changes rapidly, and the curvature is large.

## Components of Acceleration

Components of acceleration are a way of splitting the acceleration vector into two parts: one that is along the direction of motion, and one that is perpendicular to it. The part that is along the direction of motion is called the tangential component, and it tells us how much the speed is changing. The part that is perpendicular to the direction of motion is called the normal component, and it tells us how much the direction is changing.

One way to think about components of acceleration is to imagine a car driving on a curved road. The car has a speedometer that tells us how fast it is going, and a compass that tells us which direction it is facing. The tangential component of acceleration is like the speedometer: it shows us if the car is speeding up or slowing down. The normal component of acceleration is like the compass: it shows us if the car is turning left or right.

A vivid example of introducing components of acceleration is to use a roller coaster. You can feel different forces acting on your body as you ride along the track. When you go up or down a hill, you feel a force pushing you forward or backward. This force is due to the tangential component of acceleration, which changes your speed. When you go around a loop or a curve, you feel a force pushing you sideways or inward. This force is due to the normal component of acceleration, which changes your direction.

You can also use a roller coaster to show how components of acceleration depend on speed and curvature. The faster you go, the greater the tangential component of acceleration will be when you go up or down a hill. The sharper the curve or loop, the greater the normal component of acceleration will be when you go around it.

The binormal vector is a vector that is perpendicular to both the tangent vector and the normal vector of a curve. It is usually denoted by B and it forms an orthonormal basis with T and N, called the Frenet-Serret frame. The binormal vector tells us how much the curve twists out of the plane that contains T and N.

One example of a binormal vector is for a helix, which is a curve that wraps around a cylinder. The tangent vector T is always tangent to the helix, the normal vector N is always pointing towards the axis of the cylinder, and the binormal vector B is always parallel to the axis of the cylinder. The binormal vector does not change its direction as we move along the helix, but it changes its length depending on how tightly the helix is wound. The tighter the helix, the smaller the binormal vector. The length of the binormal vector is related to the torsion of the curve, which measures how fast the curve twists.

<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 19 TNB.png" alt="Figure 19 TNB" style="zoom:50%;" />

### Formula for Tangential Component of Acceleration

The formula for the tangential component of acceleration is:
$$
aT = \frac{dV }{dt}
$$
where `V` is the speed of the object, and $\frac{dV }{dt}$ is the rate of change of speed with respect to time.

### Formula for Normal Component of Acceleration

The formula for the normal component of acceleration is:
$$
aN = ||a|| \times sin(\theta)
$$
where `||a||` is the magnitude of the acceleration vector, and $\theta$ is the angle between the acceleration vector and the unit tangent vector.

### Formula for Binormal Component of Acceleration

The formula for the binormal component of acceleration is:
$$
aB = ||a|| \times cos(\theta) \times k \times N
$$
where `||a||` is the magnitude of the acceleration vector, $\theta$ is the angle between the acceleration vector and the unit tangent vector, `k` is the curvature of the path, and `N` is the unit normal vector to the path.

# 11.8 Surface in Three-Space

Cross sections and traces are two ways of looking at the shapes of 3D objects by cutting them with a plane. A plane is a flat surface that extends infinitely in all directions. Imagine you have a loaf of bread and a knife. You can cut the bread in different ways to get different shapes of slices. Those slices are called cross sections of the bread. For example, if you cut the bread horizontally, you get a rectangular cross section. If you cut it diagonally, you get a trapezoidal cross section. If you cut it vertically, you get a square cross section.

A trace is similar to a cross section, but instead of cutting the object, you just look at where the plane touches the object. For example, if you have a cone and a plane that is parallel to the base of the cone, the trace of the plane on the cone is a circle. If you have a sphere and a plane that goes through the center of the sphere, the trace of the plane on the sphere is a circle too.

Cross sections and traces can help us understand the properties and structures of 3D objects better. They can also help us create 2D drawings of 3D objects by projecting them onto a plane. For example, if you want to draw a cube on a piece of paper, you can use cross sections and traces to find out what shapes you need to draw and how they are connected.

## Cross sections and traces

Before diving into surfaces, it's important to understand the concepts of cross sections and traces, which will be used to describe surfaces in three-space.

A **cross section** is the intersection of a three-dimensional object with a plane. For example, if you cut a cylinder with a plane that is perpendicular to the base, the resulting cross section is a circle.

A **trace** is the intersection of a surface with a plane that is parallel to one of the coordinate planes (i.e. the $xy$, $xz$, or $yz$ plane). For example, if you have a surface that is defined by the equation $z = x^2 + y^2$, the trace in the $xy$ plane (i.e. when $z=0$) is the circle $x^2 + y^2 = 0$.

## Surfaces in three-space

A **surface** in three-space is a two-dimensional object that exists in three-dimensional space. In other words, a surface is a collection of points that can be described by two parameters, usually denoted by $u$ and $v$. The parameters $u$ and $v$ can be thought of as coordinates on the surface, much like $x$ and $y$ are coordinates on a plane.

There are many ways to represent a surface in three-space, but one common way is to use a **parametric representation**. A parametric representation of a surface specifies the coordinates of each point on the surface as a function of the parameters $u$ and $v$.

For example, consider the surface given by the parametric equations:
$$
x=u
$$

$$
y=v
$$

$$
z=u^2+v^2
$$

This surface is a paraboloid that opens upward. The $u$ and $v$ parameters can take on any values, so this surface extends infinitely in all directions.

Another way to represent a surface is to use an **implicit representation**. An implicit representation of a surface is an equation that describes all the points on the surface. For example, the equation $x^2 + y^2 + z^2 = 1$ is an implicit representation of a sphere with radius 1 centered at the origin.



## Tangent planes and normal vectors

Just like a plane in two-dimensional space can be described by a point and a normal vector, a surface in three-space can be described by a point on the surface and a **normal vector**. The normal vector is perpendicular to the surface at the point, and it can be used to define the **tangent plane** to the surface at the point.

After we learn the next chapter we can directly find the equation of the tangent plane inside the surface, but so far we have not learned enough to find it. Therefore, it is important to understand this concept first, and then we can go back to this point after we have learned the powerful tool of partial derivatives.

## Some common 3D geometries

### Cylinders

A cylinder is a surface that consists of all the points that are a fixed distance from a given line called the axis of the cylinder. There are two types of cylinders: circular and elliptical.

#### Circular cylinder

A circular cylinder is a surface that consists of all the points that are a fixed distance from a given line called the axis of the cylinder, and the cross section perpendicular to the axis is a circle. The equation of a circular cylinder with axis along the z-axis and radius r is:
$$
x^2+y^2=r^2
$$

#### Elliptical cylinder

An elliptical cylinder is a surface that consists of all the points that are a fixed distance from a given line called the axis of the cylinder, and the cross section perpendicular to the axis is an ellipse. The equation of an elliptical cylinder with axis along the z-axis, and radii a and b in the x and y directions, respectively, is:
$$
\frac{x^2}{a^2} +\frac{y^2}{b^2}=1
$$

### Quadric Surfaces

A quadric surface is a second-degree surface in three-dimensional space. It is defined by a quadratic equation in three variables x, y, and z. There are several types of quadric surfaces:

#### Sphere

A sphere is a quadric surface that consists of all the points that are a fixed distance from a given point called the center of the sphere. The equation of a sphere with center at (h,k,l) and radius r is:
$$
(x-h)^2+(y-k)^2+(z-l)^2=r^2
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 3 A Sphere.png" alt="Figure 3 A Sphere" style="zoom:50%;" />

#### Ellipsoid

An ellipsoid is a quadric surface that is similar to a sphere, but its shape is determined by three different radii. The equation of an ellipsoid with center at (h,k,l) and radii a, b, and c in the x, y, and z directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}+\frac{(z-l)^2}{c^2}=1
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 20 Ellipsoid.png" alt="Figure 20 Ellipsoid" style="zoom:50%;" />

#### Hyperboloid of one sheet

A hyperboloid of one sheet is a quadric surface that consists of two mirror-image sheets, each of which is hyperboloid in shape. The equation of a hyperboloid of one sheet with center at (h,k,l) and radii a, b, and c in the x, y, and z directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}-\frac{(z-l)^2}{c^2}=1
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 21 Hyperboloid of one sheet.png" alt="Figure 21 Hyperboloid of one sheet" style="zoom:50%;" />

#### Hyperboloid of two sheets

A hyperboloid of two sheets is a quadric surface that consists of two mirror-image sheets, each of which is hyperboloid in shape. The equation of a hyperboloid of two sheets with center at (h,k,l) and radii a, b, and c in the x, y, and z directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}-\frac{(y-k)^2}{b^2}-\frac{(z-l)^2}{c^2}=1
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 22 Hyperboloid of two sheets.png" alt="Figure 22 Hyperboloid of two sheets" style="zoom:50%;" />

#### Elliptic cone

An elliptic cone is a quadric surface that consists of all the points that are a fixed distance from a given point called the vertex of the cone, and the cross section perpendicular to the axis is an ellipse. The equation of an elliptic cone with vertex at (h,k,l) and semi-axes a and b in the x and y directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=\frac{(z-l)^2}{c^2}
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 23 Elliptic Cone.png" alt="Figure 23 Elliptic Cone" style="zoom:50%;" />

#### Elliptic paraboloid

An elliptic paraboloid is a quadric surface that is shaped like a bowl, and its cross section perpendicular to the axis is an ellipse. The equation of an elliptic paraboloid with vertex at (h,k,l) and semi-axes a, b, and c in the x, y, and z directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=\frac{z-l}{c}
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 24 Ellipitic Paraboloid.png" alt="Figure 24 Ellipitic Paraboloid" style="zoom:50%;" />

#### Hyperbolic paraboloid

A hyperbolic paraboloid is a quadric surface that is shaped like a saddle, and its cross section perpendicular to the axis is a hyperbola. The equation of a hyperbolic paraboloid with vertex at (h,k,l) and semi-axes a, b, and c in the x, y, and z directions, respectively, is:
$$
\frac{(x-h)^2}{a^2}-\frac{(y-k)^2}{b^2}=\frac{z-l}{c}
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 25 Hyperbolic Paraboloid.png" alt="Figure 25 Hyperbolic Paraboloid" style="zoom:50%;" />

### Other Surfaces

There are other surfaces in three-space that don't fit into the categories of cylinders or quadric surfaces:

#### Plane

A plane is a flat surface that extends infinitely in all directions. The equation of a plane with normal vector $\vec{n}=(a,b,c)$ and containing a point $(x_0,y_0,z_0)$ is:
$$
a(x-x_0)+b(y-y_0)+c(z-z_0)=0
$$

#### Torus

A torus is a surface that is shaped like a donut. The equation of a torus with center at (h,k,l), major radius R, and minor radius r is:
$$
(\sqrt{x^2+y^2}-R)^2+z^2=r^2
$$
<img src="D:/Information/Book/Math/Notes/Chapter 11 Geometry in Space and Vectors/Figure/Figure 26 Torus.png" alt="Figure 26 Torus" style="zoom:50%;" />

These are just a few examples of the types of surfaces that can be encountered in multivariable calculus. Understanding these surfaces and their equations is important for visualizing and analyzing functions of multiple variables in three-dimensional space.