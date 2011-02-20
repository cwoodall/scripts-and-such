% lookup_example.m: demonstrates the lookup function

% Make your menu
opt = menu('Select a color', 'Indigo', 'Yellow', 'Sky Blue');
% Right afterwards throw the options into a 'dictionary' for use with the
% lookup function
colors = {'indigo', 1; 'yellow', 2; 'sky blue', 3 };

% Take care of your actions and sections statements
if opt == lookup('indigo', colors) 
    % Notice that the color is easy to figure out
    disp('You picked indigo')
elseif opt == lookup('yellow', colors)
    disp('You picked yellow')
elseif opt == lookup('sky blue', colors)
    disp('You picked sky blue')
else
    disp('ColorError')
end