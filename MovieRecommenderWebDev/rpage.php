<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Movie Recommender</title>
		<meta name="keywords" content="css3, transforms, shadow, shading, 3d, box shadow" />
		<link rel="shortcut icon" href="../favicon.ico">
		<link rel="stylesheet" type="text/css" href="normalize.css" />
		<link rel="stylesheet" type="text/css" href="demo.css" />
		<link rel="stylesheet" type="text/css" href="style.php" />
		<script src="modernizr.custom.js"></script>
	</head>
	<body>
		<div class="container">
			<!-- Top Navigation -->
			<header>
				<h1>Movies</h1>  
			</header>
			<div class="wrapper">
				<ul class="stage clearfix">

					<li class="scene">
						<div class="movie" onclick="return true">
							<div class="poster"></div>
							<div class="info">
								<header>
									<h1><?php $rm=file_get_contents("finalrm.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[0];?></h1>
									<span class="year"><?php $rm=file_get_contents("title.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[0];?></span>
									<span class="rating">PG</span>
									<span class="duration">130 minutes</span>
								</header>
								<p>
								<?php $rm=file_get_contents("plot.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[0];?>
								</p>
							</div>
						</div>
					</li>

					<li class="scene">
						<div class="movie" onclick="return true">
							<div class="poster"></div>
							<div class="info">
								<header>
									<h1><?php $rm=file_get_contents("finalrm.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[1];?></h1>
									<span class="year"><?php $rm=file_get_contents("title.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[1];?></span>
									<span class="rating">NR</span>
									<span class="duration">83 minutes</span>
								</header>
								<p>
								<?php $rm=file_get_contents("plot.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[1];?>
								</p>
							</div>
						</div>
					</li>

					<li class="scene">
						<div class="movie" onclick="return true">
							<div class="poster"></div>
							<div class="info">
								<header>
									<h1><?php $rm=file_get_contents("finalrm.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[2];?></h1>
									<span class="year"><?php $rm=file_get_contents("title.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[2];?></span>
									<span class="rating">NR</span>
									<span class="duration">95 minutes</span>
								</header>
								<p>
								<?php $rm=file_get_contents("plot.txt");
                                        $arr= explode('&',$rm);
                                        echo $arr[2];?>
								</p>
							</div>
						</div>
					</li>

				</ul>
			</div><!-- /wrapper -->
		</div><!-- /container -->
	</body>
</html>