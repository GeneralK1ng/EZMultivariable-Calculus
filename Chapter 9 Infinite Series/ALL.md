# 前言

我非常高兴能够与你们分享这份多元微积分的笔记，这是我个人整理的一份学习资料，旨在帮助你们更好地掌握这门重要而又有趣（bushi）的学科。

多元微积分是数学中的一门关键学科，它探索了多变量函数的性质、曲线与曲面的几何特征以及在实际问题中的应用。对于各位而言，掌握多元微积分不仅是学业发展的重要一环，更是在西浦大一中经历最难的一门数学课（）。

然而，学习多元微积分并不总是一件容易的事情。在这个过程中，我们常常会遇到各种挑战和困惑。因此，我希望这份笔记能够成为你们学习的有力辅助工具，为你们提供清晰而系统的概念解释、详细的计算步骤以及一些常见问题的解答。我尽力确保这份笔记的准确性和易于理解性，但由于个人编辑，难免存在一些漏洞和错误。因此，我非常欢迎你们指出任何问题或提供宝贵的建议，以帮助我不断改进和完善这份学习资料。

要记住多元微积分是一门需要动手实践的学科。除了理论知识，更重要的是通过大量的练习和实际问题的应用来巩固所学的内容。可以搭配上课老师给的习题来进行练习，希望这份笔记能够激发你们的思考和探索欲望，帮助你们培养解决问题的能力。

而且因为本人是MTH004的学生，可能不能完全覆盖各个课程的学生，如果有学愿意补充也非常欢迎！

最后，我想对你们表达真诚的祝愿。希望这份多元微积分的笔记能够成为你们学习路上的良友，帮助你们克服困难，取得优秀的成绩。无论你们是初学者还是已经掌握了一定知识的学生，我都相信这份笔记能够为你们提供一些价值。愿你们在多元微积分的世界中畅行无阻，不断进步。

祝愿你们在学习中取得丰硕的成果！

衷心致意，

General_K1ng

[toc]



# 9.1 Infinite Series

Let's spice things up! We've got a scoop for you: sequences are ordered sets of terms, and when you add them all together, you've got yourself a series. Now, hold on to your hats because we're about to dive into the wild world of infinite series and how they relate to sequences. Get ready to learn about what it means for a series to converge or diverge – it's about to get crazy!

But wait, there's more! We can't forget about the geometric series, one of the most important types of series out there. Trust us, you'll be seeing this bad boy in action in the next chapter, where we'll be using it to write certain functions as polynomials with an infinite number of terms. This is a crucial process because it allows us to evaluate, differentiate, and integrate complicated functions using polynomials that are easier to handle.

Oh, and don't even get us started on the harmonic series – arguably the most interesting divergent series out there. Why is it so fascinating, you ask? Because it just fails to converge, and that's pretty darn cool if you ask us. So, buckle up and get ready to go on a wild ride through the infinite world of series and sequences!

## Introduction to Infinite Series

Infinite series are a fundamental concept in calculus, particularly in the field of analysis. An infinite series is simply the sum of an infinite sequence of terms. For example, the infinite series
$$
{\textstyle \sum_{n=1}^{\infty }} \frac{1}{n^2}=1+\frac{1}{4}+\frac{1}{9}+\frac{1}{16}+···
$$
is the sum of the sequence of terms $\frac{1}{n^2}$ for $n=1,2,3,\ldots$.

Infinite series can be used to approximate functions, solve differential equations, and explore the properties of functions. However, it's important to understand the convergence and divergence of an infinite series before using it in any calculations.

### Explicit Formula

Explicit formula refers to a mathematical formula or expression that directly gives the value of any term in a sequence or series, without having to calculate the preceding terms. It is also called a closed form solution.

For example, the explicit formula for the nth term of a arithmetic sequence with a common difference of d and a first term of a can be written as:
$$
a_n = a + (n-1)d
$$
Similarly, the explicit formula for the nth term of a geometric sequence with a common ratio of r and a first term of a can be written as:
$$
a_n = a × r^{n-1}
$$
Having an explicit formula can be very helpful in solving problems involving sequences and series, as it allows for quick and efficient calculations of any term in the sequence without having to compute all the preceding terms.

### Recursion Formula

Recursion formula, also known as recurrence relation, is a mathematical formula that defines each term of a sequence or series in terms of one or more preceding terms. In other words, it is a formula that relates each term of a sequence to the ones that come before it.

For example, the Fibonacci sequence is defined recursively as:
$$
F_n = F_n-1 + F_n-2
$$
where $F_1 = 1$ and $F_2 = 1$. This means that each term of the sequence (starting from the third term onwards) is the sum of the two preceding terms.

Another example is the arithmetic sequence, which can be defined recursively as:
$$
a_n = a_n-1 + d
$$
where $a_1$ is the first term of the sequence and d is the common difference.

Recursion formulas are useful in mathematics as they can often be used to generate a sequence more efficiently than explicitly computing each term, and can also provide insights into the properties of a sequence or series.

## Convergence and Divergence

An infinite series is said to be *convergent* if the sum of its terms approaches a finite value as the number of terms in the series approaches infinity. On the other hand, if the sum of the terms of a series approaches infinity, the series is said to be *divergent*.

For example, the harmonic series
$$
{\textstyle \sum_{n=1}^{\infty }} \frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+···
$$
is a well-known divergent series, while the geometric series
$$
{\textstyle \sum_{n=1}^{\infty }} r^n=1+r+r^2+r^3+···
$$
is convergent if $|r|<1$ and divergent if $|r| \geq 1$.

<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_1.png" style="zoom:72%;" />

> The graph illustrates the convergence of a simple infinite series, $\sum_{n=1}^{\infty} \frac{1}{n^2}$. The blue curve represents the partial sums of the series up to the first 1000 terms, while the red dashed line represents the limit of the series, which is $\frac{\pi^2}{6}$. As we can see from the graph, as the number of terms in the partial sum increases, the sum gets closer to the limit of the series, indicating that the series converges. The x-axis represents the number of terms in the partial sum, while the y-axis represents the value of the partial sum or the limit of the series. 

## Tests for Convergence

There are several tests that can be used to determine the convergence or divergence of an infinite series, including the comparison test, the limit comparison test, the ratio test, the root test, and the alternating series test. These tests are used to determine if the series is absolutely convergent, conditionally convergent, or divergent.

Understanding infinite series is essential for many applications in calculus, and it's important to have a good grasp of the convergence and divergence of a series before using it in any calculations.

### Why Do We Care About Convergence and Divergence of Infinite Series?

Infinite series are important in many areas of mathematics and science, but not all series converge to a finite limit. Understanding whether a series converges or diverges is crucial in many applications, including physics, engineering, and computer science.

For example, consider the series:
$$
\sum_{n=1}^{\infty} \frac{1}{n^2}
$$
This series is known as the "Basel problem", named after the Swiss mathematician who posed the question of finding the sum of this series. Surprisingly, the sum of this series is a finite value, approximately equal to 1.644934. This value is known as the Basel constant, and it appears in many areas of mathematics, including number theory and probability theory.

On the other hand, consider the series:
$$
\sum_{n=1}^{\infty} \frac{1}{n}
$$
This series is known as the harmonic series, and it is an example of a divergent series. This means that the sum of the series goes to infinity as the number of terms increases. This is an important result, as it shows that even though the individual terms of the series get smaller and smaller, their sum can still be infinite.

Knowing whether a series converges or diverges is also important in numerical analysis and computational methods. For example, in numerical integration, we use methods that approximate the sum of a series to a certain degree of accuracy. If we know that a series converges, we can use these methods confidently and obtain accurate results. However, if a series diverges, these methods may fail and lead to incorrect or unreliable results.

Therefore, understanding the convergence and divergence of infinite series is crucial in many areas of mathematics and science, and it allows us to make accurate predictions, solve important problems, and develop new computational methods.

## Absolute Convergence and Conditional Convergence

An infinite series is said to be *absolutely convergent* if the sum of the absolute values of its terms converges. If the sum of the absolute values of the terms diverges, but the original series still converges, the series is said to be *conditionally convergent*.

For example, the alternating harmonic series
$$
\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+···
$$
is conditionally convergent, since the sum of the absolute values of its terms (the regular harmonic series) diverges, but the original series converges.

<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_2.png"  />

## Power Series

A *power series* is an infinite series of the form
$$
{\textstyle \sum_{n=0}^{\infty}} c_nx^n=c_0+c_1x+c_2x^2+c_3x^3+···
$$
where $x$ is a variable and $c_n$ are constants. Power series are a useful tool in calculus, particularly for representing functions as infinite series.

## Conclusion

Infinite series are a fascinating and important topic in calculus. Understanding the convergence and divergence of a series is crucial for many applications, and there are several tests that can be used to determine the convergence of a series. Absolute and conditional convergence are also important concepts to understand. Finally, power series are a powerful tool for representing functions as infinite series.



This section mainly introduces what concepts we will cover in this chapter on infinite series, and it doesn't matter if you don't understand some of them, because I will focus on them in detail later in the lecture.

# 9.2 Properties of infinite series

Welcome to the fascinating world of infinite series! In this chapter, we will explore the properties of infinite series, including convergence, divergence, and the algebraic operations we can perform on series. Understanding these properties is crucial in many areas of mathematics and science, and it allows us to make accurate predictions, solve important problems, and develop new computational methods. So, let's dive in and discover the amazing properties of infinite series together!

## A few important infinite series

 In addition to exploring the properties of infinite series, we will also introduce and study some of the most important series in mathematics. These include the geometric series, which has many important applications in calculus, and the harmonic series, which is a classic example of a divergent series. We will also study other important series, such as the alternating series and the Taylor series, which have wide-ranging applications in many areas of mathematics and science. So, get ready to explore not only the properties of infinite series, but also some of the most important series in mathematics!

### Geometric Series

A *geometric series* is a special type of infinite series where each term is a constant multiple of the previous term. The general form of a geometric series is
$$
{\textstyle \sum_{n=0}^{\infty }}ar^n=a+ar+ar^2+ar^3+···
$$
where $a$ is the first term and $r$ is the common ratio. Geometric series are important in mathematics and have many applications in science and engineering.

#### Derivation of the General Formula

To derive a formula for the sum of a geometric series, we start by considering the partial sums of the series. Let $S_n$ be the sum of the first $n$ terms of the series, so
$$
S_n=a+ar+ar^2+a^3+\cdots + ar^{n-1}
$$
We can multiply both sides of this equation by $r$ to get
$$
rS_n=ar+ar^2+a^3+\cdots + ar^n
$$
Subtracting the second equation from the first, we get
$$
S_n -rS_n=a-ar^n
$$
which simplifies to
$$
(1-r)S_n=a(1-r^n)
$$
If $r\neq 1$, we can divide both sides by $(1-r)$ to get
$$
S_n=\frac{a(1-r^n)}{1-r}
$$
This formula gives the sum of the first $n$ terms of the geometric series.

To find the sum of the infinite geometric series, we take the limit as $n$ goes to infinity:
$$
{\textstyle \sum_{n=0}^{\infty }}ar^n=\lim_{n \to \infty}S_n=\lim_{n \to \infty}\frac{a(1-r^n)}{1-r}
$$
If $|r|<1$, then $r^n$ goes to zero as $n$ goes to infinity, so the limit simplifies to
$$
{\textstyle \sum_{n=0}^{\infty }}ar^n = \frac{a}{1-r}
$$
This is the formula for the sum of an infinite geometric series when $|r|<1$.

#### Convergence of the Geometric Series

The convergence of a geometric series depends on the value of the common ratio $r$. We can classify geometric series into three types:

- If $|r|<1$, then the series converges absolutely. This means that the series converges and the sum is finite.
- If $|r|=1$, then the series may converge or diverge. In this case, we need to look at the behavior of the terms in the series to determine convergence or divergence.
- If $|r|>1$, then the series diverges. This means that the sum of the series is infinite.

For example, consider the series
$$
{\textstyle \sum_{n=0}^{\infty }}\frac{1}{2^n}=1+\frac{1}{2} +\frac{1}{4}+\frac{1}{8} + \cdots
$$
<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_3.png" style="zoom:80%;" />

This is a geometric series with $a=1$ and $r=\frac{1}{2}$. Since $|r|<1$, the series converges absolutely, and the sum is
$$
{\textstyle \sum_{n=0}^{\infty }}\frac{1}{2^n}=\frac{1}{1-\frac{1}{2}}=2
$$
<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_4.png" style="zoom:80%;" />

> This image shows us vividly why the sum of this geometric series is 2. Of course, for convenience we let the first term of the series start from n=1. The graph is divided into halves each time and one-half of the remaining parts are taken, that is, one-fourth, and so on, and we find that the total area of the graph is still 1 until the infinite term.

#### Applications of Geometric Series

Geometric series have many applications in mathematics, science, and engineering. For example, they can be used to model exponential growth or decay, such as in the growth of populations or the decay of radioactive substances. They can also be used to evaluate certain types of integrals and to approximate functions.

#### Conclusion

Geometric series are a fundamental concept in calculus and have many applications in various fields. Understanding the convergence and divergence of a geometric series is crucial for using the closed-form solution to find the sum of the series.

### Harmonic Series

The harmonic series is a well-known series in mathematics that arises naturally in many different contexts, including calculus, number theory, and physics. In particular, it is a series of the form:
$$
{\textstyle \sum_{n=1}^{\infty }}\frac{1}{n}=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\cdots
$$
<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_5.png" style="zoom:80%;" />

The harmonic series is interesting because it is a divergent series, meaning that it does not have a finite sum. This can be seen by examining the partial sums of the series, which grow without bound as more and more terms are added.

#### Proof of convergence

To prove that the harmonic series is divergent, we can use the integral test. The integral test states that if the function $f(x)$ is positive, decreasing, and continuous for all $x \geq 1$, and if $a_n = f(n)$ for all $n$, then the series $\sum_{n=1}^\infty a_n$ and the improper integral $\int_1^\infty f(x) dx$ either both converge or both diverge.

In the case of the harmonic series, we can choose $f(x) = \frac{1}{x}$, which satisfies the conditions of the integral test. The improper integral $\int_1^\infty \frac{1}{x} dx$ can be evaluated as:
$$
\int_{1}^{\infty} \frac{1}{x}dx=\lim_{t \to \infty}ln(t)-ln(1)=\infty
$$
Since the integral diverges, the harmonic series must also diverge.

<img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_6.png" style="zoom:80%;" />

It can be seen that the area of each rectangle is $\frac{1}{n}$, so the total area of the first $n$ rectangles is $\sum_{i=1}^n \frac{1}{i}$. As $n$ increases, the area of the rectangles gradually approaches $\ln n$, and thus the step-like graph gradually approaches the curve with slope $y=\ln x$. Eventually, when $n$ tends to infinity, the area of the rectangle tends to $\infty$ and the stepped graph tends to the curve $y=\ln x$.

This visualization can help us better understand the behavior of the series and how it relates to the natural logarithm.

Of course, if you can't read it, it's okay, you just have to remember that the harmonic series is divergent.

#### Applications of Harmonic Series

The divergence of the harmonic series has many important applications in mathematics and science. For example:

- The harmonic series is used in number theory to study the distribution of prime numbers. The divergence of the series implies that there are infinitely many primes, which is a fundamental result in number theory.
- The divergence of the harmonic series also has important implications in physics, particularly in the study of electric fields. The potential energy of a point charge in an electric field is proportional to the sum of the inverses of the distances between the charge and all other charges in the field. This sum is equivalent to the harmonic series, and its divergence implies that the potential energy of a point charge is infinite.

#### Conclusion

In conclusion, the harmonic series is an important and interesting series in mathematics and science. It is a divergent series, meaning that it does not have a finite sum. We can prove the divergence of the series using the integral test, and the divergence has important applications in number theory and physics.

## Some properties of infinite series

1. **If a given infinite series $\sum_{n=1}^\infty u_n$ converges, then any series of the form $\sum_{n=1}^\infty au_n$, where $a$ is a constant, will also converge. This property can be derived using the definition of the limit of a sequence.**

   <img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_8.png" style="zoom:80%;" />

   > We can see that $\sum_{n=1}^\infty (-1)^n/n$ converges and $\sum_{n=1}^\infty 0.5[(-1)^n/n]$ also converges and their convergence is the same as that of $\sum_{n=1}^\infty (-1)^n/n$.
   >
   > Therefore, this theorem can be used to prove that $\sum_{n=1}^\infty 0.5[(-1)^n/n]$ converges because it is obtained by multiplying $\sum_{n=1}^\infty (-1)^n/n$ by a constant 0.5.

   - To prove the linearity property, let $s_n$ be the sequence of partial sums of the series $\sum_{n=1}^\infty u_n$, and let $t_n$ be the sequence of partial sums of the series $\sum_{n=1}^\infty au_n$. Then, we have:
     $$
     \sum_{n=1}^\infty S_n = u_1 + u_2 + u_3 + \cdots + u_n + \cdots
     $$
     and
     $$
     \sum_{n=1}^\infty t_n = au_1 + au_2 + au_3 + \cdots + au_n + \cdots
     $$
     Multiplying the first equation by $a$, we obtain:
     $$
     aS_n = au_1 + au_2 + au_3 + \cdots + au_n + \cdots
     $$
     Now, let $L$ be the limit of the sequence $s_n$, i.e., $\lim_{n\to\infty} s_n = L$. Since the series $\sum_{n=1}^\infty u_n$ converges, we know that the limit $L$ is finite. Therefore, by the algebraic property of limits, we have:
     $$
     \lim_{n \to \infty}aS_n = a \lim_{n \to \infty}S_n = aL
     $$
     Similarly, the limit of the sequence $t_n$ is given by:
     $$
     \lim_{n \to \infty}t_n = \lim_{n \to \infty}(au_1 + au_2 + \cdots + au_n + \cdots) = a(u_1 + u_2 + u_3 + \cdots + u_n + \cdots) = aL
     $$
     Therefore, the series $\sum_{n=1}^\infty au_n$ also converges, and its sum is given by $aL$.

     In conclusion, the linearity property of infinite series states that if a given infinite series converges, then any series obtained by multiplying the terms of the original series by a constant will also converge, and its sum will be the product of the constant and the sum of the original series. This property can be derived using the definition of the limit of a sequence and the algebraic property of limits.

2. **If $\sum_{n=1}^\infty u_n$ and $\sum_{n=1}^\infty v_n$ converge, then $\sum_{n=1}^\infty (u_n \pm v_n)$ also converges.**

   <img src="D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_7.png" style="zoom:80%;" />

   > We can see that both $\sum_{n=1}^\infty (-1)^n/n$ and $\sum_{n=1}^\infty 1/n^2$ converge, while $\sum_{n=1}^\infty [(-1)^n/n \pm 1/n^2]$ also converges, and their convergence is the same as that of $\sum_{n=1}^{\infty} (-1)^n/n$ and $\sum_{n=1}^\infty 1/n^2$ converge in the same way.
   >
   > Therefore, this theorem can be used to prove that $\sum_{n=1}^\infty [(-1)^n/n + 1/n^2]$ converges because it is the sum of $\sum_{n=1}^\infty (-1)^n/n$ and $\sum_{n=1}^\infty 1/n^2$.

   - To prove this result, we can use the following steps:

     1. Let $s_n = u_n + v_n$. Then $\sum_{n=1}^\infty s_n$ is a series formed by adding corresponding terms of $\sum_{n=1}^\infty u_n$ and $\sum_{n=1}^\infty v_n$.
     2. Since both $\sum_{n=1}^\infty u_n$ and $\sum_{n=1}^\infty v_n$ converge, their sequences of partial sums $(S_n)$ and $(T_n)$ converge as well. That is, $\lim_{n\to\infty} S_n = S$ and $\lim_{n\to\infty} T_n = T$.
     3. We want to show that $\sum_{n=1}^\infty s_n = \sum_{n=1}^\infty (u_n + v_n)$ converges. To do so, we need to show that the sequence of partial sums $(U_n)$ of $\sum_{n=1}^\infty s_n$ converges. That is, we need to show that $\lim_{n\to\infty} U_n$ exists.
     4. We can express $U_n$ in terms of $S_n$ and $T_n$ as follows:

     $$
     U_n = S_n + T_n = (\sum_{i=1}^n u_i)+(\sum_{i=1}^n v_i)
     $$

     5. By the properties of limits, we have:

     $$
     \lim_{n \to \infty}U_n = \lim_{n \to \infty}(S_n+T_n)=\lim_{n \to \infty}S_n+\lim_{n \to \infty}T_n=S+T
     $$

     6. Therefore, we have shown that the sequence of partial sums $(U_n)$ of $\sum_{n=1}^\infty s_n$ converges, and hence the series $\sum_{n=1}^\infty s_n$ converges.

     7. Since $s_n$ was defined as $u_n + v_n$, the result holds for both the $+$ and $-$ cases. That is, if $\sum_{n=1}^\infty u_n$ and $\sum_{n=1}^\infty v_n$ converge, then $\sum_{n=1}^\infty (u_n + v_n)$ and $\sum_{n=1}^\infty (u_n - v_n)$ also converge.

3. **Convergent infinite series that still converge after arbitrary addition of parentheses.**

   If you have a Python environment, I strongly suggest you run the python file I provided for "Verifying_Property_3" and you can see the difference in the images after the different brackets.

   - To see why this is true, consider an infinite series $\sum_{n=1}^\infty a_n$ that converges to a limit $L$. That is, the sequence of partial sums $(S_n)$, where $S_n = \sum_{i=1}^n a_i$, converges to $L$ as $n$ approaches infinity.

     Now, suppose we add parentheses to the terms of the series in any way. That is, we group some terms together with parentheses, but the order of the terms is not changed. For example, we might write:
     $$
     a_1 +(a_2+a_3)+(a_4+a_5+a_6)+(a_7+a_8+a_9+a_{10})+\cdots
     $$
     or
     $$
     (a_1 +a_2)+(a_3+a_4+a_5)+(a_6+a_7+a_8+a_9)+\cdots
     $$
     or any other grouping of terms.

     Let's denote the new sequence of partial sums by $(T_n)$, where $T_n$ is the sum of the terms up to the $n$-th group. For example, in the first grouping above, we have $T_1 = a_1$, $T_2 = a_1 + a_2 + a_3$, $T_3 = a_1 + a_2 + a_3 + a_4 + a_5 + a_6$, and so on.

     Now, consider any two adjacent groups of terms in the series. Let's call the terms in the first group $a_{k_1}, a_{k_1+1}, \ldots, a_{k_2-1}$ and the terms in the second group $a_{k_2}, a_{k_2+1}, \ldots, a_{k_3-1}$. Then the sum of these two groups is:
     $$
     (a_{k_1}+a_{k_1+1}+a_{k_1+2}+\cdots+a_{k_2-1})+(a_{k_2}+a_{k_2+1}+a_{k_2+2}+\cdots+a_{k_3-1})
     $$
     By the associative property of addition, we can rearrange this sum as:
     $$
     a_{k_1}+a_{k_1+1}+a_{k_1+2}+\cdots+a_{k_3-1}
     $$
     That is, we can group these terms together in any way we like, and the resulting sum will be the same. Therefore, the sequence of partial sums $(T_n)$ for the new grouping of terms is the same as the original sequence of partial sums $(S_n)$. In other words, adding parentheses to the terms of a convergent series does not change the limit of the series.

     Therefore, we have shown that a convergent infinite series is still convergent after adding any parentheses to the terms of the series.

4. **By removing, adding or changing the finite term, the convergence of the series does not change, but the sum may change.**

   - To formally prove this property, let's consider an infinite series $\sum_{n=1}^\infty a_n$, where $a_n$ is the $n$th term of the series. We want to show that if we modify this series by adding, removing, or changing any finite number of terms, the convergence or divergence of the series will not change.

     First, let's consider the case where we add or remove finitely many terms. Let $S$ be the original sum of the series $\sum_{n=1}^\infty a_n$, and let $S'$ be the new sum of the modified series $\sum_{n=1}^\infty a_n'$. We can express $S'$ as the sum of two series: the first is the original series with a finite number of terms removed or added, and the second is a finite series consisting of the terms that were removed or added. Formally, we can write:
     $$
     {S}' =( {\sum_{n=1}^{k}} a_n + {\sum_{n=k+m+1}^{\infty} a_n})+{\sum_{n=k+1}^{k+m}}a_n
     $$
     where $k$ is a positive integer, $m$ is a non-negative integer, and $a_n'$ is the $n$th term of the modified series.

     Since the original series converges to $S$, we have:
     $$
     \lim_{n \to \infty}({\sum_{i=1}^{n}}a_i)=S
     $$
     Now, let's consider the modified series. The first part of the modified series converges to the same limit as the original series since it differs only by a finite number of terms. The second part is a finite series, and therefore, it converges to a finite sum. Thus, the modified series also converges to a sum $S'$.

     Therefore, we have shown that if we modify an infinite series by adding or removing finitely many terms, the convergence or divergence of the series does not change.

     Next, let's consider the case where we change a finite number of terms. Suppose we modify the series by changing the $k$th term to $a_k'$, where $a_k' \neq a_k$. Let $S$ and $S'$ be the original sum and the modified sum, respectively. Then, we can write:
     $$
     {S}'=S-a_k+a_K'
     $$
     Since the difference between $S'$ and $S$ is a finite number, the convergence or divergence of the series does not change. However, the actual sum of the series is different.

     In conclusion, the property "By removing, adding or changing the finite term, the convergence of the series does not change, but the sum may change" is a fundamental result in the theory of infinite series. It tells us that we can modify an infinite series by adding, removing, or changing a finite number of terms without affecting its convergence or divergence. However, the actual sum of the series may be different.

5. **The necessary condition for the convergence of the series is $\lim_{n \to \infty}u_n=0$. In other words, if $\sum_{n=1}^{\infty}u_n$ is a convergent series, then $\lim_{n\to\infty} u_n = 0$.**

   - To prove this result, suppose that $\sum_{n=1}^{\infty}u_n$ is a convergent series. By definition, this means that the sequence of partial sums $S_k = \sum_{n=1}^{k}u_n$ converges to some finite limit $S$.

     We can express the $k$th term of the series as the difference between two consecutive partial sums:
     $$
     u_k=S_k-S_{k-1}
     $$
     Taking the limit of both sides as $k\rightarrow\infty$, we get:
     $$
     \lim_{k \to \infty}u_k=\lim_{k \to \infty}(S_k-S_{k-1})=S-S=0
     $$
     where we have used the fact that the sequence ${S_k}$ converges to $S$, so $\lim_{k\rightarrow\infty}S_k = S$ and $\lim_{k\rightarrow\infty}S_{k-1} = S$.

     Therefore, we have shown that if $\sum_{n=1}^{\infty}u_n$ is a convergent series, then $\lim_{n\to\infty} u_n = 0$.

     It's worth noting that the converse of this result is not necessarily true. That is, just because $\lim_{n\to\infty}u_n = 0$, it doesn't necessarily mean that $\sum_{n=1}^{\infty}u_n$ is convergent. For example, the harmonic series $\sum_{n=1}^{\infty}\frac{1}{n}$ diverges even though $\lim_{n\to\infty}\frac{1}{n}=0$. So, the condition $\lim_{n\to\infty}u_n = 0$ is only a necessary condition for convergence, not a sufficient one.



Of course we ask that it is not necessary to remember or fully understand the derivation of these properties, these are just to help you understand. For the purpose of the exam, you just need to remember the bolded text, it shouldn't be that hard, right?

# 9.3 Positive Series

This is a very important lesson as we will be starting to learn about the positive series, so please concentrate on that.



## Definition of a Positive Series

A positive series is an infinite series whose terms are all positive real numbers. It has the following form:
$$
\sum_{n=1}^{\infty}a_n = a_1+a_2+a_3+\cdots
$$
where $a_n$ is the $n$th term of the series.

### p-Series

A **p-series** is a series of the form $\sum_{n=1}^{\infty} \frac{1}{n^p}$, where $p$ is a positive real number. The series is named after the exponent $p$ in the denominator.

The p-series has the following properties:

- If $p>1$, then the p-series converges.
- If $p\leq 1$, then the p-series diverges.

![](D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_9.png)

The proof of this result is based on the integral test. To see why this is true, we can consider the function $f(x) = \frac{1}{x^p}$. This function is continuous, positive, and decreasing on the interval $[1,\infty)$, so we can apply the integral test to the series to obtain:
$$
\sum_{n=1}^{\infty} \frac{1}{n^p} \quad \text{if and only if}\quad \int_{1}^{\infty} \frac{1}{x^p}dx < \infty
$$
Evaluating the integral, we get:
$$
\int_{1}^{\infty} \frac{1}{x^p}dx 
  \left\{\begin{matrix} 
  \frac{1}{1-p} \quad \text{if}\quad p> 1\\
\infty \quad \text{if}\quad p\le 1
\end{matrix}\right.
$$
Thus, the p-series converges if and only if $p>1$, and diverges if $p\leq 1$.

The sum of the p-series for $p>1$ can be expressed in terms of the Riemann zeta function $\zeta(p)$, which is defined by:
$$
\zeta(p)=\sum_{n=1}^{\infty}\frac{1}{n^p}
$$
The Riemann zeta function has many interesting properties and connections to other areas of mathematics, including number theory and complex analysis.

## Convergence tests

There are several convergence tests that can be used to determine whether a positive series converges or diverges. Here are a few of the most commonly used tests:

### 1. Comparison Test

The **comparison test** is a method used to determine the convergence or divergence of a series by comparing it to another series whose convergence behavior is known. The comparison test states:

Suppose that $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ are series with positive terms, and suppose that $a_n \leq b_n$ for all $n$.

- If $\sum_{n=1}^{\infty} b_n$ converges, then $\sum_{n=1}^{\infty} a_n$ converges as well.
- If $\sum_{n=1}^{\infty} a_n$ diverges, then $\sum_{n=1}^{\infty} b_n$ diverges as well.

In other words, if the terms of the series $\sum_{n=1}^{\infty} a_n$ are always less than or equal to the terms of the series $\sum_{n=1}^{\infty} b_n$, and if $\sum_{n=1}^{\infty} b_n$ converges, then $\sum_{n=1}^{\infty} a_n$ must converge as well. Conversely, if $\sum_{n=1}^{\infty} a_n$ diverges, then $\sum_{n=1}^{\infty} b_n$ must also diverge.

The comparison test is often used to compare a given series to a p-series, since the convergence behavior of p-series is well-known. Specifically, if we have a series of the form $\sum_{n=1}^{\infty} \frac{1}{n^p}$ and another series $\sum_{n=1}^{\infty} a_n$ whose terms are always less than or equal to $\frac{1}{n^p}$, then we can use the comparison test to determine the convergence behavior of $\sum_{n=1}^{\infty} a_n$.

![](D:\Information\Book\Math\Notes\Chapter 9 Infinite Series\Figure\Figure_10.png)

> The common infinite series that we use for reference are:
>
> 1) Geometric Series
> 2) Harmonic Serie
> 3) p-Series

### 2. Limit Comparison Test

The **limit comparison test** is another method used to determine the convergence or divergence of a series. Like the comparison test, it involves comparing the given series to another series whose convergence behavior is known. However, the limit comparison test allows for more flexibility in choosing the series to compare with.

Suppose that $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ are series with positive terms. Let $L = \lim_{n \to \infty} \frac{a_n}{b_n}$, where $L$ is a positive finite number or $\infty$.

- If $0 < L < \infty$, then $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ either both converge or both diverge.
- If $L = 0$ and $\sum_{n=1}^{\infty} b_n$ converges, then $\sum_{n=1}^{\infty} a_n$ converges as well.
- If $L = \infty$ and $\sum_{n=1}^{\infty} b_n$ diverges, then $\sum_{n=1}^{\infty} a_n$ diverges as well.

The limit comparison test allows for more flexibility in choosing the series to compare with, since we only need the ratio of the terms to converge to a finite positive number. This means that we can often find a more manageable series to compare with than in the case of the comparison test.

### 3. Ratio Test

The **ratio test** is a test for the convergence or divergence of a series. The ratio test states:

Suppose that $\sum_{n=1}^{\infty} a_n$ is a series with positive terms, and let $L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$ (the limit may or may not exist).

- If $L < 1$, then $\sum_{n=1}^{\infty} a_n$ converges absolutely.
- If $L > 1$ or $L = \infty$, then $\sum_{n=1}^{\infty} a_n$ diverges.
- If $L = 1$ or the limit does not exist, then the ratio test is inconclusive and we need to use another test to determine convergence or divergence.

Intuitively, the ratio test compares the terms of the series to the terms of a geometric series with common ratio $L$. If $L < 1$, then the terms of the series decay faster than the terms of a convergent geometric series, so the series converges. If $L > 1$, then the terms of the series grow faster than the terms of a divergent geometric series, so the series diverges. If $L = 1$, then the terms of the series decay at the same rate as the terms of a convergent geometric series, so the test is inconclusive.

### 4. Root Test

The **root test** is a test for the convergence or divergence of a series. The root test states:

Suppose that $\sum_{n=1}^{\infty} a_n$ is a series with positive terms, and let $L = \lim_{n \to \infty} \sqrt[n]{a_n}$ (the limit may or may not exist).

- If $L < 1$, then $\sum_{n=1}^{\infty} a_n$ converges absolutely.
- If $L > 1$ or $L = \infty$, then $\sum_{n=1}^{\infty} a_n$ diverges.
- If $L = 1$ or the limit does not exist, then the root test is inconclusive and we need to use another test to determine convergence or divergence.

Intuitively, the root test compares the terms of the series to the terms of a convergent geometric series with common ratio $L$. If $L < 1$, then the terms of the series decay faster than the terms of a convergent geometric series, so the series converges. If $L > 1$, then the terms of the series grow faster than the terms of a divergent geometric series, so the series diverges. If $L = 1$, then the terms of the series decay at the same rate as the terms of a convergent geometric series, so the test is inconclusive.



This one is very important, as many of the concepts and extensions we mention subsequently are based on the conclusions of this chapter, so make sure you read it carefully.

# 9.4 Arbitrary Series

## Alternating series

An alternating series is a type of infinite series where the terms alternate in sign, meaning that each term is positive or negative. Mathematically, an alternating series can be represented as:
$$
\sum_{n=1}^{\infty}(-1)^{n+1}a_n
$$
where $a_n$ is a sequence of positive numbers. The first term of the series is $(-1)^2a_1=a_1$, which is positive. The second term is $(-1)^3a_2=-a_2$, which is negative. The third term is $(-1)^4a_3=a_3$, which is positive, and so on.

The key property of alternating series is that they converge if the sequence $a_n$ is decreasing and the limit of $a_n$ as $n$ approaches infinity is 0, that is, $\lim_{n\to\infty} a_n = 0$. This property is known as the Alternating Series Test.

The Alternating Series Test states that if a series $\sum_{n=1}^{\infty} (-1)^{n+1}a_n$ satisfies the conditions:

1. $a_n \geq 0$ for all $n$,
2. $a_{n+1} \leq a_n$ for all $n$, and
3. $\lim_{n\to\infty} a_n = 0$,

then the series converges.

In addition to the Alternating Series Test, there are some other important results related to alternating series. For example, the error of an alternating series approximation can be bounded by the size of the first neglected term. This result is known as the Alternating Series Estimation Theorem.

The Alternating Series Estimation Theorem states that if a series $\sum_{n=1}^{\infty} (-1)^{n+1}a_n$ satisfies the conditions of the Alternating Series Test, and $S$ is the sum of the series, then the error $R_n = S - \sum_{k=1}^{n} (-1)^{k+1}a_k$ in approximating $S$ by the first $n$ terms of the series is bounded by the size of the first neglected term, that is, $|R_n| \leq a_{n+1}$.

Another important result related to alternating series is the Leibniz criterion, which provides a sufficient condition for convergence of an alternating series. The Leibniz criterion states that if a series $\sum_{n=1}^{\infty} (-1)^{n+1}a_n$ satisfies the conditions:

1. $a_n \geq 0$ for all $n$,
2. $a_{n+1} \leq a_n$ for all $n$, and
3. $\lim_{n\to\infty} a_n = 0$,

then the series converges.



## Absolute Series

An absolute series is a type of infinite series where the terms are all positive, meaning that each term is greater than or equal to zero. Mathematically, an absolute series can be represented as:
$$
\sum_{n=1}^{\infty} |a_n|
$$
where $a_n$ is a sequence of real numbers. The absolute value of each term $|a_n|$ ensures that the terms are all positive, regardless of the sign of $a_n$.

The behavior of absolute series is important in the study of infinite series because if an absolute series converges, then the original series, which may or may not alternate in sign, also converges. This is known as the Absolute Convergence Test.

The Absolute Convergence Test states that if a series $\sum_{n=1}^{\infty} |a_n|$ converges, then the series $\sum_{n=1}^{\infty} a_n$ also converges. The converse, however, is not necessarily true: if the series $\sum_{n=1}^{\infty} a_n$ converges but the series $\sum_{n=1}^{\infty} |a_n|$ diverges, then the series $\sum_{n=1}^{\infty} a_n$ is said to converge conditionally.

### Theorem A

If the series $\sum_{n=1}^{\infty} |a_n|$ converges, then the series $\sum_{n=1}^{\infty} a_n$ also converges. Conversely, if the series $\sum_{n=1}^{\infty} a_n$ diverges, then the series $\sum_{n=1}^{\infty} |a_n|$ also diverges.

**Explanation:**

The theorem states that if the series of absolute values $\sum_{n=1}^{\infty} |a_n|$ converges, then the original series $\sum_{n=1}^{\infty} a_n$ also converges. Conversely, if the original series $\sum_{n=1}^{\infty} a_n$ diverges, then the series of absolute values $\sum_{n=1}^{\infty} |a_n|$ also diverges.

Let's understand why this theorem holds.

**Proof (Forward Direction):**

Suppose $\sum_{n=1}^{\infty} |a_n|$ converges. This means that the series of positive terms $\sum_{n=1}^{\infty} a_n'$, where $a_n' = |a_n|$, converges.

Since $a_n' \geq 0$ for all $n$, the convergence of $\sum_{n=1}^{\infty} a_n'$ implies that the series $\sum_{n=1}^{\infty} a_n$ also converges. The reason is that the terms of $\sum_{n=1}^{\infty} a_n'$ and $\sum_{n=1}^{\infty} a_n$ have the same magnitudes but potentially opposite signs.

Therefore, if the series of absolute values converges, the original series must also converge.

**Proof (Converse Direction):**

Now, let's prove the converse part of the theorem.

Suppose $\sum_{n=1}^{\infty} a_n$ diverges. This means that the series does not have a finite sum. Since the terms $a_n$ can have both positive and negative values, their absolute values $|a_n|$ can be considered as a series with nonnegative terms.

If $\sum_{n=1}^{\infty} |a_n|$ were to converge, it would mean that the series of nonnegative terms has a finite sum. However, since the original series $\sum_{n=1}^{\infty} a_n$ diverges, the series of absolute values $\sum_{n=1}^{\infty} |a_n|$ must also diverge.

Hence, if the original series diverges, the series of absolute values must also diverge.

Therefore, the theorem holds in both directions.

This theorem is useful in analyzing the convergence behavior of series. If we can show that the series of absolute values converges, we can conclude that the original series converges as well. On the other hand, if the original series diverges, we can conclude that the series of absolute values also diverges.

### Knowledge Point

If the series $\sum_{n=1}^{\infty} |u_n|$ converges, then the series $\sum_{n=1}^{\infty} u_n$ is said to be **absolutely convergent**. Conversely, if the series $\sum_{n=1}^{\infty} |u_n|$ diverges but the series $\sum_{n=1}^{\infty} u_n$ converges, then it is referred to as **conditionally convergent**.

**Explanation:**

1. **Convergence of Absolute Series**: If the series of absolute values $\sum_{n=1}^{\infty} |u_n|$ converges, it means that the series formed by the magnitudes of the terms converges. In other words, the series $\sum_{n=1}^{\infty} u_n'$, where $u_n' = |u_n|$, is convergent. As a result, the original series $\sum_{n=1}^{\infty} u_n$ is said to be absolutely convergent. The absolute convergence of a series guarantees that the series converges regardless of the signs of its terms.
2. **Conditional Convergence**: On the other hand, if the series of absolute values $\sum_{n=1}^{\infty} |u_n|$ diverges, but the series $\sum_{n=1}^{\infty} u_n$ converges, then the original series is known as conditionally convergent. This means that the convergence of the series is dependent on the alternating signs of its terms. The series may converge as a result of the cancellation between positive and negative terms.

These concepts can be better understood by considering some examples. For instance:

- The series $\sum_{n=1}^{\infty} (-1)^{n+1}/n$ is an example of a conditionally convergent series. The series of absolute values $\sum_{n=1}^{\infty} 1/n$ is known as the harmonic series, which diverges. However, the original series $\sum_{n=1}^{\infty} (-1)^{n+1}/n$ converges to the natural logarithm of 2.
- Conversely, the series $\sum_{n=1}^{\infty} (-1)^{n+1}/n^2$ is an example of an absolutely convergent series. Both the series of absolute values $\sum_{n=1}^{\infty} 1/n^2$ and the original series $\sum_{n=1}^{\infty} (-1)^{n+1}/n^2$ converge.

Understanding the distinction between absolute convergence and conditional convergence is crucial when studying the convergence behavior of series and their applications in various mathematical contexts.

**Remember:**

- If the series of absolute values converges, the original series is absolutely convergent.
- If the series of absolute values diverges but the original series converges, the original series is conditionally convergent.

These concepts play a significant role in series analysis and have implications in various branches of mathematics and beyond.

## Theorem B

For an infinite series $\sum_{n=1}^{\infty} u_n$, if the limit $\lim_{n\to\infty} \left|\frac{u_{n+1}}{u_n}\right| = L$, where $L$ is a nonnegative real number, then:

- If $L < 1$, the series $\sum_{n=1}^{\infty} u_n$ is absolutely convergent.
- If $L > 1$ or $L = \infty$, the series $\sum_{n=1}^{\infty} u_n$ is divergent.
- If $L = 1$, the test is inconclusive, and the series may be convergent or divergent.

**Explanation:**

The theorem, known as the Ratio Test, provides information about the convergence or divergence of an infinite series based on the limit of the ratio of consecutive terms $\left|\frac{u_{n+1}}{u_n}\right|$.

Let's examine the different cases described by the theorem:

1. **$L < 1$: Absolute Convergence** If the limit of the ratio is less than 1 ($L < 1$), it implies that the terms of the series eventually become smaller in magnitude as $n$ increases. In this case, the series $\sum_{n=1}^{\infty} u_n$ is said to be absolutely convergent. The convergence is guaranteed regardless of the signs of the terms. Moreover, the smaller the value of $L$, the faster the series converges.
2. **$L > 1$ or $L = \infty$: Divergence** If the limit of the ratio is greater than 1 ($L > 1$) or infinite ($L = \infty$), it indicates that the terms of the series eventually increase in magnitude as $n$ increases. Consequently, the series $\sum_{n=1}^{\infty} u_n$ is divergent. The divergence can be understood as the series growing without bounds, rendering its sum undefined.
3. **$L = 1$: Inconclusive** If the limit of the ratio is exactly 1 ($L = 1$), the test does not provide a definitive conclusion about the convergence or divergence of the series. The behavior of the series could be either convergent or divergent, and further analysis or alternative tests are necessary to determine its convergence.

## Theorem C

**Rearrangement Theorem**

The Rearrangement Theorem is a result in the theory of infinite series that states: If an infinite series $\sum_{n=1}^{\infty} a_n$ is conditionally convergent, meaning it converges but not absolutely, then for any real number $S$, it is possible to rearrange the terms of the series such that the new rearranged series converges to $S$.

**Explanation:**

The Rearrangement Theorem deals with the behavior of conditionally convergent series, which are series that converge but not absolutely. It asserts that by rearranging the terms of a conditionally convergent series, we can achieve a new series that converges to any desired real number $S$.

To understand the theorem, let's consider an example of a conditionally convergent series:
$$
\sum_{n=1}^{\infty}(-1)^{n+1}\frac{1}{n}=1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\cdots
$$
This series, known as the alternating harmonic series, is conditionally convergent. If we sum the terms in their original order, the series converges to the natural logarithm of 2. However, the Rearrangement Theorem allows us to rearrange the terms of this series in any manner we choose, creating a new series that converges to any desired real number.

For instance, if we rearrange the terms by first taking two positive terms followed by one negative term, we get:
$$
(1-\frac{1}{2})+(\frac{1}{3}-\frac{1}{4})+(\frac{1}{5}-\frac{1}{6})+\cdots
$$
This rearranged series converges to a different value, specifically, $\ln(2)/2$. By employing various rearrangement patterns, we can obtain different convergent sums.

It is important to note that the Rearrangement Theorem applies to conditionally convergent series but not absolutely convergent series. For absolutely convergent series, the order of the terms does not affect the sum.

The Rearrangement Theorem showcases the intriguing behavior of conditionally convergent series. It reveals that rearranging the terms can lead to different convergence behavior and different sums. This result demonstrates the delicate nature of conditionally convergent series and highlights the importance of considering the order in which the terms are summed.

# 9.5 Power Series

Power series are a fundamental topic in calculus and mathematical analysis. They provide a way to represent functions as infinite series of powers of a variable. Let's dive into the concepts and properties of power series.

## Definition of Power Series

A power series is an infinite series of the form:
$$
\sum_{n=0}^{\infty}a_n(x-c)^n
$$
where $a_n$ and $c$ are constants, and $x$ is a variable. The constants $a_n$ are called the coefficients of the power series.

## Convergence of Power Series

The convergence of a power series depends on the value of $x$ and the coefficients $a_n$. We define the interval of convergence, which is the set of all values of $x$ for which the series converges.

To determine the interval of convergence, we use the **ratio test** or the **root test**. These tests help determine whether the series converges absolutely, diverges, or converges conditionally.

### Ratio Test

The ratio test states that if
$$
\lim_{n \to \infty}|\frac{a_{n+1}}{a_n}|=L
$$
where $L$is a finite number, then the series converges absolutely if $L<1$ and diverges if $L>1$.

We still use the ratio test more often, so I will derive the ratio test in detail.

Suppose we have a power series of the form:
$$
\sum_{n=0}^{\infty}a_n(x-c)^n
$$
We want to determine the convergence or divergence of this series using the ratio test. The ratio test involves taking the limit of the absolute value of the ratio of consecutive terms:
$$
L=\lim_{n \to \infty}|\frac{a_{n+1}}{a_n}|
$$
Now, we'll consider the following cases:

1. If $L<1$: The series converges absolutely.
2. If $L>1$: The series diverges.
3. If $L=1$: The test is inconclusive.

Let's derive the ratio test to determine the value of $L$:

First, consider the term $\frac{a_{n+1}}{a_n}$:
$$
\frac{a_{n+1}}{a_n}=\frac{a_n(x-c)^{n+1}}{a_n(x-c)^n}=(x-c)
$$
Now, take the absolute value of this term:
$$
|\frac{a_{n+1}}{a_n}|=|x-c|
$$
Since $a_n$ and $a_{n+1}$ are coefficients of the power series, they are constant with respect to $n$, so they cancel out.

Now, we have:
$$
L=\lim_{n \to \infty}|x-c|
$$
Let's analyze this limit:

- If $|x-c|<1$, then $\lim_{n \to \infty}|x-c|=|x-c|$.
- If $|x-c|>1$, then $\lim_{n \to \infty}|x-c|=|x-c|$.
- If $|x-c|=1$, the limit does not exist since the terms alternate in sign.

Therefore, we have:
$$
L=\left\{\begin{matrix} 
  |x-c| \quad \text{if} \quad |x-c|<1\\
  |x-c| \quad \text{if} \quad |x-c|>1\\
  \text{undefined} \quad \text{if} \quad |x-c|=1\\
\end{matrix}\right.
$$

From this, we can conclude:



### Root Test

The root test states that if
$$
\lim_{n \to \infty}|a_n|^{\frac{1}{n}}=L
$$
where $L$ is a finite number, then the series converges absolutely if $L<1$ and diverges if $L>1$.

## Interval of Convergence

Once you apply either the ratio test or the root test and find the value of $L$, you can determine the interval of convergence. The interval will have one of the following forms:

1. The series converges only at $x=c$.
2. The series converges for all $x$.
3. The series converges for $c-R<x<c+R$, where $R$ is a positive number called the radius of convergence.

## Radius of Convergence

The radius of convergence, denoted by $R$, determines how far from the center $c$ the power series converges. It can be found using the following formulas:

### Ratio Test Formula

If the ratio test is used to find the value of $L$ for the series, then the radius of convergence is given by:
$$
R=\frac{1}{L}
$$
Consider the power series:

$$
a_0 + a_1x + a_2x^2+\cdots 
$$
The theorem states the following:

1. If $\lim_{{n \to \infty}} \left| \frac{{a_{n+1}}}{{a_n}} \right| = L$ where $0 < L < \infty$, then the series has a convergence radius \(R\) given by $R = \frac{1}{L}$. In other words, the series converges absolutely for all \(x\) values within the interval $-R < x < R$.

2. If $L = 0$, then the series has an infinite convergence radius, $R = \infty$. This means that the series converges absolutely for all $x$ values.

3. If $L = \infty$, then the series has a convergence radius of $R = 0$. In this case, the series only converges at $x = c$, where $c$ is the center of the power series.

To summarize:

- When $0 < L < \infty$, the series converges absolutely within the interval $-R < x < R$ where $R = \frac{1}{L}$.
- When $L = 0$, the series converges absolutely for all $x$ values.
- When $L = \infty$, the series only converges at $x = c$ (the center of the power series), and the convergence radius is $R = 0$.

## Properties of Power Series

Power series possess several important properties that make them useful for approximating functions.

### Sum of a Power Series

The sum of a power series is denoted by $S(x)$ and is defined as:
$$
S(x)=\sum_{n=0}^{\infty}a_n(x-c)^n
$$
where $S(x)$ represents the function represented by the power series.

### Differentiation and Integration

Within the interval of convergence, a power series can be differentiated and integrated term by term. This means that if $S(x)$ represents a function $f(x)$, then its derivative $f'(x)$ and integral $∫ f(x)$ can be found by differentiating and integrating each term of the power series.

And after integrating and differentiating term by term, the radius of convergence is the same. However, it should be noted that whether the endpoints converge or not needs to be re-determined.

### Uniqueness

A power series represents a unique function within its interval of convergence. That is, if two power series have the same coefficients and the same center, they represent the same function.

### Operations on Power Series

We can perform arithmetic operations on power series, such as addition, subtraction, multiplication, and division, within their respective intervals of convergence. These operations are carried out by manipulating the coefficients of the power series.

# 9.6 Taylor Series

The Taylor Series is a mathematical tool that allows us to represent a wide range of functions as an infinite series of terms. It provides a way to approximate complex functions using simpler polynomial expressions. The series is named after the English mathematician Brook Taylor, who introduced the concept in the 18th century.

## Taylor Polynomial

At the heart of the Taylor Series lies the Taylor polynomial, which approximates a function around a specific point (often denoted as *c*) by using a polynomial of increasing degree. The Taylor polynomial of degree *n* for a function *f(x)* is given by the formula:
$$
P_n(x) = f(c) + f'(c)(x-c) + \frac{f''(c)(x-c)^2}{2!} + \frac{f'''(c)(x-c)^3}{3!} + \ldots + \frac{f^n(c)(x-c)^n}{n!}
$$
In this formula, *f'(x)* represents the first derivative of *f(x)*, *f''(x)* represents the second derivative, and so on, with $f^{(n)}(x)$ representing the *n*-th derivative of *f(x)*.

## Taylor Series Expansion

The Taylor Series expands the Taylor polynomial to an infinite series. It provides a way to represent a function *f(x)* as the sum of an infinite number of terms. The general form of the Taylor Series expansion for a function *f(x)* centered around a point *c* is:
$$
f(x) = f(c) + f'(c)(x-c) + \frac{f''(c)(x-c)^2}{2!} + \frac{f'''(c)(x-c)^3}{3!} + \ldots
$$
This series continues indefinitely, with each subsequent term involving higher derivatives of the function evaluated at the center *c*.

## Taylor Series: Sufficient and Necessary Conditions

The Taylor series has both sufficient and necessary conditions for its validity. Let's discuss them in detail:

### Sufficient Condition: Infinitely Differentiable Function

The **sufficient condition** for the Taylor series expansion is that the function must be **infinitely differentiable** within a specific interval. In other words, all the derivatives of the function exist and are continuous in that interval.

If a function satisfies this condition, we can construct its Taylor series expansion by evaluating the derivatives of the function at a chosen center.

### Necessary Condition: Convergence of Remainder Term

The **necessary condition** for the Taylor series expansion is that the **remainder term must converge to zero**. This means that as we include more terms in the Taylor series, the difference between the original function and the truncated series becomes arbitrarily small.

Mathematically, the necessary condition can be stated as:
$$
\lim_{{n \to \infty}} R_n(x) = 0
$$
where *R_n(x)* represents the remainder term of the Taylor series truncated at the *n*-th term.

The convergence of the remainder term ensures that the Taylor series provides a valid approximation of the original function within the specified interval.

## Properties of Taylor Series

Here are some important properties of Taylor Series:

1. **Convergence**: The Taylor Series expansion converges to the original function *f(x)* within a certain interval around the center *c*. The size of this interval depends on the behavior of *f(x)* and the point of expansion.
2. **Approximation**: By truncating the Taylor Series at a specific term, we can obtain an approximation of the function *f(x)*. The accuracy of the approximation increases as we include more terms in the series.
3. **Remainder Term**: The remainder term represents the difference between the original function *f(x)* and the truncated Taylor Series approximation. It provides a measure of the error in the approximation and can be expressed using the Lagrange form of the remainder, Cauchy form of the remainder, or other forms depending on the situation.
4. **Uniform Convergence**: In some cases, the Taylor Series expansion may converge uniformly, meaning that the approximation is accurate across the entire interval of interest, rather than just at a specific point.
5. **Center Selection**: The choice of the center *c* affects the behavior and accuracy of the Taylor Series. Selecting a suitable center can simplify calculations and improve the approximation in specific regions.

### Example

Let's take an example to illustrate the concept. Consider the function *f(x) = sin(x)*. We can find the Taylor Series expansion for *f(x)* centered at *c = 0*.

The derivatives of *f(x) = sin(x)* are:

- *f'(x) = cos(x)*
- *f''(x) = -sin(x)*
- *f'''(x) = -cos(x)*
- *f''''(x) = sin(x)*

Evaluating these derivatives at *x = 0* gives us:

- *f(0) = 0*
- *f'(0) = 1*
- *f''(0) = 0*
- *f'''(0) = -1*
- *f''''(0) = 0*

Substituting these values into the Taylor polynomial formula, we have:
$$
P_n(x) = 0 + 1(x-0) + \frac{0(x-0)^2}{2!} + \frac{-1(x-0)^3}{3!} + \ldots
$$
Simplifying the terms, we get:
$$
P_n(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots
$$
This is the Taylor Series expansion of *f(x) = sin(x)* centered at *c = 0*.

## Important Taylor expansions

1. **Exponential Function Expansion**:

The Taylor expansion for the exponential function is:
$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$
This expansion is particularly useful in various mathematical and scientific contexts, especially when dealing with exponential growth or decay phenomena.

2. **Trigonometric Function Expansion**:

The Taylor expansions for common trigonometric functions are:

- Sine function:
  $$
  \sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}
  $$

- Cosine function:
  $$
  \cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}
  $$

- Arctangent Expansion:
  $$
  \arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1}
  $$

- Tangent Expansion:
  $$
  \tan(x) = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \ldots = \sum_{n=1}^{\infty} \frac{B_{2n} (-4)^n (1-4^n) x^{2n-1}}{(2n)!}
  $$

3. **Natural Logarithm Expansion**:

The Taylor expansion for the natural logarithm function is:
$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \ldots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}
$$
This expansion is particularly useful in approximating the logarithm of values close to 1.

4. **Geometric Series**:

The Taylor expansion for the geometric series is:
$$
\frac{1}{1-x} = 1 + x + x^2 + x^3 + \ldots = \sum_{n=0}^{\infty} x^n, \quad |x| < 1
$$
This expansion is widely used in mathematics and physics, especially in the study of sequences and series.

5. **Binomial Expansion**:

The binomial expansion, based on the binomial theorem, is used to expand expressions of the form $(a + b)^n$:
$$
(a + b)^n = \binom{n}{0} a^n b^0 + \binom{n}{1} a^{n-1} b^1 + \binom{n}{2} a^{n-2} b^2 + \ldots + \binom{n}{n-1} a^1 b^{n-1} + \binom{n}{n} a^0 b^n
$$
This expansion is applicable in combinatorics, probability theory, and algebraic manipulations.

6. **Error Function Expansion**:

The Taylor expansion for the error function is:
$$
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \left(x - \frac{x^3}{3} + \frac{x^5}{10} - \frac{x^7}{42} + \ldots\right) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{n!(2n+1)}
$$
The error function is widely used in statistics and mathematical analysis, particularly in the study of normal distributions and probability.



The last two are not required, understanding is sufficient

# 9.7 Application of Taylor's Formula

Many of you may be wondering about the purpose of learning Taylor expansions, as they can be difficult to understand. However, this chapter aims to demonstrate the incredible power of the Taylor formula.

What methods can we employ to find the limits of a function? The limit operator (quadratic + composite)? Substitution? Equivalent infinitesimal? No, no, and no! In fact, once you grasp Taylor's formula, there's no need to learn any of these methods. You won't need to use them anymore! Using them could lead to mistakes, and if you make a mistake, you won't know where it went wrong!

## Introduction of Taylor's formula

### Limits of Polynomials

When it comes to finding limits, dealing with functions like $e^x$, $\sin(x)$, or $\ln(1+x)$ can often be challenging. They can seem quite perplexing. However, there's one type of function that is very friendly when it comes to limits, and that is the polynomial!

The general formula for a polynomial is:
$$
a_nx^n+a_{n-1}x^{n-1}+\cdots+a_2x^2+a_1x+a_0=\sum_{i=0}^{n}a_ix^i
$$
where $a_i$ are constants, and $a_n \neq 0$.

Adding and subtracting polynomials is straightforward; you just need to add and subtract the coefficients of the corresponding terms. Multiplying and dividing polynomials is a bit more involved, but when it comes to finding the limit as $x \to \infty$, there is an easily understandable conclusion:

Consider the limit when two polynomials are divided:
$$
L=\lim_{x \to 0} \frac{a_mx^m+a_{m+1}x^{m+1}+\cdots}{b_nx^n+b_{n+1}x^{n+1}+\cdots} , \quad (a_mb_n \neq 0)
$$
The outcome of this limit depends on the relationship between the exponents $m$ and $n$:

- If $m > n$, which means the numerator is a higher-order infinitesimal and tends to 0 faster than the denominator, the result is $L = 0$.
- If $m < n$, which means the numerator is a lower-order infinitesimal and the denominator tends to 0 faster than the numerator, the result is $L=\infty$.
- If $m=n$, which means the numerator and denominator are of the same order of infinitesimals, you can obtain:

$$
L=\lim_{x \to \infty} \frac{(a_mx^m+a_{m+1}x^{m+1}+\cdots)/x^m}{(b_mx^n+b_{m+1}x^{m+1}+\cdots)/x^m}=\lim_{x \to 0} \frac{a_mx^m+a_{m+1}x+\cdots}{b_mx^n+b_{m+1}x+\cdots}=\frac{a_m}{b_m}
$$

When finding the limit as $x \to 0$, polynomial factoring can be achieved by keeping only the term with the lowest order. (Note that this must be the factorization of the entire function, as explained in the example at the end of the text in the Appendix.)

Furthermore, note that when finding the limit as $x \to \infty$, it is generally advisable to perform an inverse substitution, i.e., replace all occurrences of $x$ with $\frac{1}{x}$.

From these observations, we can conclude that the limits of polynomial expressions in quadratic form with respect to $x$ are easy to determine as $x \to 0$.

### Polynomial Expressions for General Functions

Having established the simplicity of finding the limit of a polynomial, a natural question arises: can we approximate a general function using a polynomial? After all, a polynomial can have an arbitrary number of terms, each with its own coefficients. These coefficients act as adjustable controls for the function, allowing us to manipulate them in an attempt to make the polynomial closely approximate the general function.

Let's denote the general function as $f(x)$ and assume that it can be approximated by a polynomial:
$$
f(x)=a_0+a_1x+a_2x^2+a_3x^3+\cdots+a_nx^n+\cdots \quad (1)
$$
The question now is how to determine the coefficients of this polynomial.

It's easy to observe that $a_0 = f(0)$, but finding the subsequent coefficients doesn't seem as straightforward. We would like the equation above to hold for all values of $x$, which allows us to differentiate both sides of the equation with respect to $x$ simultaneously. Doing so, we find:
$$
f'(x)=a_1+2a_2x+3a_3x^2+\cdots+na_nx^{n-1}+\cdots
$$
From this, we can easily deduce that $a_1 = f'(0)$. Similarly, we can determine the remaining coefficients in a similar manner.

By equating the equation $(1)$ and taking the $n$th derivative of $x$ on both sides, we obtain:
$$
f^{(n)}(x)=n!a_n+\cdots
$$
Setting $x = 0$ yields:
$$
a_n=\frac{f^{(n)}(0)}{n!}
$$
Hence, we can now determine all the coefficients $a_1, a_2, \ldots, a_n$ (assuming that $f(x)$ has derivatives of order $n$). Consequently, we can express $f(x)$ as:
$$
f(x)=\sum_{i=0}^{n}a_ix^i + R(x), \quad a_i=\frac{f^{(n)}(0)}{i!}
$$
Here, $R(x)$ represents the remainder term or the error of the function $f(x)$ with respect to this polynomial approximation. Currently, we do not know the exact form of this remainder term.

### Taylor's Theorem

Although we haven't determined the exact form of the remainder term, Taylor's theorem provides us with reassurance (and I won't attempt to prove it here). Let's recall the **Maclaurin's formula** for **Peano's remainder term**:

If $f(x)$ has derivatives of order $n$ at $x = 0$, then in the vicinity of $x = 0$, we have:

$f(x) = \sum_{i=0}^{n} a_ix^i + o(x^n)$, where $a_i = \frac{f^{(n)}(0)}{i!}$.

Here, $o(x^n)$ denotes a higher order infinitesimal compared to $x^n$, which means that $\lim_{x\to 0} \frac{o(x^n)}{x^n} = 0$.

Taylor's formula involves substituting $x$ in Maclaurin's formula with $x - x_0$, which represents a translation of $x$. I don't strictly differentiate between Taylor's formula and Maclaurin's formula. For now, we won't delve into the Lagrange remainder term.

The beauty lies in the fact that elementary functions, along with some power functions and variable limit integrals, constitute a significant portion of our common limit problems. Since these functions possess infinitely differentiable properties, we can comfortably apply Taylor's formula to them.

## Commonly Used Taylor Formulas

Here are some commonly used Taylor formulas, as mentioned in the previous chapter:

1. **Exponential Function Expansion**:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

2. **Trigonometric Function Expansion**:

- Sine function:
  $$
  \sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}
  $$

- Cosine function:
  $$
  \cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}
  $$

- Arctangent Expansion:
  $$
  \arctan(x) = x - \frac{x^3}{3} + \frac{x^5}{5} - \frac{x^7}{7} + \ldots = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1}
  $$

- Tangent Expansion:
  $$
  \tan(x) = x + \frac{x^3}{3} + \frac{2x^5}{15} + \frac{17x^7}{315} + \ldots = \sum_{n=1}^{\infty} \frac{B_{2n} (-4)^n (1-4^n) x^{2n-1}}{(2n)!}
  $$

3. **Natural Logarithm Expansion**:

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \ldots = \sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}
$$

4. **Geometric Series**:

$$
\frac{1}{1-x} = 1 + x + x^2 + x^3 + \ldots = \sum_{n=0}^{\infty} x^n, \quad |x| < 1
$$

5. **Binomial Expansion**:

The binomial expansion, based on the binomial theorem, is used to expand expressions of the form $(a + b)^n$:
$$
(a + b)^n = \binom{n}{0} a^n b^0 + \binom{n}{1} a^{n-1} b^1 + \binom{n}{2} a^{n-2} b^2 + \ldots + \binom{n}{n-1} a^1 b^{n-1} + \binom{n}{n} a^0 b^n
$$

6. **Error Function Expansion**:

$$
\mathrm{erf}(x) = \frac{2}{\sqrt{\pi}} \left(x - \frac{x^3}{3} + \frac{x^5}{10} - \frac{x^7}{42} + \ldots\right) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{n!(2n+1)}
$$

These formulas provide useful approximations for various functions and can be utilized in calculations and problem-solving.

## The Power of The Taylor Formula

The Taylor formula provides valuable insights into the limitations of substitution and the use of equivalent infinitesimals.

In the case of substitution, if we replace $x\to 0$ with $cosx$, we initially obtain the value of 1. However, it is essential to consider higher order terms such as $-\frac{1}{2!}x^2$, which emerge subsequently. Neglecting these terms can lead to incorrect limit evaluations.

Similarly, when considering equivariant infinitesimals, the infinitesimal equivalent of $sinx$ as $x\to 0$ is indeed $x$. However, it is crucial to acknowledge the presence of higher order terms like $-\frac{1}{3!}x^3$. Disregarding these terms can lead to inaccuracies in limit calculations.

The Taylor formula also reinforces L'Hôpital's rule:
$$
L=\lim_{x \to 0}\frac{a_mx^m+a_{m+1}x^{m+1}+\cdots}{b_mx^m+b_{m+1}x^{m+1}+\cdots}
\overset{\text{L'Hôpital's rule}}{\Longrightarrow  }\lim_{x \to 0}\frac{ma_mx^{m-1}+(m+1)a_{m+1}x^m+\cdots}{mb_mx^{m-1}+(m+1)b_{m+1}x^m+\cdots}
=\cdots 
$$
From this perspective, it becomes evident that L'Hôpital's rule involves the step-by-step reduction of the numerator and denominator, akin to a draw. In contrast, Taylor's formula allows for a comprehensive breakdown of both the numerator and denominator into polynomials, akin to an X-ray of a function, providing a holistic view at a glance.

## Application of Taylor's Formula

When applying Taylor's formula to evaluate limits, it is crucial to include the Peano remainder term. This inclusion allows you to assess the accuracy of your approximation. Let's consider an example:
$$
\lim_{x\to 0}\frac{e^x-1-x}{x^2}=\lim_{x\to 0 }\frac{(1+x+\frac{1}{2!}x^2+o(x^2))-1-x}{x^2}=\lim_{x\to0}\frac{\frac{1}{2}x^2+o(x^2)}{x^2}=\frac{1}{2}
$$
Substitution, equivalent infinitesimals, and L'Hôpital's rule are indeed useful and concise techniques. However, it is essential to exercise caution and apply them selectively rather than indiscriminately. When unsure about their applicability, it is advisable to resort to Taylor's formula instead.

By using Taylor's formula, you can maintain a clear understanding of when these alternative methods can be employed, thereby avoiding potential inaccuracies.

### Quadratic Problems

1. Calculate limits $\lim_{x\to0}\frac{e^x-cosx-x}{x^2}$.

Since the denominator is of the second order, we expand the numerator to the second order as well:
$$
\begin{eqnarray} 
L&=&\lim_{x\to 0}\frac{(1+x+\frac{1}{2}x^2+o(x^2))-(1-\frac{1}{2}x^2+o(x^2))-x}{x^2}\\
~&=&\lim_{x\to 0}\frac{\frac{1}{2}x^2+\frac{1}{2}x^2+o(x^2)}{x^2}\\
~&=&1
\end{eqnarray} 
$$

2. Calculate limits $\lim_{x\to 0}\frac{3sin	x+x^2cos{\frac{1}{x}}}{(1+cosx)\ln(1+x)}$.

The numerator has oscillatory behavior, which presumably does not affect the limit. We will first simplify the denominator using the conclusion from before, where we factorize and keep only the lowest-order term:
$$
\begin{eqnarray} 
L&=&\lim_{x\to 0}\frac{3sinx+x^2cos{\frac{1}{x}}}{(1+1+o(x))(x+o(x))}\\
&=&\lim_{x\to0}\frac{3sinx+x^2cos{\frac{1}{x}}}{2x}
\end{eqnarray} 
$$
Now, we can split the limit calculation into two parts:
$$
L=\lim_{x\to 0}\frac{3sinx}{2x}+\frac{x}{2}cos{\frac{1}{x}}=\frac{3}{2}+0=\frac{3}{2}
$$

3. Calculate limits $L=\lim_{x\to 0}\frac{xsinxcosx-x^2}{e^x\ln(1+x)+\ln(1-x)}$

This problem involves multiplying polynomials and can be a bit tedious. If you're unsure how many terms to expand, start with expanding two terms and include the remainder. If the expansion is not accurate enough, continue expanding.

Since the numerator appears more manageable, let's expand the numerator first to determine the order of expansion:
$$
\begin{eqnarray} 
xsinxcosx-x^2&=&x(x-\frac{1}{3!}x^3+o(x^3))(1-\frac{1}{2!}x^2+o(x^2))-x^2\\
&=&x^2-\frac{1}{2}x^4+o(x^4)-\frac{1}{6}x^4+o(x^4)-x^2\\
&=&-\frac{2}{3}x^4+o(x^4)
\end{eqnarray} 
$$
Note that terms above $x^4$ in the expansion can be combined as $o(x^4)$ without the need to compute each term individually. This gives us a fourth-order infinitesimal with $x$ in the numerator. Since the coefficient of the fourth-order term is nonzero, this expansion is sufficient. If the coefficient were zero, we would continue expanding further. Next, we need to expand the denominator to the fourth order (if the numerator and denominator have different orders, the limit is either 0 or infinity, which is easy to determine and typically not asked in this form).

For the denominator:
$$
e^x\ln(1+x)+\ln(1-x)=(1+x+\frac{1}{2}x^2+o(x^2))(x-\frac{1}{2}x^2+o(x^2))+(-x-\frac{1}{2}x^2+o(x^2))
$$
It is evident that this expansion is not sufficient, as the form of $o(x^2)$ appearing is uncertain and can affect the limits. We further increase the accuracy of the expansion by:
$$
\begin{eqnarray} 
&&e^x\ln(1+x)+\ln(1-x)\\
&=&(1+x+\frac{1}{2}x^2+\frac{1}{6}x^3+o(x^3))(x-\frac{1}{2}x^2+\frac{1}{3}x^3-\frac{1}{4}x^4+o(x^4))+(-x-\frac{1}{2}x^2-\frac{1}{3}x^3-\frac{1}{4}x^4+o(x^4))\\
&=&x-\frac{1}{2}x^2+\frac{1}{3}x^3-\frac{1}{4}x^4+x^2-\frac{1}{2}x^3+\frac{1}{3}x^4+\frac{1}{2}x^3-\frac{1}{4}x^4+\frac{1}{6}x^4+o(x^4)-x-\frac{1}{2}x^2-\frac{1}{3}x^3-\frac{1}{4}x^4+o(x^4)\\
&=&(-\frac{1}{4}+\frac{1}{3}-\frac{1}{4}+\frac{1}{6}-\frac{1}{4})x^4+o(x^4)\\
&=&-\frac{1}{4}x^4+o(x^4)
\end{eqnarray}
$$
In summary:
$$
L=\lim_{x\to 0}\frac{-\frac{2}{3}x^4+o(x^4)}{-\frac{1}{4}x^4+o(x^4)}=\frac{8}{3}
$$

### Compound Function Questions

When dealing with Taylor's formula, it is essential to consider the function approaching zero as a whole.

1. Calculate limits $L=\lim _{x \rightarrow 0} \frac{(1-\cos x)(x-\ln (1+\tan x))}{\sin ^{4} x}$.

The factorization of the denominator and numerator in the first step is well handled, while the factorization of the second term in the numerator poses some challenges. Let's consider expanding $tanx$ as a whole.
$$
L=\lim_{x\to0}\frac{\frac{1}{2}x^2(x-(tanx-\frac{1}{2}(tanx)^2+o((tanx)^2)))}{x^4}
$$
Since we know that $\tan x=x+o(x)$, we can substitute $(\tan x)^2=x^2+o(x^2)$, resulting in:
$$
L=\lim_{x\to 0}\frac{x-tanx+\frac{1}{2}x^2+o(x^2)}{2x^2}=\lim_{x\to 0}\frac{x-tanx}{2x^2}+\frac{1}{4}
$$
By Section 2, we can determine that $x-\tan x$ is a third-order infinitesimal. Hence:
$$
L=0+\frac{1}{4}=\frac{1}{4}
$$

2. Calculate limits $L=\lim_{x\to0}\frac{2\ln(cosx)+x^2}{sin^2x-x^2}$.

We can handle the denominator more effectively by the following approach:
$$
\begin{eqnarray} 
sin^2x-x^2&=&(sinx+x)(sinx-x)\\
&=&2x(-\frac{1}{3!}x^3+o(x^3))\\
&=&-\frac{1}{3}x^4+o(x^4)
\end{eqnarray}
$$
Now, let's expand the numerator to the fourth order, taking into account the entire expression $(\cos x-1)$:
$$
\begin{eqnarray} 
2\ln(cosx)+x^2&=&2\ln(1+cosx-1)+x^2\\
&=&2((cosx-1)-\frac{1}{2}(cosx-1)^2+o((cosx-1)^2))+x^2\\
&=&2(-\frac{1}{2}x^2+\frac{1}{4!}x^4+o(x^4)-\frac{1}{2}(-\frac{1}{2}x^2+o(x^2))^2+o(x^4))+x^2\\
&=&2(-\frac{1}{2}x^2+\frac{1}{24}x^4-\frac{1}{8}x^4+o(x^4))+x^2\\
&=&-\frac{1}{6}x^4+o(x^4)
\end{eqnarray}
$$
Therefore,
$$
L=\lim_{x\to 0}\frac{-\frac{1}{6}x^4+o(x^4)}{-\frac{1}{3}x^4+o(x^4)}=\frac{1}{2}
$$

### Power Finger Function Questions

When dealing with idempotent functions of the form $f(x)^{g(x)}$, it is common to take the logarithm and utilize the approximation $\ln(1+\alpha(x))=\alpha(x)+o(\alpha(x))$.

1. Calculate limits $L=\lim_{x\to 0}(\frac{x}{sinx}^{\frac{1}{x^2}})$.

To simplify the expression, we can take the natural logarithm:
$$
\begin{eqnarray} 
\ln L&=&\lim_{x\to 0}\frac{1}{x^2}\ln{\frac{x}{sinx}}\\
&=&\lim_{x\to0}\frac{1}{x^2}\ln(1+\frac{x}{sinx}-1)\\
&=&\lim_{x\to 0}\frac{1}{x^2}(\frac{x}{sinx}-1)\\
&=&\lim_{x\to 0}\frac{x-sinx}{x^2sinx}\\
&=&\lim_{x\to 0}\frac{x-(x-\frac{1}{3!}x^3+o(x^3))}{x^3}\\
&=&\frac{1}{6}
\end{eqnarray}
$$
Taking the exponentiation of both sides, we find:
$$
L=e^{\frac{1}{6}}
$$
