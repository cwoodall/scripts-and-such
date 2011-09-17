function out = each( iterator, action )
    % each(iterable, action)
    out = [];
    for i = iterator
        out = [out action(i)];
    end
end