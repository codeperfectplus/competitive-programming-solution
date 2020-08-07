#include "isogram.h"
#include <string>
#include <cctype>

namespace isogram {

    bool is_isogram(std::string word)
    {
        for(auto a : word)
        {
            if(std::isalpha(a))
            {
                if(std::find(a) != std::rfind(a))
                {
                    return false;
                }
            }
        }
        return true;
    }

}  // namespace isogram