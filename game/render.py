ahalf_x = 85
ahalf_y = 45
phalf_x = 2.5
phalf_y = 12
def simulate_player( *p,*dp, ddp,  dt):
{
	ddp -= *dp * 10.f;

	*p = *p + *dp * dt + ddp * dt * dt * .5f;
	*dp = *dp + ddp * dt;


	if (*p + phalf_y > ahalf_y)
	{
		*p = ahalf_y - phalf_y;
		*dp *= 0;
	}
	else if (*p - phalf_y < -ahalf_y)
	{
		*p = -ahalf_y + phalf_y;
		*dp *= 0;
	}
}