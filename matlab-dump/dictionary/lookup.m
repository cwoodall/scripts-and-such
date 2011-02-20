function [ value ] = lookup( key, dict )
% lookup( key, dict ): searches for the key, value pair in dictionary 
%   dict.
%
%   key  :  The key, usually a string
%   dict : "a dictionary" which is defined by this function as a cell array
%           with a key column and a value column (n x 2 cell array).   
    
    keys = dict(:,1)';
    values = dict(:,2)';
    
    for i = 1:length(keys)
        if isequal(keys(i), cellstr(key))
           value = cell2mat(values(i));
        end
    end
end

