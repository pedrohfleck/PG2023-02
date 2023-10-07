#version 400

layout (location = 0) in vec3 position;

uniform mat4 projection;

void main()
{
	
	//...pode ter mais linhas de código aqui!
	gl_Position = projection * vec4(position, 1.0);
}