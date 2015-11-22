<html>
<?php
	
	if (isset($_GET['mode']) && ($_GET['mode'] == 'XxX')){
		if (isset($_GET['password']) && ($_GET['password'] == 'fordfiesta')){
			?><Body><?php
			require("playlist/porn.php");
			?></Body><?php
		}else
			?>
			<Body>
			<h1>SORRY YOU SHOULDNT BE HERE !!!!!!!!</h1>
			</body>
			<?php
			
		
	}

?>
</html>