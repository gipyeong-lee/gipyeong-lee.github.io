---
layout: learn-module
title: Fundamentals of Robot Kinematics
course_slug: precise-robot-hand
course_data_key: precise-robot-hand-en
course_locale: en
lang: en
ref: learn:precise-robot-hand:robot-mechanics-fundamentals
translations:
- lang: ko
  url: /learn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: en
  url: /learn/en/precise-robot-hand/robot-mechanics-fundamentals/
- lang: ja
  url: /learn/ja/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-cn
  url: /learn/zh-cn/precise-robot-hand/robot-mechanics-fundamentals/
- lang: zh-tw
  url: /learn/zh-tw/precise-robot-hand/robot-mechanics-fundamentals/
module_id: M1
permalink: /learn/en/precise-robot-hand/robot-mechanics-fundamentals/
no_ads: true
generated_by: mindtickle-studio
generation_run_id: b409b9219ba4488bb342aac4eb8f5a73
translation_run_id: 0886d1415b8d413b8654c2195ac9ac00
id: M1
slug: robot-mechanics-fundamentals
phase_id: P1
estimated_hours: 10.0
prerequisites: []
objectives:
- Understand the basic definitions of robot kinematics and the concept of rigid-body
  transformation.
- Learn how to mathematically describe the position and orientation of a robot using
  coordinate system transformations and rotation matrices.
- Acquire basic kinematic theories for designing an 5-finger robotic hand and learn
  analytical approaches.
worked_examples:
- 'Example 1: Find the end position $(x, y)$ of a robot link with 1 rotation joints
  in a 2-dimensional plane. When the joint angle is $\theta$ and link length is $L$,
  $x = L \cos(\theta)$ and $y = L \sin(\theta)$ [S1].'
- 'Example 2: Describe a 2-dimensional rotation matrix $R$ that rotates by $\theta$
  about the $x$-axis. $R = \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta)
  \\ \cos(\theta) \end{bmatrix}$ [S1].'
lab:
  title: Coordinate System Transformation Simulation and Basic Kinematic Analysis
  steps:
  - Create an 2-link planar manipulator model using kinematic analysis software.
  - Observe the trajectory of the end position while changing the joint angles.
  - Derive inverse kinematic equations manually and compare them with the simulation
    results.
  safety:
  - Adjust screen brightness and take periodic breaks when working on computers.
  - This practice is simulation-based, so hardware energization is not required.
  deliverables:
  - Summary report including the kinematic analysis process
  - Trajectory simulation result images
assignment:
  title: Kinematic Modeling of 5-Finger Robotic Hand Joint Structure
  deliverables:
  - Forward kinematics equation derivation results for 1 robot fingers
  - Fingertip position change prediction data according to joint angle changes
  rubric:
  - Mathematical accuracy of rotation matrices
  - Physical validity of forward kinematics equations
  - Logical structure of the report
quiz:
- question: What is the discipline in robot kinematics that describes only motion
    without considering forces or torques?
  choices:
  - Dynamics
  - Kinematics
  - Control Theory
  - Material Mechanics
  answer_index: 1
  explanation: Kinematics is the study of motion focused on position, velocity, and
    acceleration, excluding force and torque [S1].
- question: In 3-dimensional space, what matrix defines the orientation between two
    coordinate systems?
  choices:
  - Rotation Matrix
  - Mass Matrix
  - Stiffness Matrix
  - Damping Matrix
  answer_index: 0
  explanation: A rotation matrix is an orthogonal matrix that mathematically transforms
    orientation between two coordinate systems [S1].
completion_criteria:
- Completion of theory lectures
- Submission of kinematic analysis result report
- Achieve 100 points on the theory quiz
source_ids:
- S1
---

## Fundamentals of Robot Kinematics

Robot kinematics is the study of robot motion in terms of position, velocity, and acceleration without considering forces or torques [S1]. The starting point for designing a manipulator, such as a robotic hand, is to describe the state of each joint as coordinates in space.

### 1. Rigid-body Transformation
Each link of a robot is considered a rigid body, and the transformation from one coordinate system to another is represented as a combination of rotation and translation. In 3-dimensional space, the rotation matrix $R$ is an orthogonal matrix, through which the orientation between two coordinate systems is defined [S1].

### 2. Forward Kinematics
Forward kinematics is the process of calculating the position and orientation of the end-effector when the joint variables (angles or positions) are known. For an 5-finger robotic hand, the position of the fingertips is obtained through the finger joint angles ($\theta_1, \theta_2, \dots, \theta_n$).

### 3. Inverse Kinematics
Inverse kinematics is the process of finding the joint variables required to achieve a desired fingertip position. It consists of non-linear equations, and solutions may not exist or multiple solutions may occur [S1].
